# Generated by Django 2.0.7 on 2018-07-25 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_date_and_time',
            new_name='date_and_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_details',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_duration',
            new_name='duration',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_expcted_cpacity',
            new_name='expcted_cpacity',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_max_price',
            new_name='max_price',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_planner',
            new_name='planner',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_pud_date',
            new_name='pud_date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='offer_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='offer_event',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='offer_planner',
            new_name='planner',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='offer_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='planner',
            old_name='planner_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='planner',
            old_name='planner_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='planner',
            old_name='planner_emaol',
            new_name='emaol',
        ),
        migrations.RenameField(
            model_name='planner',
            old_name='planner_mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='planner',
            old_name='planner_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='planner',
            old_name='planner_website',
            new_name='website',
        ),
    ]