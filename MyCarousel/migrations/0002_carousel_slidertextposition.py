# Generated by Django 3.2 on 2021-07-12 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCarousel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='SliderTextPosition',
            field=models.CharField(choices=[('0', 'Start'), ('1', 'Middile'), ('2', 'End')], default=0, max_length=1),
        ),
    ]