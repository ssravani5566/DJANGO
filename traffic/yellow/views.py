from django.http import HttpResponse

def yellow_home(request):
    return HttpResponse("<h1 style='color:orange;'>This is YELLOW app</h1>")
