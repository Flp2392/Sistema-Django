# Generated by Django 4.2.3 on 2023-07-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=10)),
                ('ano', models.BigIntegerField()),
                ('cor', models.CharField(max_length=10)),
            ],
        ),
    ]
