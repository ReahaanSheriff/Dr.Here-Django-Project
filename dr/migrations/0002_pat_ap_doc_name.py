# Generated by Django 3.0.5 on 2020-10-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pat_ap',
            name='doc_name',
            field=models.CharField(default='NULL', max_length=30),
        ),
    ]