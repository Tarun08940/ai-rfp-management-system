from django.urls import path
from . import views

urlpatterns = [
    path("rfps/create", views.create_rfp_page),
    path("vendors", views.vendors_page),
    path("rfps/send", views.send_rfp_page),
    path("rfps/compare", views.compare_page),
]
