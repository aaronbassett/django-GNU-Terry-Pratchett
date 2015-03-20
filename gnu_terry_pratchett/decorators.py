from functools import wraps


def clacks_overhead(fn):
    """
    A Django view decorator that will add the `X-Clacks-Overhead` header.

    Usage:

        @clacks_overhead
        def my_view(request):
            return my_response

    """
    @wraps(fn)
    def _wrapped(*args, **kw):
        response = fn(*args, **kw)
        response['X-Clacks-Overhead'] = 'GNU Terry Pratchett'
        return response

    return _wrapped

