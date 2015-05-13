from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from rpg_base.models import Location, Campaign


@login_required()
def index(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    locations = get_list_or_404(Location, campaign=pk)
    paginator = Paginator(locations, 25)

    page = request.GET.get('page')

    try:
        locations = paginator.page(page)
    except PageNotAnInteger:
        locations = paginator.page(1)
    except EmptyPage:
        locations = paginator.page(paginator.num_pages)

    context = {
        "locations": locations,
        "campaign": campaign,
    }

    return render_to_response("location/index.html", context)


@login_required
def view(request, pk, location_pk):
    location = get_object_or_404(Location, pk=location_pk, campaign=pk)

    context = {
        "location": location,
    }

    return render_to_response("location/view.html", context)
