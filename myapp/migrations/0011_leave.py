# Generated by Django 4.2.4 on 2023-09-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_attendance_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Name', models.CharField(max_length=100)),
                ('Start_Date', models.DateField()),
                ('End_Date', models.DateField()),
                ('Leave_Type', models.CharField(max_length=100)),
                ('Reason', models.CharField(max_length=1000)),
            ],
        ),
    ]