# Generated by Django 4.0.3 on 2022-03-09 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0003_alter_carmodel_car_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('first_reg', models.DateTimeField()),
                ('odometer', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carbrand')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
