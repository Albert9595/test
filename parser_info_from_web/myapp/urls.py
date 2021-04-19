from django.urls import path
from .views import GetParsInfo



urlpatterns = [
    path("", GetParsInfo.as_view(), name="index")
]
