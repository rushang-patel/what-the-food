# Generated by Django 4.2.3 on 2023-08-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='checkboxes',
            field=models.CharField(blank=True, choices=[('Vegetarian', 'Vegetarian'), ('Dairy-Free', 'Dairy-Free'), ('Beef', 'Beef'), ('Pork', 'Pork'), ('Chicken', 'Chicken')], max_length=100),
        ),
    ]
