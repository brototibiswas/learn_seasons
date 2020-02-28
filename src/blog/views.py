from django.shortcuts import render

# Create your views here.
from .models import Blog
def blog_season_detail_view(request):
    obj = Blog.objects.get(id=1)
    context = {
        'title' : obj.title,
        'desc' : obj.desc
    }
    return render(request, "blog/seasons.html", context)