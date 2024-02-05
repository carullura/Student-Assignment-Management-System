# Generated by Django 5.0.1 on 2024-02-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementsystem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='subject1_mark',
            new_name='english_mark',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='subject2_mark',
            new_name='maths_mark',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='subject3_mark',
            new_name='tamil_mark',
        ),
        migrations.AddField(
            model_name='student',
            name='biology_mark',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='chemistry_mark',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='computer_science_mark',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='physics_mark',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
