# Generated by Django 4.0.4 on 2022-06-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('cname', models.CharField(max_length=30)),
                ('Accno', models.IntegerField()),
                ('bank', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=30)),
            ],
        ),
    ]
