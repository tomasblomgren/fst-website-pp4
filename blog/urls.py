from . import views
from django.urls import path
from .views import UpdateView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.Postlike.as_view(), name='post_like'),
    path('<pk>/edit', views.PostEditView.as_view(), name='edit_post'),
    path('<pk>/Delete/', views.EditSuccess.as_view(), name='delete_confirm'),
    path('<pk>/SuccessDeletingView/', views.SuccessDeletingView.as_view(), name='success_delete'),
    path('<pk>/SuccessEditingView/', views.SuccessEditingView.as_view(), name='success_save'),
]
