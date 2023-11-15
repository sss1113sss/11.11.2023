from django.shortcuts import render
from .models import Post

def blogs(request):
    content = [
               {'name':'messi wooon','date':'13.11.2023','text':'jijadijajdijaijdijawd','image':'messi.avif'}
               {'name':'messi wn','date':'13.11.2023','text':'jijadijajdijaijdijawd','image':'messi.avif'}
               {'name':'messi win','date':'13.11.2023','text':'jijadijajdijaijdijawd','image':'messi.avif'}
               ]
    return render(request=request, template_name='blogs.html', context={'content':content})
