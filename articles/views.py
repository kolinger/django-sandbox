from django.shortcuts import render_to_response
from django.template.context import RequestContext

from articles.models import Article


def default(request):
    return render_to_response("articles.html", {
        "articles": Article.objects.all()
    }, context_instance=RequestContext(request))


def detail(request, slug):
    return render_to_response("article.html", {
        "article": Article.objects.get(slug=slug)
    }, context_instance=RequestContext(request))