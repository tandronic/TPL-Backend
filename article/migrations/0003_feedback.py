# Generated by Django 3.2.12 on 2022-03-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('resolved', models.BooleanField(default=False)),
            ],
        ),
    ]
