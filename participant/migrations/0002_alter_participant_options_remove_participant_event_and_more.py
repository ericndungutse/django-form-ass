# Generated by Django 4.2.2 on 2023-07-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_options'),
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participant',
            options={'verbose_name': 'Participant', 'verbose_name_plural': 'Participants'},
        ),
        migrations.RemoveField(
            model_name='participant',
            name='event',
        ),
        migrations.AddField(
            model_name='participant',
            name='events',
            field=models.ManyToManyField(to='event.event'),
        ),
    ]