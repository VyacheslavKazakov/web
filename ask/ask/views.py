from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_GET

@require_GET
def found(request):
    return HttpResponse("Found!")

@require_GET
def not_found(request):
    return HttpResponseNotFound("Not Found!")
