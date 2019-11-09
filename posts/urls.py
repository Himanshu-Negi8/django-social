from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [

        path('',views.PostListView.as_view(),name='post'),
        path('<slug:slug>/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
        path('createpost/',views.CreatePostView.as_view(),name='createPost'),
        path('delete/<int:pk>/',views.DeletePostView.as_view(),name='delete'),
        path('by/<slug:username>/',views.UserPost.as_view(),name='for_user')
]