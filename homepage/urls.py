
  
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
app_name = "homepage"
urlpatterns = [
    path("index", views.index, name="index"),
    path('post/new/', PostCreateView.as_view(), name='new_post'),
    
    path('', PostListView.as_view(), name='instagram-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('<int:pk>',views.like, name='like'),
]