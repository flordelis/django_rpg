from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rpg_base.models import Character, Campaign


@login_required()
def index(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    characters = get_list_or_404(Character, campaign=pk)

    context = {
        "campaign": campaign,
        "characters": characters,
    }

    return render(request, "character/index.html", context)


@login_required
def view(request, pk, character_pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    character = get_object_or_404(Character, pk=character_pk, campaign=pk)

    context = {
        "campaign": campaign,
        "character": character,
    }

    return render(request, "character/view.html", context)
