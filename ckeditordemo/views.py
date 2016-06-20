from django.shortcuts import render, get_object_or_404
from ckeditordemo.forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    template_name = "ckeditordemo/index.html"
    form = PostForm()
    return render(request, template_name, { 'form': form })

def detail(request, post_id):
    print(post_id)
    post = get_object_or_404(Post, pk=post_id)
    print(post.content)
    return render(request, 'ckeditordemo/detail.html', {'post': post})
