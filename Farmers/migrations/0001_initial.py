# Generated by Django 3.2.7 on 2021-11-12 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('farmer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.farmers')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile_pics')),
                ('farmer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.farmers')),
            ],
        ),
    ]
