from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm


# Create your views here.
def home(request):
    all_posts = Post.objects.filter(status='published')
    return render(request, 'home.html', {'posts': all_posts})

def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')

    return render(request, 'single.html', {'post': post})


def feed(request):
    posts = Post.objects.order_by('-published_date')  # Retrieve posts ordered by timestamp
    return render(request, 'feed.html', {'posts': posts})

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return redirect('feed')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/feed')  # Redirect to the feed page after successful form submission
    else:
        form = PostForm(initial={'author': request.user})
    
    return render(request, 'create_post.html', {'form': form})

