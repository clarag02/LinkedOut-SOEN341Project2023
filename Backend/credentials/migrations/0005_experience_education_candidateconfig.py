# Generated by Django 4.1.7 on 2023-02-17 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0004_employer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=1000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credentials.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('minor', models.CharField(max_length=100, null=True)),
                ('skills', models.CharField(max_length=1000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('candidate', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='credentials.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preffered_pronouns', models.CharField(default='None', max_length=50)),
                ('skills', models.CharField(max_length=1000)),
                ('interests', models.CharField(max_length=1000)),
                ('resume', models.BinaryField()),
                ('candidate', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='credentials.candidate')),
                ('current_employer', models.ForeignKey(default=-1, null=True, on_delete=django.db.models.deletion.CASCADE, to='credentials.employer')),
            ],
        ),
    ]
