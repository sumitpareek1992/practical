# Generated by Django 3.0 on 2020-09-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('physics', models.FloatField()),
                ('chemistry', models.FloatField()),
                ('mathematics', models.FloatField()),
                ('english', models.FloatField()),
                ('parsent_no', models.CharField(max_length=5)),
                ('previous_no', models.CharField(max_length=5)),
            ],
        ),
    ]