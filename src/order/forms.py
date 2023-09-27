from django import forms

from order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["company_name", "company_tax_id", "legal_adress", "post_adress",
                  "company_email", "phone_number", "delivery_adress", "position",
                  "position_name", "bank_details", "comments"]

    def __init__(self, profile=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if profile:
            self.fields["company_name"].initial = profile.company_name
            self.fields["company_tax_id"].initial = profile.company_tax_id
            self.fields["legal_adress"].initial = profile.legal_adress
            self.fields["post_adress"].initial = profile.post_adress
            self.fields["company_email"].initial = profile.company_email
            self.fields["phone_number"].initial = profile.phone_number
            self.fields["delivery_adress"].initial = profile.delivery_adress
            self.fields["position"].initial = profile.position
            self.fields["position_name"].initial = profile.position_name
            self.fields["bank_details"].initial = profile.bank_details
