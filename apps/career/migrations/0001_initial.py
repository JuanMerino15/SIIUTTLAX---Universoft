

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academy', '0001_initial'),
        ('period', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Carrera')),
                ('level', models.CharField(choices=[('TSU', 'Técnico Superior Universitario'), ('ING', 'Ingenieria'), ('MTR', 'Maestria'), ('Lic', 'Licenciatura')], max_length=5, verbose_name='Nivel de estudios')),
                ('short_name', models.CharField(max_length=10, verbose_name='Abreviatura')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('year_plan', models.CharField(max_length=4, verbose_name='Año')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.professor', verbose_name='Director')),
            ],
            options={
                'verbose_name': 'Career',
                'verbose_name_plural': 'Careers',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Materia')),
                ('total_hours', models.IntegerField(verbose_name='Horas totales')),
                ('weekly_hours', models.IntegerField(verbose_name='Horas semanales')),
                ('file', models.CharField(max_length=100, verbose_name='Hoja de asignatura')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Carrera')),
                ('semester', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='period.semester', verbose_name='Semestre')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
    ]
