from django.shortcuts import render_to_response
from frontend.models import Page, Module


def page(request, url):
    menu = Page.objects.order_by('order')
    page = Page.objects.get(url='/' + url)

    module_main = Module.objects.filter(page=page).get(name='Main')

    return render_to_response('frontend/' + page.template + '.html', {
    	'current_url': '/' + url,
        'menu': menu,
        'page': page,
        'module_main': module_main
    })