# Generated by Django 4.2.5 on 2023-10-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patents', '0002_remove_pt_main_patents_pt__search__a861b6_gin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pt_main',
            name='parentappnumber',
            field=models.IntegerField(null=True),
        ),
    ]
