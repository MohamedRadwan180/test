# Generated by Django 2.0.7 on 2018-07-25 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30)),
                ('event_type', models.CharField(max_length=20)),
                ('event_date_and_time', models.DateTimeField(verbose_name='Event date and Time')),
                ('event_address', models.CharField(max_length=100)),
                ('event_pud_date', models.DateTimeField(verbose_name='Event date and Time')),
                ('event_duration', models.IntegerField()),
                ('event_details', models.CharField(max_length=200)),
                ('event_expcted_cpacity', models.IntegerField()),
                ('event_max_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('event_status', models.IntegerField(choices=[(0, 'Sent'), (1, 'Offered'), (2, 'Accepted'), (3, 'Rejected')])),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('offer_description', models.CharField(max_length=200)),
                ('offer_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Planner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planner_name', models.CharField(max_length=50)),
                ('planner_emaol', models.EmailField(max_length=254)),
                ('planner_mobile', models.IntegerField()),
                ('planner_address', models.CharField(max_length=100)),
                ('planner_category', models.CharField(max_length=1)),
                ('planner_website', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='offer_planner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Planner'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_planner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Planner'),
        ),
    ]
