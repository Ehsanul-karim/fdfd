# Generated by Django 4.2.6 on 2023-11-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_alter_physicalstructure_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalstructure',
            name='age',
            field=models.IntegerField(choices=[('minor', 'Minor'), ('young', 'Young'), ('adult', 'Adult'), ('aged', 'Aged')], null=True),
        ),
        migrations.AlterField(
            model_name='physicalstructure',
            name='faceShape',
            field=models.CharField(choices=[('oval', 'Oval'), ('round', 'Round'), ('square', 'Square'), ('heart', 'Heart'), ('oblong', 'oblong')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='physicalstructure',
            name='facialHair',
            field=models.CharField(choices=[('beard', 'Beard'), ('mustache', 'Mustache'), ('shaved', 'Shaved')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='physicalstructure',
            name='hairColor',
            field=models.CharField(choices=[('black', 'Black'), ('brown', 'Brown'), ('blonde', 'Blonde')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='physicalstructure',
            name='hairLength',
            field=models.CharField(choices=[('short', 'Short'), ('long', 'Long'), ('medium', 'Medium')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='physicalstructure',
            name='hairStyle',
            field=models.CharField(choices=[('curly', 'Curly'), ('straight', 'Straight'), ('bald', 'Bald')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='physicalstructure',
            name='skinTone',
            field=models.CharField(choices=[('browny', 'Browny'), ('blacky', 'Black'), ('whitey', 'White')], max_length=255, null=True),
        ),
    ]
