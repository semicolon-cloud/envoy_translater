
from logging import getLogger

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from envoy_translator import utils
from envoy_translator.api.utils import parse_filters
from envoy_translator.listeners.models import Listener, Route


class APIViewWithLogger(APIView):
    """
    APIView with a logger.
    """

    def __init__(self, *args, **kwargs):
        super(APIViewWithLogger, self).__init__(*args, **kwargs)
        self.logger = getLogger("envoy_translator")


class ListenerList(APIViewWithLogger):
    
    @utils.authenticated
    @parse_filters
    def get(self, request, filters=None):

        page = request.GET.get("page", 1)
        listeners_per_page = request.GET.get("listeners_per_page", None)

        if not filters:
            filters = {}

        if filters:
            listeners = Listener.objects.filter(**filters).order_by("-created_on")
        else:
            listeners = Listener.objects.all().order_by("-created_on")

        if listeners_per_page:
            paginator = Paginator(listeners, listeners_per_page)
            try:
                listeners = paginator.page(page)
            except EmptyPage:
                return Response({"errors": ["Empty page"]}, status=400)
            except PageNotAnInteger:
                return Response({"errors": ["Page not an integer"]}, status=400)

        listener_list = []
        for listener in listeners:
            listener_list.append(listener.to_dict())

        if listeners_per_page:
            return Response(
                {
                    "listeners": listener_list,
                    "pages": paginator.num_pages,
                    "has_more": listeners.has_next(),
                    "has_prev": listeners.has_previous(),
                },
                status=200,
            )
            # NOTE(amelia): 'has_more'and 'has_prev' names are
            # based on the horizon pagination table pagination names <-- copied from adjutant
        else:
            return Response({"listeners": listener_list})

    @utils.admin
    def post(self, request): # create
        if request.data["type"] not in ["tls", "http"]:
            return Response({"errors": ["Invalid type"]}, status=400)

        listener = Listener.objects.create(
            listener_name=request.data["listener_name"],
            description=request.data["description"],
            ip=request.data["ip"],
            external_ip=request.data["external_ip"],
            port=request.data["port"],
            type=request.data["type"],
        )

        return Response({"listener": listener.to_dict()})

class ListenerDetail(APIViewWithLogger):
    @utils.admin
    @parse_filters
    def get(self, request, listener_id):
        listener = Listener.objects.get(uuid=listener_id)

        routes = Route.objects.filter(listener=listener)
        routes_list = []
        for route in routes:
            routes_list.append(route.to_dict())

        return Response({"listener": listener.to_dict(), "routes": routes_list})


class RouteList(APIViewWithLogger):
    @utils.authenticated
    @parse_filters
    def get(self, request, filters=None):
        page = request.GET.get("page", 1)
        project_id = request.GET.get("project_id", request.keystone_user["project_id"])
        roles = set(request.keystone_user.get("roles", []))

        if not roles & {'admin'}:
            if project_id != request.keystone_user["project_id"]:
                return Response({"errors": ["Can not impersonate project id"]}, status=403)
            if project_id is None:
                return Response({"errors": ["Bring project token"]}, status=403)

        routes_per_page = request.GET.get("routes_per_page", None)

        if not filters:
            filters = {}

        if project_id != 'null':
            filters["project_id__exact"] = project_id

        if filters:
            routes = Route.objects.filter(**filters).order_by("-created_on")
        else:
            routes = Route.objects.all().order_by("-created_on")

        if routes_per_page:
            paginator = Paginator(routes, routes_per_page)
            try:
                routes = paginator.page(page)
            except EmptyPage:
                return Response({"errors": ["Empty page"]}, status=400)
            except PageNotAnInteger:
                return Response({"errors": ["Page not an integer"]}, status=400)

        route_list = []
        for route in routes:
            route_list.append(route.to_dict())


        if routes_per_page:
            return Response(
                {
                    "routes": route_list,
                    "pages": paginator.num_pages,
                    "has_more": routes.has_next(),
                    "has_prev": routes.has_previous(),
                },
                status=200,
            )
            # NOTE(amelia): 'has_more'and 'has_prev' names are
            # based on the horizon pagination table pagination names <-- copied from adjutant
        else:
            return Response({"routes": route_list})

    @utils.mod_or_admin
    def post(self, request):
        if not isinstance(request.data["domain_names"], list):
            return Response({"errors": ["Domain names must be list"]}, status=400)


        listener = Listener.objects.get(uuid=request.data["listener_id"])

        target_servers = []
        for obj in request.data["target_servers"]:
            target_servers.append({
                'ip': obj["ip"],
                'port': obj["port"]
            })

        route = Route.objects.create(
            domain_names=','.join(request.data["domain_names"]),
            keystone_user=request.keystone_user["username"],
            project_id=request.keystone_user["project_id"],
            target_servers=target_servers,
            listener=listener,
        )

        return Response({"route": route.to_dict()})

class RouteDetail(APIViewWithLogger):
    @utils.authenticated
    @parse_filters
    def get(self, request, route_id, filters=None):
        route = Route.objects.get(uuid=route_id)

        if route.project_id != request.keystone_user["project_id"]:
            return Response({"errors": ["Forbidden"]}, status=403)

        return Response(route.to_dict())

    @utils.mod_or_admin
    @parse_filters
    def delete(self, request, route_id):
        route = Route.objects.get(uuid=route_id)

        if route.project_id != request.keystone_user["project_id"]:
            return Response({"errors": ["Forbidden"]}, status=403)

        route.delete()
        return Response(route.to_dict())

    def put(self, request, route_id):
        route = Route.objects.get(uuid=route_id)
        if route.project_id != request.keystone_user["project_id"]:
            return Response({"errors": ["Forbidden"]}, status=403)

        if not isinstance(request.data["domain_names"], list):
            return Response({"errors": ["Domain names must be list"]}, status=400)


        target_servers = []
        for obj in request.data["target_servers"]:
            target_servers.append({
                'ip': obj["ip"],
                'port': obj["port"]
            })
        route.target_servers.set(target_servers)
        route.domain_names = ','.join(request.data["domain_names"])
        route.updated_on = timezone.now()

        route.save()
        return Response(route.to_dict())