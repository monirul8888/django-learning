from django.shortcuts import render, redirect
from .models import Recipe
from django.shortcuts import get_object_or_404

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
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")