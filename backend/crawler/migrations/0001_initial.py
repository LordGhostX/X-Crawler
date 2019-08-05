# Generated by Django 2.2.3 on 2019-08-04 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Unknown Author', max_length=30)),
                ('pub_title', models.CharField(max_length=200)),
                ('pub_summary', models.CharField(max_length=200)),
                ('pub_url', models.CharField(max_length=200)),
                ('pub_picture', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('fields', models.CharField(max_length=200)),
                ('works', models.CharField(max_length=200)),
                ('pictures', models.ImageField(upload_to='')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawler.Publication')),
            ],
        ),
    ]
