# Generated by Django 4.0.3 on 2022-03-29 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0007_rename_idate_item_date_rename_image_id_item_imageid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Imageid',
            new_name='imageid',
        ),
    ]
