# Generated by Django 3.2.2 on 2021-05-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simplab_API', '0006_auto_20210517_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='profile_image',
            field=models.ImageField(blank=True, default='/media/profile_images/default.jpg', upload_to='profile_images'),
        ),
    ]
