from django.contrib import admin
from .models import Carousel,HeadingContent,Feature


# Register your models here.
class CarouselAdmin(admin.ModelAdmin):
    list_display = [
        'SliderHeadLine',
        'SliderImg'
    ]

admin.site.register(Carousel,CarouselAdmin)

admin.site.register(HeadingContent)
admin.site.register(Feature)