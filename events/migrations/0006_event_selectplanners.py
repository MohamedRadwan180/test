# Generated by Django 2.0.7 on 2018-08-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20180725_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='selectPlanners',
            field=models.ManyToManyField(related_name='selectedPlanners', to='events.Planner'),
        ),
    ]