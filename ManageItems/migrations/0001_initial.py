# Generated by Django 4.0.3 on 2022-03-21 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hwItems',
            fields=[
                ('hwItem', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('hwName', models.CharField(max_length=50)),
                ('hwDescription', models.TextField(max_length=200)),
            ],
        ),
    ]
