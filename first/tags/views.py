from django.shortcuts import render, redirect
from .models import Tag


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, "tag_list.html", locals())


def tag_detail(request, pk):
    tag = Tag.objects.get(pk=pk)
    return render(request, "tag_detail.html", locals())


def tag_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        print(title)
        tag = Tag.objects.create(title = title)
        return redirect(tag.get_absolute_url())

    return render(request, "tag_create.html")