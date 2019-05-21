import os

from flask import Blueprint
from .views import AddProductView, SuccessView, ListProductView
import stripe


class FlaskStripeManager(object):
    stripe_api_key = None
    blueprint = None

    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app=app)

    def init_app(self, app):
        self.stripe_api_key = app.config.STRIPE_API_KEY
        if 'SECRET_KEY' not in app.config:
            app.config.SECRET_KEY = 'secret'

        self.blueprint = Blueprint(
            'stripe',
            'stripe',
            template_folder='templates',
            url_prefix='/shop',
            root_path=os.path.dirname(__file__),
        )
        self.blueprint.add_url_rule(
            '/product/add',
            view_func=AddProductView.as_view('add_product'),

        )
        self.blueprint.add_url_rule(
            '/success',
            view_func=SuccessView.as_view('success')
        )

        self.blueprint.add_url_rule(
            '/product/list',
            view_func=ListProductView.as_view('product_list', blueprint=self)
        )


        app.register_blueprint(self.blueprint)
