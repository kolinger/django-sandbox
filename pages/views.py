from django.shortcuts import render_to_response

from pages.models import Page


def default(request):
    return render_to_response("default.html", {
        "pages": Page.objects.all()
    })


def detail(request, slug):
    return render_to_response("detail.html", {
        "page": Page.objects.get(slug=slug)
    })