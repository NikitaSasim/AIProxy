from django.urls import path
from .views import GptApiView, GigaApiView

urlpatterns = [
    path("gpt", GptApiView.as_view(), name="gpt"),
    path("giga", GigaApiView.as_view(), name="giga")
    ]
