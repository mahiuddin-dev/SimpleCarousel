from django.shortcuts import render
from .models import Carousel,HeadingContent,Feature

# Create your views here.
def Home(request):
    carousel = Carousel.objects.all()
    hcontent = HeadingContent.objects.all().order_by('-pk')[:3]
    feature = Feature.objects.all().order_by('-pk')


    context = {'carousel':carousel, 'hcontent':hcontent,'feature':feature }

    return render(request,'index.html', context)
