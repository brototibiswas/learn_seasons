from django.shortcuts import render

# Create your views here.
from .models import Blog
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