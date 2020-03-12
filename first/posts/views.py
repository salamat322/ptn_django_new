from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Post, Comment, Like, LikeComment
from tags.models import Tag



def default_page(request):
    return render(request, 'default_page.html')


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
            if 'like' in request.POST:
                try:
                    like = Like.objects.get(user=request.user, post=post)
                    like.delete()
                except:
                    Like.objects.create(user=request.user, post=post)
                # if request.user in post.likes.all():
                #     post.likes.remove(request.user)
                # else:
                #     post.likes.add(request.user)
            elif 'like-comment' in request.POST:
                id = int(request.POST.get('like-comment'))
                comment = Comment.objects.get(pk=id)
                try:
                    like = LikeComment.objects.get(user=request.user, comment=comment)
                    like.delete()
                except:
                    LikeComment.objects.create(user=request.user, comment=comment)
        return redirect(post.get_absolute_url())
    
    return render(request,
                  "post_detail.html",
                  locals())


def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        tag_title = request.POST.get('tag_title')
        a = False
        for i in title:
            if i != ' ':
                a = False
                break
            else:
                a = True
        if a or len(title) == 0:
            return render(request, "post_create.html", locals())
        content = request.POST.get("content")
        user = request.user

        post_obj = Post.objects.create(user=user,
            title=title, content=content)
        if len(tag_title) != 0:
            try:
                tag = Tag.objects.get(title=tag_title)
                tag.post.add(post_obj)
            except:
                tag_obj = Tag.objects.create(title=tag_title)
                tag_obj.post.add(post_obj)
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
        a = False
        for i in title:
            if i != ' ':
                a = False
                break
            else:
                a = True
        if a or len(title) == 0:
            return render(request, "post_update.html", locals())
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

def update_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    if request.method == 'POST':
        commit = request.POST.get('commit')
        comment.comment = commit
        comment.save() 
        return redirect(post.get_absolute_url())
    return render(request, 'comment_update.html', locals())