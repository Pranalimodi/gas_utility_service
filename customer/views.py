# customer/views.py

from django.shortcuts import render, redirect
from .forms import ServiceRequestForm

def request_service(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('request_list')  # Redirect to the list of requests after submission
    else:
        form = ServiceRequestForm()
    return render(request, 'customer/request_form.html', {'form': form})

# customer/views.py

from .models import ServiceRequest

def request_list(request):
    requests = ServiceRequest.objects.all()  # For now, show all requests
    return render(request, 'customer/request_list.html', {'requests': requests})

def home(request):
    return render(request, 'customer/home.html')
