from itertools import chain
from django.shortcuts import render, redirect
from .models import ImageSpot, Barangay
from .forms import ImageForm

from django.conf import settings
from django.core.files.storage import FileSystemStorage

def index(request):
  saved = False

  if request.method == "POST":
    #Get the posted form
    NewImageForm = ImageForm(request.POST, request.FILES)

    if NewImageForm.is_valid():
      feature = []
      feature = NewImageForm.cleaned_data["layer_name"].rsplit('/',1)
      feature = feature[1]
      feature = feature.split(':')
      sorted_files = sorted(request.FILES.getlist('image'), key=lambda x: x.name)
      sorted_geodata = sorted(request.POST.getlist('geodata'))

      for index, images in enumerate(sorted_files):
        image = ImageSpot()
        image.establishment_type = feature[1]
        temppicture_ycoordinate, xcoordinate = sorted_geodata[index].split(':')
        xcoordinate, temppicture_ycoordinate = xcoordinate.split(',')
        image.image = images
        image.geom = {'type': 'Point', 'coordinates': [float(xcoordinate), float(temppicture_ycoordinate)]}
        image.save()
        saved = True
      return render(request, 'photomap/index.html', {'qs_results': qs_results})

  else:
    qs_results = ImageSpot.objects.all()
    barangay_results = Barangay.objects.all()
    return render(request, 'photomap/index.html', {'qs_results': qs_results, 'barangay_results': barangay_results})

def get(request):
  try:
    establishment_type = request.GET["est"].split(',')
  except:
    establishment_type = {"Barangay Halls"}
  print(establishment_type)
  qs_results = ImageSpot.objects.filter(establishment_type__in=establishment_type)
  barangay_results = Barangay.objects.all()
  return render(request, 'photomap/get.html', {'qs_results': qs_results, 'barangay_results': barangay_results})

def iframetest(request):
  return render(request, 'photomap/iframe.html')