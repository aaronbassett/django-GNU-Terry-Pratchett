#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.test import RequestFactory

from nose.tools import eq_

from gnu_terry_pratchett.decorators import clacks_overhead


@clacks_overhead
def view(request):
    return HttpResponse("Death can't have him")


def test_view_decorator():
    request = RequestFactory().get('/')
    response = view(request)
    eq_(response['x-clacks-overhead'], 'GNU Terry Pratchett')

