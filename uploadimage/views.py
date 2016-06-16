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
        # print(request.FILES)
        # print(request.POST.get('file'))
        # return;
        # file = request.FILES.get('file')
        print(file.name)
        print(file.charset)
        print(file.content_type)
        print(file.size)
        print(file.content_type_extra)
        # print(file.temporary_file_path())
        # return HttpResponse('POST')
        filename = file.name

        path = default_storage.save('{}/{}'.format('avatar',filename), ContentFile(file.read()))
        # tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        return HttpResponse('POST')

    else:
        print('get')
        return HttpResponse('GET')
