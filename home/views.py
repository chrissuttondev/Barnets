from django.http import HttpResponse


# Create your views here.
def home(request):
    """view to display the home page"""
    return HttpResponse("Hello world")
