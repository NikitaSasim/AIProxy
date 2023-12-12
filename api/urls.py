from django.urls import path
from .views import GptApiView

urlpatterns = [
    path("gpt", GptApiView.as_view(), name="gpt"),
    ]
