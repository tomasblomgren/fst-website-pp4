from . import views
from django.urls import path
from .views import UpdateView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.Postlike.as_view(), name='post_like'),
    path('edit/<slug:slug>', views.PostEditView.as_view(), name='edit_post'),

]
