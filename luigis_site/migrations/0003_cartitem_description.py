# Generated by Django 3.2.25 on 2024-03-10 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luigis_site', '0002_menuitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
