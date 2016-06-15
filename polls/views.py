from django.shortcuts import render
# from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {'name': 'carl' }
    return render(request, 'polls/index.html', context);
    # template = loader.get_template('polls/index.html');
    # return HttpResponse(template.render({}, request));
    # return HttpResponse("Hello!");
