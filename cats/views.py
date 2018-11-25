from django.shortcuts import render,redirect
from django.urls import reverse
from cats.models import Cat
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth import login, logout
from .forms import CatCreateForm


# Create your views here.
def show_my_cats(request):
    context = {}
    try:
        cats = Cat.objects.filter(user=request.user)
        context['cats'] = cats
    except Cat.DoesNotExist:
        context['cats'] = None

    return render(request, 'cats/index.html', context)

def cat_create(request):
    if request.method == 'POST':
        form = CatCreateForm(request.POST)
        if form.is_valid():
            Cat = form.save()
            Cat.user = request.user
            Cat.save()

        return redirect('/')

    else:
        form = CatCreateForm
    return render(request, 'cats/create.html',
                  {'form': form})


def cat_edit(request, id):
    try:
        cat = Cat.objects.get(id=id)

        if request.method == "POST":
            cat.name = request.POST.get("name")
            cat.age = request.POST.get("age")
            cat.breed = request.POST.get("breed")
            cat.hair_color = request.POST.get("hair_color")
            cat.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "cats/altercat.html", {"cat": cat})
    except Cat.DoesNotExist:
        return HttpResponseNotFound("Cat not found")

def cat_delete(request, id):
    try:
        cat = Cat.objects.get(id=id)
        cat.delete()
        return HttpResponseRedirect("/")
    except Cat.DoesNotExist:
        return HttpResponseNotFound("Cat not found")


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/cats/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "cats/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "cats/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")