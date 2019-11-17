from django.views.generic import TemplateView, CreateView, DetailView
from  django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Product, Category,BaiViet

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

class AboutView(TemplateView):
    template_name = "aboutus.html"

    def get_context_data(self, **kwargs):
        context = dict()
        baiviets = BaiViet.objects.all()
        context['baiviets'] = baiviets
        return context


def noidung_baiviet(request, pk):
    baiviet = BaiViet.objects.get(pk=pk)
    # print(binhluans)
    context = {
        'baiviet': baiviet,
        'baiviet_id':pk
        }
    return render(request, 'post.html', context)

class Contact(TemplateView):
    template_name = "contact.html"

cart = {}
def addcart(request):
    if request.is_ajax():
        cart_id = request.POST.get('cart_id')
        num = request.POST.get('num')
        proDetail = Product.objects.get(pk = id)
        if id in cart.keys():
            itemCart = {
                'name':proDetail.title,
                'price':proDetail.price,
                'image': str(proDetail.product_img),
                'num': int(cart['cart_id']['num']) +1
            }
        else:
            itemCart = {
                'name': proDetail.title,
                'price': proDetail.price,
                'image': str(proDetail.product_img),
                'num': int(cart['cart_id']['num'])
            }
        cart['cart_id'] = itemCart
        request.session['cart'] = cart
        cartInfo = request.session['cart']
    return render(request,'addcart.html',{'cart':cartInfo })