# Generated by Django 5.0.6 on 2024-07-15 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='asignaturas/', verbose_name='Archivo'),
        ),
    ]
