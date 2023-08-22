from django.shortcuts import render, redirect
from . import models
from . import forms
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import django_tables2 as tables
from django_tables2 import SingleTableView
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from django_tables2 import TemplateColumn

# Create your views here.

class PendaftarTable(tables.Table):
    actions = TemplateColumn(template_code='<div class="" style="display: flex; justify-content: center;"><button id="{{ record.id }}" class="user_delete btn badge mr-1" style="color:red;"><i class="bi bi-trash"></i></button></div>')
    wa_number = TemplateColumn(template_code='<a href="https://wa.me/62{{record.wa_number}}" target="blank">{{record.wa_number}}</a>')
    class Meta:
        model = models.UserItfess
        template_name = "django_tables2/bootstrap.html"
        fields = ("nama","utusan","email","wa_number","password")

class MemberTable(tables.Table):
    actions = TemplateColumn(template_code='<div class="" style="display: flex; justify-content: center;"><button id="{{ record.id }}" class="member_delete btn badge mr-1" style="color:red;"><i class="bi bi-trash"></i></button></div>')

    class Meta:
        model = models.Member
        template_name = "django_tables2/bootstrap.html"
        fields = ("nama","email")

class Member2Table(tables.Table):
    user = tables.Column(verbose_name= 'Nama Ketua', accessor='user.nama')
    nama = tables.Column(verbose_name= 'Nama Member')
    class Meta:
        model = models.Member
        template_name = "django_tables2/bootstrap.html"
        fields = ("user", "nama","email")

class memberCreateView(BSModalCreateView):
    template_name = 'home/modal_member.html'
    form_class = forms.memberForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('index')
    def get_initial(self):
        super(memberCreateView, self).get_initial()
        print("self.request.user")
        return {"user": 1}


def sign_up(request):
    if request.method == 'GET':
        form = forms.UsersForm()
        return render(request, 'home/register.html', {'form': form})    
    elif request.method == 'POST':
        form = forms.UsersForm(request.POST)
        
        if form.is_valid():
            user = models.UserItfess()
            user.nama = form.cleaned_data['nama']
            user.utusan = form.cleaned_data['utusan']
            user.wa_number = form.cleaned_data['wa_number']
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['email']
            #user.password = form.cleaned_data['password1']
            #user = form.save(commit=False)
            user.set_password(form.cleaned_data.get("password1"))
            user.save()
            authenticated_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            print(authenticated_user)
            login(request, authenticated_user)
            return redirect('/')
#            return render(request,'home/',{'form': form})
        else:        
            return render(request,'home/register.html',{'form': form})
   
def sign_in(request):
    if request.method == 'GET':
        form = forms.LoginForm()
        return render(request, 'home/login.html', {'form': form})    
    elif request.method == 'POST':
        form = forms.LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('/')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'home/login.html',{'form': form})

def sign_out(request):
    if request.method == 'GET':
        logout(request)
        return redirect('/')


def admin(request):
    return render(request,'home/index_admin.html')

def dokumen(request):
    return render(request,'home/index_admin.html')

def manage(request):
    table = MemberTable(Member.objects.all().filter(user=request.user))

    return render(request,'home/index_manage.html',{'table':table})

def manage2(request):
    table = Member2Table(Member.objects.all())
    return render(request,'home/index_manage2.html',{'table':table})

def data_upload(request):
    return render(request,'home/index_upload.html')

#@login_required
class userListView(SingleTableView, LoginRequiredMixin, generic.ListView):
    model = models.UserItfess
    form_class = forms.userItFessForm
    model = models.UserItfess
    table_class = PendaftarTable
    login_url = "/user/login/"
    redirect_field_name = "redirect_to"

class userDetailView(generic.DetailView):
    model = models.UserItfess
    form_class = forms.userItFessForm

class memberListView(generic.ListView):
    model = models.Member
    form_class = forms.memberForm


class memberCreateView(generic.CreateView):
    model = models.Member
    form_class = forms.memberForm


class memberDetailView(generic.DetailView):
    model = models.Member
    form_class = forms.memberForm


class memberUpdateView(generic.UpdateView):
    model = models.Member
    form_class = forms.memberForm
    pk_url_kwarg = "pk"


class memberDeleteView(generic.DeleteView):
    model = models.Member
    success_url = reverse_lazy("azka_member_list")