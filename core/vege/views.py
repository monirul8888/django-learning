from django.shortcuts import render, redirect
from .models import Recipe
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def recipe(request):
    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')
        desc = request.POST.get('desc')
        image = request.FILES.get('image')

        Recipe.objects.create(
            recipe_name=recipe_name,
            desc=desc,
            image=image
        )

        return redirect("/recipe/")
    recipes = Recipe.objects.all()
    return render(request, "recipe.html", {"recipes": recipes})

def delete_recipe(request, id):

    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect("/recipe/")

def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        recipe.recipe_name = request.POST.get('recipe_name')
        recipe.desc = request.POST.get('desc')

        if request.FILES.get('image'):
            recipe.image = request.FILES.get('image')

        recipe.save()
        return redirect("/recipe/")

    return render(request, "update_recipe.html", {"recipe": recipe})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/recipe/")

    return render(request, "login.html")


def log_out_page(request):
    logout(request)
    return redirect("/login")




def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return redirect("/register/")

        user=User.objects.create_user(
            username=username,
            
            first_name=name
        )

        user.set_password(password)
        user.save()


        return redirect("/login/")

    return render(request, "register.html")