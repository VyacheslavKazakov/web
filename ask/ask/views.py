from django.http import HttpResponse, HttpResponseNotFound

def found(request):
    return HttpResponse("Found!")

def not_found(request):
    return HttpResponseNotFound("Not Found!")
