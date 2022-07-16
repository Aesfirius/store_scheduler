from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from shop_scheduler import queries as q
from shop_scheduler import helpers as h


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            q.create_user(username, password)
            user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('home')


def user_logout(request):
    logout(request)
    return redirect('home')


class HomeView(LoginRequiredMixin, View):
    """
    """
    login_url = '/login/'

    def get(self, request):
        """
        Вернуть все товары взятые из базы по:
        - user.group in products.groups
        и
        группировать данные по:
        - группа
            - запланированная дата покупки
                - локация продукта
                    - продукты
        """
        user_id = request.user.username
        q_product_data = q.get_products_by_user_id(user_id)
        user_product_data = h.combine_user_data(q_product_data, me=user_id)

        return render(request, 'home.html', {'user_data': user_product_data})

    def post(self, request):
        return render(request, 'home.html')


class SettingsView(LoginRequiredMixin, View):

    def get(self, request):

        return render(request, 'settings.html')


class ShareView(LoginRequiredMixin, View):

    def get(self, request):

        return render(request, 'share.html')

    def post(self, request):
        if 'add' in request.path:
            product = q.get_product(request.POST['product_id'])
            q.add_group_for(product, request.POST['share_add'])
            return redirect('home')
        elif 'del' in request.path:

            return redirect('home')
        else:
            return render(request, 'share.html', {'product_id': request.POST['product_id']})
