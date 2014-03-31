from articles.models import Tag


def global_variables(request):
    print("lol")
    return {
        "tags": Tag.objects.all(),
    }