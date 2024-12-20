# Generated by Django 4.0.3 on 2022-03-29 11:25

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_alter_images2_patient_id_alter_images2_image_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=191)),
                ('description', models.TextField(max_length=50)),
                ('Idate', models.TextField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to=images.models.user_directory_path)),
            ],
        ),
    ]
