from django.http import HttpResponse

def green_home(request):
    return HttpResponse("<h1 style='color:green;'>This is GREEN app</h1>")
