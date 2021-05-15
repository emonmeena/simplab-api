# Generated by Django 3.2.2 on 2021-05-14 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simplab_API', '0016_alter_team_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teams', models.ManyToManyField(blank=True, related_name='all', to='Simplab_API.Team')),
            ],
        ),
    ]