# -*- coding: utf-8 -*-


class ClacksMixin(object):
    """
    Django CBV Mixin that will add the X-Clacks-Overhead header to GET responses.
    """

    def dispatch(self, request, *args, **kwargs):
        response = super(ClacksMixin, self).dispatch(request, *args, **kwargs)
        if request.method == 'GET':
            response['X-Clacks-Overhead'] = 'GNU Terry Pratchett'
        return response
