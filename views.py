from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.models import User

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('priority')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    print('entra en la vista')
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=pk,created_date__lte=timezone.now()).order_by('created_date')
    print(comments)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return render(request, 'comment/comment_detail.html', {'comments': comments})

def comment_new(request, pk):
    print('entra en la vista')
    if request.method == "POST":
        form = CommentForm(request.POST)
        print('ha entrado en el post')
        if form.is_valid():
            print('form is valid')
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.author = request.user
            comment.created_date = timezone.now()
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            print('comentario creado')
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'comment/comment_edit.html', {'form': form})

def comment_edit(request, pk):
    post = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=post)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published_date = timezone.now()
            comment.save()
            return redirect('comment_detail', pk=post.pk)
    else:
        form = CommentForm(instance=post)
    return render(request, 'comment/comment_edit.html', {'form': form})