from django.urls import path
from . import views

app_name = 'group'

urlpatterns = [

    path('',views.ListGroup.as_view(),name='all'),
    path('new/',views.CreateGroup.as_view(),name='create'),
    path('groupdetail/<slug:slug>',views.SingleGroup.as_view(),name='single'),
    path('join/<slug:slug>',views.JoinView.as_view(),name='join'),
    path('leave/<slug:slug>',views.LeaveView.as_view(),name='leave'),

]