from django.shortcuts import render, redirect
from .models import Recipe


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
