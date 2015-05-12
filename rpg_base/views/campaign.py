from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from rpg_base.models import Campaign


@login_required()
def index(request):
    campaigns = get_list_or_404(Campaign, user=request.user)
    paginator = Paginator(campaigns, 25)

    page = request.GET.get('page')

    try:
        campaigns = paginator.page(page)
    except PageNotAnInteger:
        campaigns = paginator.page(1)
    except EmptyPage:
        campaigns = paginator.page(paginator.num_pages)

    context = {
        "page": page,
        "campaigns": campaigns,
    }

    return render_to_response("campaign/index.html", context)


@login_required
def view(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk, user=request.user)

    context = {
        "campaign": campaign,
    }

    return render_to_response("campaign/view.html", context)
