# Generated by Django 3.2.9 on 2021-11-04 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('departamento', models.ManyToManyField(to='departamentos.Departamento')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
