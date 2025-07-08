from django.http import HttpResponse

def red_home(request):
    return HttpResponse("<h1 style='color:red;'>This is RED app</h1>")
