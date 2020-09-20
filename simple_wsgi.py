import pprint
import datetime


"""
When called by the server, the application object must return an iterable yielding zero or more bytestrings. 
This can be accomplished in a variety of ways, such as by returning a list of bytestrings, or by the application 
being a generator function that yields bytestrings, or by the application being a class whose instances are iterable. 
Regardless of how it is accomplished, the application object must always return an iterable yielding zero or more 
bytestrings.
"""


def simplest_wsgi_app(environ, start_response):
    pprint.pprint(environ, indent=2)
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello, world!', datetime.datetime.utcnow().isoformat().encode()]


application = simplest_wsgi_app
