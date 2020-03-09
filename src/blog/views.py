from django.shortcuts import render

# Create your views here.
from .models import Season_Blog
from .forms import RawSeasonPostForm


def season_post_create_view(request):
    form = RawSeasonPostForm()

    if request.method == "POST":
        form = RawSeasonPostForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            Season_Blog.objects.create(**form.cleaned_data)

    context = {
        "form" : form
    }
    return render(request, "blog/blogpost_create.html", context)


# def season_post_create_view(request):
#     if request.method == "POST":
#         name = request.POST.get('season_name')
#         print(name)

#     context = {}
#     return render(request, "blog/blogpost_create.html", context)


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