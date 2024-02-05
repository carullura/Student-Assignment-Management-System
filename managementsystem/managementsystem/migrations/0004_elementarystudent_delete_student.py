# Generated by Django 5.0.1 on 2024-02-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementsystem', '0003_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementaryStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_number', models.CharField(max_length=20, unique=True)),
                ('standard', models.CharField(max_length=10)),
                ('number_of_subjects', models.PositiveIntegerField()),
                ('tamil_mark', models.PositiveIntegerField()),
                ('english_mark', models.PositiveIntegerField()),
                ('maths_mark', models.PositiveIntegerField()),
                ('science_mark', models.PositiveIntegerField()),
                ('social_mark', models.PositiveIntegerField()),
                ('total_marks', models.PositiveIntegerField()),
                ('percentage', models.FloatField()),
                ('pass_fail_status', models.CharField(max_length=10)),
                ('tamil_grade', models.CharField(blank=True, max_length=2, null=True)),
                ('english_grade', models.CharField(blank=True, max_length=2, null=True)),
                ('maths_grade', models.CharField(blank=True, max_length=2, null=True)),
                ('science_grade', models.CharField(blank=True, max_length=2, null=True)),
                ('social_grade', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
