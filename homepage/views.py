from django.views.generic import CreateView
from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required 
# Create your views here.
#home view

def index(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'home/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'home/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'gallery/post_detail.html'
    context_object_name = 'post'
    

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    view class to create post
    """
    model = Post
    fields = "__all__"
    template_name = 'gallery/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def post(request, pk):
    """
    View to handle post model
    Args:
    Pk - Primary Key,an unique way to identify an object uniquely in relational database systems
    """
    post = Post.objects.get(pk=pk)
    user = request.user
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(author= user,description=form.cleaned_data["description"],post=post)
            comment.save()

    comments = Comment.objects.filter(post=post).order_by('-date_posted')
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return self.get(self, request, pk, context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'image', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'gallery/post_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

@login_required
def like(request,pk):
    post = Post.objects.get(pk=pk)
    post.likes+=1
    post.save()
    return redirect('homepage:index')

