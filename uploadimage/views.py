from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os

# Create your views here.
def index(request):
    template_name = "uploadimage/index.html"
    # return HttpResponse("Hello Upload Image Demo")
    return render(request, template_name, None)

def upload(request):
    if request.method == 'POST':
        username = request.POST['username']
        file = request.FILES['file']
        filename = file.name
        path = default_storage.save('{}/{}'.format('avatar',filename), ContentFile(file.read()))
        # tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        return HttpResponse('POST1')

    else:
        return HttpResponse('GET')
