from django.urls import path
from .views import create_rfp_from_text

urlpatterns = [
    path("rfps/create-from-text", create_rfp_from_text),
]


from .views import (
    create_rfp_from_text,
    create_vendor,
    list_vendors,
    send_rfp_to_vendors,
)

urlpatterns = [
    path("rfps/create-from-text", create_rfp_from_text),
    path("vendors", list_vendors),
    path("vendors/create", create_vendor),
    path("rfps/send", send_rfp_to_vendors),
]
