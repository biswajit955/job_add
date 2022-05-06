from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post ,Company
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,

)


def base(request):
    post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'job/base.html', context)

# Create your views here.



def about(request):
    return render(request, 'job/about.html')


class PostListView(ListView):
    model = Post
    template_name = 'job/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4
    paginate_orphans = 1
    ordering = ['-date_posted']

class CompanyListView(ListView):
    model = Company
    template_name = 'job/company.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'companys'
    paginate_by = 4
    paginate_orphans = 1
    ordering = ['-date_posted']


class PostDetailview(DetailView):
    model = Post
    template_name = 'job/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'job/post_create.html'
    fields = ['title', 'Location','date_posted','job_function','key_skills','vacancies','job_description','experience','salary','educational_qualification']
    success_url = '/'

    def form_valid(self, form,*argv, **kwargs):
        form.instance.author = self.request.user
        users = self.request.user
        com = Company.objects.filter(user=users).values('company_name').first()
        company_name = com["company_name"]
        form.instance.company = company_name
        return super().form_valid(form)

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = 'job/company_create.html'
    fields = ['company_name', 'logo','address']
    success_url = 'company'

    def form_valid(self, form,*argv, **kwargs):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = Post
    template_name = 'job/post_create.html'
    fields = ['title', 'Location','date_posted','job_function','key_skills','vacancies','job_description','experience','salary','educational_qualification']

    # after post request url
    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("post-detail", kwargs={"pk": pk})

    def form_valid(self, form):
        form.instance.author == self.request.user
    # ------------------------------------
        print(form.instance.author)
        print(self.request.user)
    # ------------------------------------
        messages.info(self.request, f"Your post updated")
        return super().form_valid(form)

    def test_func(self):
        Post = self.get_object()
        if self.request.user == Post.author:
            return True
        return False

class CompanyUpdateView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = Company
    template_name = 'job/company_create.html'
    fields = ['company_name', 'logo','address']

    # after post request url
    def get_success_url(self):
        return reverse("company")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.info(self.request, f"Your post updated")
        return super().form_valid(form)

    def test_func(self):
        Post = self.get_object()
        if self.request.user == Post.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'job/post_delete.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        Post = self.get_object()
        if self.request.user == Company.user:
            return True
        return False

class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    template_name = 'job/company_delete.html'
    success_url = 'company'

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(CompanyDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        Post = self.get_object()
        if self.request.user == Post.author:
            return True
        return False
