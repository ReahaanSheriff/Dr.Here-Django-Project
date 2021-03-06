# Generated by Django 3.0.5 on 2020-10-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='d_det',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='d_profile',
            fields=[
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=25)),
                ('mobile', models.IntegerField()),
                ('prof_pic', models.ImageField(upload_to='pics')),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('door_no', models.IntegerField()),
                ('st_name', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('zip_code', models.IntegerField()),
                ('degree', models.CharField(max_length=25)),
                ('department', models.CharField(max_length=25)),
                ('exp', models.IntegerField()),
                ('id_no', models.IntegerField(primary_key=True, serialize=False)),
                ('id_proof', models.ImageField(upload_to='pics')),
                ('hos_name', models.CharField(max_length=50)),
                ('hos_door_no', models.IntegerField()),
                ('hos_st_name', models.CharField(max_length=100)),
                ('hos_area', models.CharField(max_length=25)),
                ('hos_city', models.CharField(max_length=25)),
                ('hos_state', models.CharField(max_length=25)),
                ('hos_zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='p_det',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pat_ap',
            fields=[
                ('ap_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('dept', models.CharField(max_length=20)),
                ('mob_no', models.IntegerField()),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=75)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
