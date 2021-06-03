from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from .models import Comment

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('priority')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

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

def comment_list(request):
    comments = Comment.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/comment_list.html', {'comments':comments})

def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return render(request, 'blog/comment_detail.html', {'comments': comments})

def comment_new(request):
    if request.method == "COMMENT":
        form = CommentForm(request.COMMENT)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published_date = timezone.now()
            comment.save()
            return redirect('commnet_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Comment, pk=pk)
    if request.method == "COMMENT":
        form = CommentForm(request.COMMENT, instance=post)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published_date = timezone.now()
            comment.save()
            return redirect('comment_detail', pk=post.pk)
    else:
        form = CommentForm(instance=post)
    return render(request, 'blog/comment_edit.html', {'form': form})