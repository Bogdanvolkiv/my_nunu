pip install django
django-admin startproject recipe_site
cd recipe_site
python manage.py startapp recipes
Структура проекта
recipe_site/
│── recipe_site/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── recipes/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── recipe_detail.html
│   │   ├── recipe_form.html
│   │   ├── register.html
│   ├── static/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│── manage.py
Настройки проекта
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'recipes',  # Подключаем приложение
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
Модели
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    DIFFICULTY_LEVELS = [
        ('Easy', 'Легко'),
        ('Medium', 'Средне'),
        ('Hard', 'Сложно'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    steps = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="Время в минутах")
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS, default='Medium')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
Админка
from django.contrib import admin
from .models import Recipe, Category, Ingredient

admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Ingredient)
 Формы
from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'cooking_time', 'image', 'categories', 'ingredients', 'difficulty']
Представления
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm

def index(request):
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})
Маршруты
from django.urls import path
from .views import index, recipe_detail, add_recipe

urlpatterns = [
    path('', index, name='index'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('add/', add_recipe, name='add_recipe'),
]
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
Шаблоны
<!DOCTYPE html>
<html>
<head>
    <title>Сайт рецептов</title>
</head>
<body>
    <h1>Сайт рецептов</h1>
    <a href="{% url 'index' %}">Главная</a> | 
    <a href="{% url 'add_recipe' %}">Добавить рецепт</a>
    <hr>
    {% block content %}{% endblock %}
</body>
</html>
{% extends "base.html" %}
{% block content %}
<h2>Рецепты</h2>
<ul>
    {% for recipe in recipes %}
        <li><a href="{% url 'recipe_detail' recipe.id %}">{{ recipe.title }}</a></li>
    {% endfor %}
</ul>
{% endblock %}
{% extends "base.html" %}
{% block content %}
<h2>{{ recipe.title }}</h2>
<p><b>Описание:</b> {{ recipe.description }}</p>
<p><b>Ингредиенты:</b> {{ recipe.get_ingredients }}</p>
<p><b>Шаги:</b> {{ recipe.steps }}</p>
<p><b>Время приготовления:</b> {{ recipe.cooking_time }} минут</p>
{% endblock %}
{% extends "base.html" %}
{% block content %}
<h2>Добавить рецепт</h2>
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Сохранить</button>
</form>
{% endblock %}
Запуск проекта
python manage.py migrate
python manage.py createsuperuser  # создаем администратора
python manage.py runserver
