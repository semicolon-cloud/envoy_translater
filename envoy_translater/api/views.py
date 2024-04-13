from logging import getLogger

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework.views import APIView

from envoy_translater import utils
from envoy_translater.api.utils import parse_filters
from envoy_translater.listeners.models import Listener


class APIViewWithLogger(APIView):
    """
    APIView with a logger.
    """

    def __init__(self, *args, **kwargs):
        super(APIViewWithLogger, self).__init__(*args, **kwargs)
        self.logger = getLogger("envoy_translater")


class ListenerList(APIViewWithLogger):
    
    @utils.authenticated
    @parse_filters
    def get(self, request, filters=None):

        page = request.GET.get("page", 1)
        listeners_per_page = request.GET.get("listeners_per_page", None)

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

        listener = Listener.objects.create(
            listener_name=request.data["listener_name"],
            description=request.data["description"],
            ip=request.data["ip"],
            external_ip=request.data["external_ip"],
            port=request.data["port"],
            type=request.data["type"],
        )

        return Response({"listener": listener.to_dict()})

