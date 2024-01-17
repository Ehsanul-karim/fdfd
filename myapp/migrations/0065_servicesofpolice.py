# Generated by Django 4.2.6 on 2024-01-16 22:14

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0064_investigatorroles_publicroles'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesOfPolice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to=myapp.models.filepath)),
            ],
        ),
    ]