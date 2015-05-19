from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from rpg_base.models import Campaign


@login_required
def index(request):
    print request.GET
    if "search" in request.GET:
        search_value = request.GET["search"]
        campaigns = get_list_or_404(Campaign, user=request.user, name__contains=request.GET["search"])
    else:
        search_value = ""
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
        "objects": campaigns,
        "search_value": search_value,
    }

    return render_to_response("campaign/index.html", context)


@login_required
def view(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk, user=request.user)

    context = {
        "campaign": campaign,
    }

    return render_to_response("campaign/view.html", context)
