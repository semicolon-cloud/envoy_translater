from django.conf.urls import url

from envoy_translater.api import views

urlpatterns = [
    url(r"^listeners/?$", views.ListenerList.as_view()),
    # url(r"^listeners/(?P<id>\w+)/?$", None),
    # url(r"^routes/?$", None),
    # url(r"^routes/(?P<id>\w+)/?$", None),
]