# Generated by Django 4.1.1 on 2022-10-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=255)),
                ('joining_date', models.DateField()),
            ],
        ),
    ]