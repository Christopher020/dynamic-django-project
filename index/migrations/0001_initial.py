# Generated by Django 4.0.3 on 2022-05-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('discription', models.CharField(max_length=800)),
                ('image', models.ImageField(upload_to='about/')),
            ],
        ),
    ]