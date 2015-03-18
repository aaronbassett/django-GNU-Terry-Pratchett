#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.test import Client
import unittest


class TestClacks(unittest.TestCase):

    def test_xheader_exists(self):
        c = Client()
        response = c.get(reverse('test'))

        self.assertEqual(response["X-Clacks-Overhead"], "GNU Terry Pratchett")
