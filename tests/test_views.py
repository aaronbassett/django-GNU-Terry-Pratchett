#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.test import RequestFactory

from django.views.generic import View

from nose.tools import eq_, ok_

from gnu_terry_pratchett.views import ClacksMixin


class GNUTerryPratchett(ClacksMixin, View):
    def get(self, request):
        return HttpResponse("Death can't have him")


def test_cbv_get():
    """Should have header."""
    view = GNUTerryPratchett.as_view()
    request = RequestFactory().get('/')
    response = view(request)
    eq_(response['x-clacks-overhead'], 'GNU Terry Pratchett')


def test_cbv_post():
    """Should _not_ have header."""
    view = GNUTerryPratchett.as_view()
    request = RequestFactory().post('/')
    response = view(request)
    ok_('X-Clacks-Overhead' not in response)
