# Generated by Django 4.1.7 on 2023-03-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patents', '0003_alter_pt_priority_claim_priorityclaimcountry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pt_interested_party',
            name='partyname',
            field=models.CharField(max_length=75, null=True),
        ),
    ]
