from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Post, Comment, Like


def main_page(request):
    posts = Post.objects.all().order_by("-pk")  # select * from Post
    context = {
        "posts": posts
    }
    return render(request, "main_page.html", context=context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        try:
            comment = request.POST.get("comment_text")
            Comment.objects.create(post=post, comment=comment, user=request.user)
        except:
            try:
                like = Like.objects.get(user=request.user, post=post)
                like.delete()
            except:
                Like.objects.create(user=request.user, post=post)
            # if request.user in post.likes.all():
            #     post.likes.remove(request.user)
            # else:
            #     post.likes.add(request.user)

        return redirect(post.get_absolute_url())
    
    return render(request,
                  "post_detail.html",
                  locals())


def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        user = request.user
        post_obj = Post.objects.create(user=user,
            title=title, content=content)

        if len(request.FILES) != 0:
            image = request.FILES["image"]
            post_obj.image = image
            post_obj.save()
        return redirect("main-page")
    return render(request, "post_create.html")


def post_delete(request, pk):
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('main-page')
    return render(request, 'post_delete.html')


def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if len(request.FILES) != 0: 
            image = request.FILES["post_image"]
            post.image = image
        post.title = title
        post.content = content
        post.save()

        return redirect(post.get_absolute_url())
                # posts/post.id/   - post-detail
    return render(request, "post_update.html", locals())


def liked_users(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'liked_users.html', locals())


def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    if request.method == "POST":
        comment.delete()
        return redirect(post.get_absolute_url())
    return render(request, 'comment_delete.html', locals())