from articles.models import Tag


def global_variables(request):
    return {
        "tags": Tag.objects.all(),
    }
