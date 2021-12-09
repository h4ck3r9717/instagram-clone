from django.urls import path
from . import views
app_name = "profileApp"
urlpatterns = [
       path('profile/', views.profile, name='profile'),
       
       path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
       path('follow/<to_follow>', views.follow, name='follow'),
       path('search/', views.search_profile, name='search'),
       path("all_profiles/",views.all_profiles, name="all_profiles"),
       path('user_profile/<username>/', views.user_profile, name='user_profile'),
]