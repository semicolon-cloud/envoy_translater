from django.conf.urls import url

from envoy_translator.api import views

urlpatterns = [
    url(r"^listeners/?$", views.ListenerList.as_view()),
    url(r"^listeners/(?P<listener_id>\w+)/?$", views.ListenerDetail.as_view()),
    url(r"^routes/?$", views.RouteList.as_view()),
    url(r"^routes/(?P<route_id>\w+)/?$", views.RouteDetail.as_view()),
]