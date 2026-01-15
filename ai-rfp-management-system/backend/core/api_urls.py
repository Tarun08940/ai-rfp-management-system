from django.urls import path
from . import views

urlpatterns = [
    path("rfps/create-from-text", views.create_rfp_from_text),

    path("vendors", views.list_vendors),
    path("vendors/create", views.create_vendor),

    path("rfps/send", views.send_rfp_to_vendors),

    path("proposals/create-from-email", views.create_proposal_from_email),

    path("rfps/<int:rfp_id>/proposals", views.list_proposals_for_rfp),
    path("rfps/<int:rfp_id>/recommendation", views.recommend_vendor_for_rfp),
    path("rfps", views.list_rfps),

]
