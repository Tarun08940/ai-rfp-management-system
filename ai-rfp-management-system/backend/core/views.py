import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import RFP
from .services.ai_service import generate_structured_rfp


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
