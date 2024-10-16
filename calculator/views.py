from django.shortcuts import render, get_object_or_404

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipe_view(request, recipe_name):
    recipe = get_object_or_404(DATA, recipe_name)
    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
        if servings <= 0:
            raise ValueError("Количество порций должно быть положительным числом.")
    except ValueError:
        return render(request, 'calculator/index.html', {
            'error': "Параметр servings должен быть целым положительным числом."
        })

    adjusted_recipe = {ingredient: quantity * servings for ingredient, quantity in recipe.items()}
    context = {
        'recipe': adjusted_recipe
    }

    return render(request, 'calculator/index.html', context)