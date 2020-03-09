from django.shortcuts import render

# Create your views here.
from .models import Season_Blog
from .forms import BlogpostForm

def season_post_create_view(request):
    if request.method == "POST":
        name = request.POST.get('season_name')
        print(name)

    context = {}
    return render(request, "blog/blogpost_create.html", context)


def blog_desc_view(request):
    obj = Season_Blog.objects.get(id=1)
    # context = {
    #     'title' : obj.title,
    #     'desc' : obj.desc
    # }
    context = {
        'object' : obj
    }
    return render(request, "blog/description.html", context)