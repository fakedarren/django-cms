from django.shortcuts import render_to_response
from frontend.models import Page


def page(request, url):
    menu = Page.objects.order_by('order')
    page = Page.objects.get(url='/' + url)
    return render_to_response('frontend/page.html', {
        'menu': menu,
        'page': page
    })