# Generated by Django 4.2.11 on 2024-04-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendor_management", "0002_customuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalperformance",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
