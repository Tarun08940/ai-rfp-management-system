import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import RFP
from .services.ai_service import generate_structured_rfp
from .models import Vendor



@csrf_exempt
@require_POST
def create_rfp_from_text(request):
    body = json.loads(request.body)
    user_input = body.get("text")

    if not user_input:
        return JsonResponse({"error": "Text input is required"}, status=400)

    structured = generate_structured_rfp(user_input)

    rfp = RFP.objects.create(
        title=structured.get("title", "Untitled RFP"),
        raw_input_text=user_input,
        structured_data=structured,
        budget=structured.get("budget"),
        payment_terms=structured.get("payment_terms"),
        warranty_requirement=structured.get("warranty_requirement"),
    )

    return JsonResponse(
        {
            "id": rfp.id,
            "title": rfp.title,
            "structured_data": rfp.structured_data,
        }
    )


@csrf_exempt
@require_POST
def create_vendor(request):
    body = json.loads(request.body)

    name = body.get("name")
    email = body.get("email")

    if not name or not email:
        return JsonResponse({"error": "Name and email required"}, status=400)

    vendor = Vendor.objects.create(name=name, email=email)

    return JsonResponse({"id": vendor.id, "name": vendor.name, "email": vendor.email})



def list_vendors(request):
    vendors = Vendor.objects.all()
    data = [
        {"id": v.id, "name": v.name, "email": v.email}
        for v in vendors
    ]
    return JsonResponse(data, safe=False)


from django.core.mail import send_mail
from .models import RFP


@csrf_exempt
@require_POST
def send_rfp_to_vendors(request):
    body = json.loads(request.body)

    rfp_id = body.get("rfp_id")
    vendor_ids = body.get("vendor_ids", [])

    if not rfp_id or not vendor_ids:
        return JsonResponse({"error": "rfp_id and vendor_ids required"}, status=400)

    rfp = RFP.objects.get(id=rfp_id)
    vendors = Vendor.objects.filter(id__in=vendor_ids)

    email_body = f"""
RFP: {rfp.title}

Details:
{rfp.raw_input_text}

Please reply to this email with your proposal including:
- Total price
- Delivery timeline
- Warranty
- Payment terms
"""

    for vendor in vendors:
        send_mail(
            subject=f"RFP Request: {rfp.title}",
            message=email_body,
            from_email=EMAIL_HOST_USER,
            recipient_list=[vendor.email],
            fail_silently=False,
        )

    return JsonResponse({"status": "RFP emails sent"})


from .models import Proposal
from .services.proposal_ai_service import parse_vendor_email


@csrf_exempt
@require_POST
def create_proposal_from_email(request):
    body = json.loads(request.body)

    rfp_id = body.get("rfp_id")
    vendor_id = body.get("vendor_id")
    email_text = body.get("email_text")

    if not rfp_id or not vendor_id or not email_text:
        return JsonResponse(
            {"error": "rfp_id, vendor_id, and email_text are required"},
            status=400
        )

    parsed = parse_vendor_email(email_text)

    proposal = Proposal.objects.create(
        rfp_id=rfp_id,
        vendor_id=vendor_id,
        raw_email_text=email_text,
        parsed_data=parsed,
        total_price=parsed.get("total_price"),
        delivery_timeline=parsed.get("delivery_timeline"),
        warranty=parsed.get("warranty"),
        payment_terms=parsed.get("payment_terms"),
        ai_summary=parsed.get("summary"),
    )

    return JsonResponse(
        {
            "id": proposal.id,
            "vendor": proposal.vendor.name,
            "rfp": proposal.rfp.title,
            "parsed_data": proposal.parsed_data,
        }
    )
