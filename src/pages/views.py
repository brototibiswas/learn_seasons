from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # custom dictionary -> {}
    context = {
        # key : value
        "seasons" : ["Summer","Winter","Fall","Spring"]
    }
    return render(request, 'home.html',context)