# Generated by Django 3.0.7 on 2020-07-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200712_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollCourse',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=20)),
                ('fees', models.FloatField()),
                ('duration', models.IntegerField()),
                ('sid', models.IntegerField()),
            ],
        ),
    ]
