# Generated by Django 2.2.6 on 2019-10-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20191004_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Flats', 'Flats'), ('Villas', 'Villas'), ('Land', 'Land'), ('Shopping Complex', 'Shopping Complexes')], max_length=30),
        ),
        migrations.AlterField(
            model_name='article',
            name='condition',
            field=models.CharField(choices=[('New', 'NEW'), ('Used', 'Used'), ('Upcoming project', 'Upcoming Project')], max_length=30),
        ),
    ]
