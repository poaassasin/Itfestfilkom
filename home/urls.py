"""itfest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from . import api
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("member", api.memberViewSet)
router.register("Users", api.UsersViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path("user/", views.userListView.as_view(), name="user_list"),
    path("member/", views.memberListView.as_view(), name="member_list"),
    path("manage/", views.manage, name="member_list"),
    path("manage2/", views.manage2, name="member_list"),
    path("dokumen/", views.dokumen, name="member_list"),
    path("admin/", views.admin, name="member_list"),
    path("modal_member/", views.memberCreateView.as_view(), name="adm_lelang_modal_obyek_seleksi"),
    path("data_upload/", views.data_upload, name="member_list"),
    path("member/create/", views.memberCreateView.as_view(), name="member_create"),
    path("member/detail/<int:pk>/", views.memberDetailView.as_view(), name="member_detail"),
    path("member/update/<int:pk>/", views.memberUpdateView.as_view(), name="member_update"),
    path("member/delete/<int:pk>/", views.memberDeleteView.as_view(), name="member_delete"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='commons/password_reset.html',
             subject_template_name='commons/password_reset_subject.txt',
             email_template_name='commons/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='commons/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='commons/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='commons/password_reset_complete.html'
         ),
         name='password_reset_complete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
