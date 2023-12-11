from django.urls import path
from .views import GptApiView

urlpatterns = [
    path("post_feedback", GptApiView.as_view(), name="gpt"),
    ]
