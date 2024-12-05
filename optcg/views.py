from django.http import HttpResponse


def index(request):
    return HttpResponse("THE ONE PIECE IS REAL!!!!!")