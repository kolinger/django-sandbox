from django.shortcuts import render_to_response
from django.template.context import RequestContext

from pages.models import Page


def default(request):
    return render_to_response("pages.html", {
        "pages": Page.objects.all()
    }, context_instance=RequestContext(request))


def detail(request, slug):
    return render_to_response("page.html", {
        "page": Page.objects.get(slug=slug)
    }, context_instance=RequestContext(request))