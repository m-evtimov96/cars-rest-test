# Generated by Django 4.0.3 on 2022-03-09 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_carmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='car_brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='cars.carbrand'),
        ),
    ]