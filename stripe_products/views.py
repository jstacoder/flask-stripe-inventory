from flask import json
from flask_views.base import TemplateView, SessionViewMixin
from flask_views.edit import FormMixin, ProcessFormMixin
import stripe

from stripe_products.forms import BaseProductForm


class ListProductView(TemplateView):
    template_name = 'list_product.html'

    def __init__(self, **kwargs):
        if 'blueprint' in kwargs:
            print('saving bluepriont')
            self.blueprint = kwargs.pop('blueprint')
        super().__init__(**kwargs)

    def get_context_data(self, **kwargs):
        api_key = self.blueprint.stripe_api_key
        print(api_key)
        stripe.api_key = api_key
        products = stripe.Product.list(limit=5).data
        print(products)
        return dict(products=products)


class AddProductView(FormMixin, ProcessFormMixin, SessionViewMixin, TemplateView):
    template_name = 'add_product.html'
    form_class = BaseProductForm

    success_url = '/shop/success'

    def form_valid(self, form=None):
        form_data = json.dumps(form.data)
        print(form_data)
        self.session['form_data'] = form_data
        return super().form_valid(form=form)


class SuccessView(SessionViewMixin, TemplateView):
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        form_data = self.session.get('form_data')

        print('here, ',form_data)
        return dict(form_data=form_data)

