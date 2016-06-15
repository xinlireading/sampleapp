from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    template_name = "uploadimage/index.html"
    # return HttpResponse("Hello Upload Image Demo")
    return render(request, template_name, None)
