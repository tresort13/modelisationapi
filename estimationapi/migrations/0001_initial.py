# Generated by Django 4.0.6 on 2022-07-19 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TauxNataliteMortalite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manifest', models.FileField(upload_to='files')),
                ('date_heure_envoie', models.DateTimeField(auto_now_add=True)),
                ('date_envoie', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
