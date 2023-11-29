# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from multiple.models import details_csv

# Create your views here.
def verification(request):
    if request.method == 'GET':
        verify_id = request.GET.get('verify_id')
        form = details_csv.objects.filter(verify_id=verify_id)
        context = {'form':form}
        return render(request, 'verification.html', context)
    return render(request, 'verification.html')