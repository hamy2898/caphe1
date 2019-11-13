from django.views.generic import TemplateView, CreateView, DetailView
from  django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Product, Category

from django.contrib.auth import authenticate,login
from django.views import View

from django.http import HttpResponseRedirect

#View đăng ký người dùng
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

#View đăng ký người dùng thành công
class SignUpDoneView(TemplateView):
    template_name = 'registration/signup_done.html'
    title = 'Signup successful'

#View hiển thị trang chủ (index.html)
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        product = Product.objects.all()[:6]
        context = {
            'categorys': categories,
            'products' : product,
        }
        return context

class Product1(TemplateView):
    template_name = "shop.html"

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        product = Product.objects.all()
        context = {
            'categorys1': categories,
            'products1': product,
        }
        return context



def detail(request, pk):
    detail = Product.objects.get(pk=pk)
    context = {
        'detail': detail,
        'id': pk,
        }
    return render(request, 'product_detail.html', context)