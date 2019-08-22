from django.shortcuts import render
from .models import ServicesData

# Create your views here.
def home2_view(request):
    return render(request, 'durgasoft_home.html')


def services_view(request):
    services=ServicesData.objects.all()
    return render(request, 'durgasoft_services.html',{'services':services})



def contact_view(request):
    return render(request, 'durgasoft_contact.html')


def gallery_view(request):
    return render(request, 'durgasoft_gallery.html')


def feddback_view(request):
    return render(request, 'durgasoft_feedback.html')
