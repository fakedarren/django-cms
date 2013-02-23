from django.shortcuts import render_to_response
from frontend.models import Page


def page(request, url):
    page = Page.objects.filter(url='/' + url)[0]
    return render_to_response('frontend/page.html', {'page': page})