import requests


def before_scenario(context, scenario):
    context.base_url = 'https://jsonplaceholder.typicode.com'


def after_scenario(context, scenario):
    pass


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_all(context):
    pass


def after_all(context):
    pass
