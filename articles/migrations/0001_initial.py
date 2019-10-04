# Generated by Django 2.2.6 on 2019-10-04 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('FT', 'Flats'), ('VL', 'Villas'), ('LD', 'Land'), ('CX', 'Shopping Complex')], max_length=30)),
                ('condition', models.CharField(choices=[('NW', 'NEW'), ('UD', 'Used'), ('UC', 'Upcoming Project')], max_length=30)),
                ('owner_name', models.CharField(max_length=40)),
                ('owner_address', models.TextField()),
                ('description', models.TextField()),
                ('location', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Article',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.Article')),
            ],
        ),
    ]
