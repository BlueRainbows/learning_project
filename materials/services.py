import stripe
from config.settings import SECRET_KEY_STRIPE
stripe.api_key = SECRET_KEY_STRIPE


def create_product_course(name, description):
    course = stripe.Product.create(
        name=name,
        description=description,
    )
    return course.get('id')


def create_product_lesson(name, description):
    lesson = stripe.Product.create(
        name=name,
        description=description,
    )
    return lesson.get('id')
