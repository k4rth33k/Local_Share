# Generated by Django 2.1.5 on 2019-11-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id_s', models.AutoField(primary_key=True, serialize=False)),
                ('link', models.TextField()),
            ],
        ),
    ]