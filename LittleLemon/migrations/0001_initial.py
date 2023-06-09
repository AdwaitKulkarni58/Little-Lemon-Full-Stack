# Generated by Django 3.2.13 on 2023-03-15 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id', models.IntegerField(verbose_name=11)),
                ('name', models.CharField(max_length=255)),
                ('no_of_guests', models.IntegerField(verbose_name=6)),
                ('bookingDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id', models.IntegerField(verbose_name=5)),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory', models.IntegerField(verbose_name=5)),
            ],
        ),
    ]
