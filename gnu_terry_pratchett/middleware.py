# -*- coding: utf-8 -*-


class ClacksMiddleware(object):

    def process_response(self, request, response):
        response['X-Clacks-Overhead'] = 'GNU Terry Pratchett'

        return response
