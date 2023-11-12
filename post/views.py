from django.shortcuts import render
from .models import Post

def blogs(request):
    content = Post.objects.all()
    return render(request=request, template_name='blogs.html', context={'content':content})
