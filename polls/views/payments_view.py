from django_pesapal.views import PaymentRequestMixin
from django.views.generic import TemplateView

class PaymentView(TemplateView, PaymentRequestMixin):
    template_name = "polls/index.html"

    def get_context_data(self, **kwargs):
        ctx = super(PaymentView, self).get_context_data(**kwargs)

        order_info = {
            "amount": 10,
            "description": "Payment for X",
            "reference": 2,
            "email": "pesapal@example.com",
        }

        ctx["pesapal_url"] = self.get_payment_url(**order_info)
        return ctx