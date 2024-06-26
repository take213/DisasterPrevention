# Generated by Django 3.2.6 on 2024-05-19 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('postalcode', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('shipmentdate', models.DateField()),
                ('completed', models.BooleanField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['shipmentdate'],
            },
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('postalcode', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('deadline', models.DateField()),
                ('completed', models.BooleanField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['deadline'],
            },
        ),
    ]
