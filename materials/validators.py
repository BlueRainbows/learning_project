from rest_framework.serializers import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        the_correct_url = "https://www.youtube.com/"
        get_value = dict(value).get(self.field)
        if get_value is not None:
            if the_correct_url.lower() not in get_value.lower():
                raise ValidationError("Источником ссылки должен быть youtube.com")
