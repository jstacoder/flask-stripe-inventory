import os
from flask import Flask, render_template, request
from stripe_products import FlaskStripeManager

app = Flask(__name__)

app.config.STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY')


stripe_manager = FlaskStripeManager(app=app)

@app.route('/')
def hello_world():
    return 'hello world'



if __name__ == '__main__':
    app.run()
