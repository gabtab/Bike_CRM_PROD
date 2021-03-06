# Generated by Django 2.1.5 on 2020-10-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('job_type', models.CharField(max_length=100)),
                ('job_prioity', models.CharField(max_length=100)),
                ('order_number', models.CharField(max_length=100)),
                ('invoice_number', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('assigned', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('last_mod_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
