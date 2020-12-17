from django.shortcuts import render

# Create your views here.


def lista_post(request):
    return render(request, "Lista_post.html")


def post_singular(request):
    return render(request, "post_singular.html")
