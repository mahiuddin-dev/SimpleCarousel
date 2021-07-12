from django.db import models

# Create your models here.
class Carousel(models.Model):
    SliderHeadLine = models.CharField(max_length=50)
    SliderDes = models.TextField(max_length=150)

    METADATA_FIELD_TYPE_POSITION = (
        ('0', 'Start'),
        ('1', 'Middile'),
        ('2', 'End'),
    )
    SliderTextPosition = models.CharField(max_length=1, choices=METADATA_FIELD_TYPE_POSITION, default=0)
    
    METADATA_FIELD_TYPE = (
        ('0', 'Yes'),
        ('1', 'No'),
    )

    SliderButton = models.CharField(max_length=1, choices=METADATA_FIELD_TYPE, default=0)
    ButtonText = models.CharField(max_length=50, blank=True, null= True,default='Click Here')
    SliderImg = models.ImageField(upload_to='Carousel/')

    @property
    def value(self):
        if self.fieldtype == '0':
            return self.ButtonText
    

class HeadingContent(models.Model):
    HeadingTitle = models.CharField(max_length=50)
    ShortText = models.TextField(max_length=250)
    Image = models.ImageField(upload_to='Heading/')
    
    def __str__(self):
        return self.HeadingTitle


class Feature(models.Model):
    Title = models.CharField(max_length=150)
    ShortText = models.TextField(max_length=250)
    Image = models.ImageField(upload_to='Feature/')


    def __str__(self):
        return self.Title
