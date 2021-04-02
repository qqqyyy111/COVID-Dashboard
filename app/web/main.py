from . import web


@web.route('/')
def index():
    return "hello world"