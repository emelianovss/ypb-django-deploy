from simple_wsgi import application as _


def middleware_wsgi_app(environ, start_response):
    environ['_MY_MIDDLEWARE'] = 'THIS IS MIDDLEWARE'
    yield from _(environ, start_response)


application = middleware_wsgi_app
