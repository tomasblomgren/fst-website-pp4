from . import views
from django.urls import path
from .views import UpdateView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.Postlike.as_view(), name='post_like'),
    path('edit/<slug:slug>', views.EditPost.as_view(), name='edit_post'),
    path('pk/update', views.EditPost.as_view(), name='edit_post'),

]
