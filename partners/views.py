from django.shortcuts import render
from .models import Partner
from django.forms import modelformset_factory
# Create your views here.

def partner_form(request):
    # partner = Partner.objects.get(pk=request.user.id)
    formset = modelformset_factory(Partner, exclude=[])
    return render(request, 'partner/partner_form.html', {'form': formset})

def diaper_request(request):
    # partner = Partner.objects.get(pk=request.user.id)
    formset = modelformset_factory(Partner, exclude=[])
    return render(request, 'partner/diaper_request.html', {'form': formset})