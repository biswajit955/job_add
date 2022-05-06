from django.urls import path
from .views import (
    PostListView,
    PostDetailview,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CompanyCreateView,
    CompanyListView,
    CompanyUpdateView,
    CompanyDeleteView,
    about,
    base,
    
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('base/', base, name='base'),
    path('post/<int:pk>/', PostDetailview.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/create', PostCreateView.as_view(), name='post-create'),
    path('company/company_create', CompanyCreateView.as_view(), name='company-create'),
    path('company', CompanyListView.as_view(), name='company'),
    path('company/<int:pk>/update', CompanyUpdateView.as_view(), name='company-update'),
    path('company/<int:pk>/delete', CompanyDeleteView.as_view(), name='company-delete'),
    path('about/', about, name='about'),
]