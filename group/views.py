from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

# Create your views here.
from django.views.generic import CreateView, DetailView, ListView, RedirectView

from .models import Group, GroupMember


class CreateGroup(CreateView,LoginRequiredMixin):
    model = Group
    fields = ['name','description']

class SingleGroup(DetailView):
    model = Group

class ListGroup(ListView):
    model = Group
    paginate_by = 1

class JoinView(LoginRequiredMixin,RedirectView):
    login_url = 'account:login'
    def get_redirect_url(self, *args, **kwargs):
        return reverse('group:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,*args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except:
            print("already joined")
        else:
            pass
        return super().get(self.request,*args,**kwargs)

class LeaveView(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('group:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        try:
            membership = GroupMember.objects.filter(user = self.request.user,group__slug = self.kwargs.get('slug'))
        except GroupMember.DoesNotExist:
            print("Such a relation does not exist")
        else:
            membership.delete()
        return super().get(self,request,*args,**kwargs)