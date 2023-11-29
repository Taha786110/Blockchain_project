# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from multiple.models import details_csv,civil_details,comp_details,mech_details,elec_details
from home.models import details
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='http://127.0.0.1:8000/')
def fetch(request):
    username = request.user.username
    if username == 'BIT':
        form = list(civil_details.objects.all())+list(comp_details.objects.all())+list(mech_details.objects.all())+list(elec_details.objects.all())
        context = {'form':form}
        return render(request, 'reg.html', context)
    elif username == 'comp':
        form = comp_details.objects.all()
        context = {'form':form}
        return render(request, 'reg.html', context)
    elif username == 'civil':
        form = civil_details.objects.all()
        context = {'form':form}
        return render(request, 'reg.html', context)
    elif username == 'mech':
        form = mech_details.objects.all()
        context = {'form':form}
        return render(request, 'reg.html', context)
    elif username == 'elec':
        form = elec_details.objects.all()
        context = {'form':form}
        return render(request, 'reg.html', context)
    else:
        data = None
    