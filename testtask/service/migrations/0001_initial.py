# Generated by Django 3.2.4 on 2021-06-02 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='album',
            fields=[
                ('userId', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
            ],
        ),
    ]
