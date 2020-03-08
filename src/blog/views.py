from django.shortcuts import render

from .forms import BlogpostForm

# Create your views here.
from .models import Blog



def blogpost_create_view(request):
    form = BlogpostForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogpostForm()
   
    context = {
        'form' : form
    }

    print(request)
    return render(request, "blog/blogpost_create.html", context)

def blog_desc_view(request):
    obj = Blog.objects.get(id=1)
    # context = {
    #     'title' : obj.title,
    #     'desc' : obj.desc
    # }
    context = {
        'object' : obj
    }
    return render(request, "blog/description.html", context)