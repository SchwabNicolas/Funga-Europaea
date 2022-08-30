from django.urls import path, include
from funga_europaea import settings
from funga_europaea.dev_views import (
    Error400View,
    Error403View,
    Error404View,
    Error500View
)

app_name = "dev"

if settings.DEBUG == True:
    urlpatterns = [
        path("__reload__/", include("django_browser_reload.urls")),
        path("400/", Error400View.as_view(), name="400"),
        path("403/", Error403View.as_view(), name="403"),
        path("404/", Error404View.as_view(), name="404"),
        path("500/", Error500View.as_view(), name="500"),
    ]
else: 
    urlpatterns = []