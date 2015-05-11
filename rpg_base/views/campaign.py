from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rpg_base.models import Campaign


@login_required()
def index(request):
    campaigns = get_list_or_404(Campaign, user=request.user)

    context = {
        "campaigns": campaigns,
    }

    return render(request, "campaign/index.html", context)


@login_required
def view(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk, user=request.user)

    context = {
        "campaign": campaign,
    }

    return render(request, "campaign/view.html", context)
