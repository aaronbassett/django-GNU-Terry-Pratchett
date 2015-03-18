from django.conf.urls import patterns, url
from django.http import HttpResponse


def test_view(self):
    return HttpResponse("Hello")


urlpatterns = patterns(
    '',
    url(r'^$', test_view, name='test'),
)
