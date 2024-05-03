import stripe
from config.settings import SECRET_KEY_STRIPE
stripe.api_key = SECRET_KEY_STRIPE


def create_price(amount, product):
    price = stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        nickname="Покупка",
        product=product,
    )
    return price


def create_session(price):
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/success",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
