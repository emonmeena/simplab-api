# Generated by Django 3.2.2 on 2021-05-14 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Simplab_API', '0020_alter_team_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='students',
            field=models.ManyToManyField(blank=True, default=[models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Simplab_API.user')], related_name='all_member_teams', to='Simplab_API.User'),
        ),
    ]
