from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from rpg_base.models import Encounter, Campaign


@login_required
def index(request, campaign_pk):
    campaign = get_object_or_404(Campaign, pk=campaign_pk, user=request.user)
    if "search" in request.GET:
        search_value = request.GET["search"]
        encounters = get_list_or_404(Encounter, campaign=campaign_pk, name__contains=request.GET["search"])
    else:
        search_value = ""
        encounters = get_list_or_404(Encounter, campaign=campaign_pk)

    paginator = Paginator(encounters, 25)


    page = request.GET.get('page')

    try:
        encounters = paginator.page(page)
    except PageNotAnInteger:
        encounters = paginator.page(1)
    except EmptyPage:
        encounters = paginator.page(paginator.num_pages)



    context = {
        "campaign": campaign,
        "encounters": encounters,
        "search_value": search_value,
    }

    return render_to_response("encounter/index.html", context)


@login_required
def view(request, campaign_pk, encounter_pk):
    encounter = get_object_or_404(Encounter, pk=encounter_pk, campaign=campaign_pk)

    context = {
        "encounter": encounter,
    }

    return render_to_response("encounter/view.html", context)
