# Generated by Django 4.0.6 on 2022-08-12 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimationapi', '0004_populationactiveoffreemploisecteur'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonneeProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier', models.FileField(upload_to='files')),
                ('date_heure_envoie', models.DateTimeField(auto_now_add=True)),
                ('date_envoie', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
