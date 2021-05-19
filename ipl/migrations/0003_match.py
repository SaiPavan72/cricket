# Generated by Django 3.1.7 on 2021-05-19 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0002_auto_20210519_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='ipl.team')),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_one', to='ipl.team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_two', to='ipl.team')),
            ],
        ),
    ]
