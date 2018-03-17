import re


def camel_to_snake(s):
    return re.sub("([A-Z]+)", "_\\1", s).lower().lstrip("_")


class Vehicle(object):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, camel_to_snake(key), value)
