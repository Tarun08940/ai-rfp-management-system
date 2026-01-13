from django.urls import path
from .views import create_rfp_from_text

urlpatterns = [
    path("rfps/create-from-text", create_rfp_from_text),
]
