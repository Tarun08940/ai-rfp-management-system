from django.db import models


class RFP(models.Model):
    title = models.CharField(max_length=255)
    raw_input_text = models.TextField()
    structured_data = models.JSONField()

    budget = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True
    )
    delivery_deadline = models.DateField(null=True, blank=True)
    payment_terms = models.CharField(max_length=255, null=True, blank=True)
    warranty_requirement = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Proposal(models.Model):
    rfp = models.ForeignKey(
        RFP, on_delete=models.CASCADE, related_name="proposals"
    )
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name="proposals"
    )

    raw_email_text = models.TextField()
    parsed_data = models.JSONField()

    total_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True
    )
    delivery_timeline = models.CharField(max_length=255, null=True, blank=True)
    warranty = models.CharField(max_length=255, null=True, blank=True)
    payment_terms = models.CharField(max_length=255, null=True, blank=True)

    ai_summary = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vendor.name} → {self.rfp.title}"
