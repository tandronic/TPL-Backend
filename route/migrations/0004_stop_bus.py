# Generated by Django 3.2.12 on 2022-03-27 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0003_auto_20220327_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='stop',
            name='bus',
            field=models.ManyToManyField(related_name='stop', to='route.Bus'),
        ),
    ]