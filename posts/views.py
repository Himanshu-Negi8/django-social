from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.http import Http404
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from .models import Post, User
from .forms import PostForm
from django.contrib.auth import get_user_model
from group.models import Group,GroupMember
# Create your views here.


class PostListView(SelectRelatedMixin,ListView):
    model = Post
    select_related = ('user','group')

class PostDetailView(SelectRelatedMixin,DetailView):
    model = Post
    select_related = ('user','group')


class CreatePostView(LoginRequiredMixin,SelectRelatedMixin,CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        user = self.request.user
        group = self.object.group
        isMember = GroupMember.objects.get(group=group,user=user)
        if isMember:
            self.object.user = user
            self.object.save()
            return super().form_valid(form)
        else:
            return HttpResponseRedirect(reverse('group:all'))


class DeletePostView(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = Post
    select_related = ('user', 'group')
    success_url = 'group:single'

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        user = self.object.user
        group = self.object.group
        isMember = GroupMember.objects.get(group=group, user=user)
        if not isMember:
            return HttpResponseRedirect(reverse_lazy(self.success_url, kwargs={'slug': group.slug}))
        self.object.delete()
        return HttpResponseRedirect(reverse_lazy(self.success_url, kwargs={'slug': group.slug}))


class UserPost(ListView):
    model = Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))

        except User.DoesNotExist:
            raise Http404

        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context