from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import districts
# Create your views here.
#def index(request):
    #return HttpResponse("Hello world. you are at the polls index")

class HomePageView(TemplateView):
    template_name= 'index.html'

def district_datasets(request):    #no use!!!!
    Districts = serialize('geojson', districts.objects.all())
    return HttpResponse(districts,content_type='json')
    