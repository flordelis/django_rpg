from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from rpg_base.models import Organization, Campaign


@login_required
def index(request, campaign_pk):
    campaign = get_object_or_404(Campaign, pk=campaign_pk)
    organizations = Organization.objects.filter(campaign=campaign)
    paginator = Paginator(organizations, 25)

    page = request.GET.get('page')

    try:
        organizations = paginator.page(page)
    except PageNotAnInteger:
        organizations = paginator.page(1)
    except EmptyPage:
        organizations = paginator.page(paginator.num_pages)

    context = {
        "objects": organizations,
        "campaign": campaign,
    }

    return render_to_response("organization/index.html", context)


@login_required
def view(request, organization_pk):
    organization = get_object_or_404(Organization, pk=organization_pk)

    context = {
        "organization": organization,
    }

    return render_to_response("organization/view.html", context)
