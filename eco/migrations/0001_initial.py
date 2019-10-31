# Generated by Django 2.2.4 on 2019-10-31 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('image', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('type', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('sensors', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('remarks', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('family', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('genus', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('species', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('variety', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('cultivar', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('superior_selection', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('type', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('brand', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('model', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Datalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('light', models.FloatField(blank=True, default=None, null=True)),
                ('temperature', models.FloatField(blank=True, default=None, null=True)),
                ('humidity', models.FloatField(blank=True, default=None, null=True)),
                ('soil', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('moisture', models.FloatField(blank=True, default=None, null=True)),
                ('remarks', models.TextField(blank=True, default=None, null=True)),
                ('alive', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('environment', models.BooleanField(blank=True, default=None, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('plant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eco.Plant')),
            ],
        ),
    ]
