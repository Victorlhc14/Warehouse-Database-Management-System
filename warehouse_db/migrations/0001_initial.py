# Generated by Django 3.0 on 2019-12-09 18:08

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
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('manufacturer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stock_On_Hand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('quantity1', models.IntegerField()),
                ('quantity2', models.IntegerField()),
                ('quantity3', models.IntegerField()),
                ('product1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producta', to='warehouse_db.Product')),
                ('product2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productb', to='warehouse_db.Product')),
                ('product3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productc', to='warehouse_db.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Belonging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
