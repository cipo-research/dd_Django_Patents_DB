# Generated by Django 4.2.5 on 2023-09-27 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pt_main',
            fields=[
                ('patentnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('filingdate', models.CharField(max_length=10, null=True)),
                ('pctfilingdate', models.CharField(max_length=10, null=True)),
                ('grantdate', models.CharField(max_length=11, null=True)),
                ('apptypecode', models.CharField(max_length=10, null=True)),
                ('appstatuscode', models.CharField(max_length=2, null=True)),
                ('bibliographicfileextractdate', models.CharField(max_length=10, null=True)),
                ('countryofpublicationcode', models.CharField(max_length=2, null=True)),
                ('documentkindtype', models.CharField(max_length=2, null=True)),
                ('examinationrequestdate', models.CharField(max_length=10, null=True)),
                ('filingcountrycode', models.CharField(max_length=2, null=True)),
                ('langfilingcode', models.CharField(max_length=2, null=True)),
                ('licenseforsaleindicator', models.BooleanField(null=True)),
                ('pctappnumber', models.CharField(max_length=17, null=True)),
                ('pctpubnumber', models.CharField(max_length=13, null=True)),
                ('pctpubdate', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pt_priority_claim',
            fields=[
                ('foreignappnumber', models.IntegerField(null=True)),
                ('priorityclaimkindcode', models.CharField(max_length=2, null=True)),
                ('priorityclaimcountrycode', models.CharField(max_length=2, null=True)),
                ('priorityclaimcountry', models.CharField(max_length=100, null=True)),
                ('calendardate', models.CharField(max_length=10, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('patentnumber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patents.pt_main')),
            ],
        ),
        migrations.CreateModel(
            name='pt_ipc_classification',
            fields=[
                ('ipcclasscount', models.IntegerField(null=True)),
                ('filingdate', models.CharField(max_length=10, null=True)),
                ('pctfilingdate', models.CharField(max_length=10, null=True)),
                ('classificationlevel', models.CharField(max_length=50, null=True)),
                ('classificationstatuscode', models.CharField(max_length=1, null=True)),
                ('classificationstatus', models.CharField(max_length=50, null=True)),
                ('classofficecountrycode', models.CharField(max_length=2, null=True)),
                ('generationofficecountry', models.CharField(max_length=70, null=True)),
                ('ipclevelcode', models.CharField(max_length=1, null=True)),
                ('ipcsectioncode', models.CharField(max_length=1, null=True)),
                ('ipcsection', models.CharField(max_length=100, null=True)),
                ('ipcclasscode', models.CharField(max_length=2, null=True)),
                ('ipcclass', models.TextField(null=True)),
                ('ipcsubclasscode', models.CharField(max_length=1, null=True)),
                ('ipcsubclass', models.TextField(null=True)),
                ('ipcmaingroupcode', models.IntegerField(null=True)),
                ('ipcgroup', models.TextField(null=True)),
                ('ipcsubgroupcode', models.TextField(null=True)),
                ('ipcsubgroup', models.TextField(null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('patentnumber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patents.pt_main')),
            ],
        ),
        migrations.CreateModel(
            name='pt_interested_party',
            fields=[
                ('interestedpartycount', models.IntegerField(null=True)),
                ('agenttypecode', models.CharField(max_length=25, null=True)),
                ('appltypecode', models.CharField(max_length=25, null=True)),
                ('interestedpartytypecode', models.CharField(max_length=4, null=True)),
                ('partyname', models.CharField(max_length=300, null=True)),
                ('partyaddressline1', models.CharField(max_length=100, null=True)),
                ('partyaddressline2', models.CharField(max_length=100, null=True)),
                ('partyaddressline3', models.CharField(max_length=100, null=True)),
                ('partyaddressline4', models.CharField(max_length=100, null=True)),
                ('partyaddressline5', models.CharField(max_length=100, null=True)),
                ('partycity', models.CharField(max_length=75, null=True)),
                ('partypostalcode', models.CharField(max_length=10, null=True)),
                ('partyprovincecode', models.CharField(max_length=2, null=True)),
                ('partyprovince', models.CharField(max_length=25, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('patentnumber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patents.pt_main')),
            ],
        ),
        migrations.CreateModel(
            name='pt_disclosure',
            fields=[
                ('disclosuretextsequencenumber', models.IntegerField(null=True)),
                ('parentappnumber', models.CharField(max_length=7, null=True)),
                ('pctarticle2239fulfilleddate', models.DateField(null=True)),
                ('pctappnumber', models.CharField(max_length=17, null=True)),
                ('pctsect371date', models.CharField(max_length=10, null=True)),
                ('pctpubcountrycode', models.CharField(max_length=2, null=True)),
                ('pctpubnumber', models.CharField(max_length=13, null=True)),
                ('pctpubdate', models.CharField(max_length=10, null=True)),
                ('pubkindtype', models.CharField(max_length=2, null=True)),
                ('printedasamendedcountrycode', models.CharField(max_length=2, null=True)),
                ('disclosuretext', models.TextField(null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('patentnumber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patents.pt_main')),
            ],
        ),
        migrations.CreateModel(
            name='pt_claim',
            fields=[
                ('claimtextsequencenumber', models.IntegerField(blank=True, null=True)),
                ('parentappnumber', models.CharField(max_length=7, null=True)),
                ('pctarticle2239fulfilleddate', models.DateField(null=True)),
                ('pctappnumber', models.CharField(max_length=17, null=True)),
                ('pctsect371date', models.CharField(max_length=10, null=True)),
                ('pctpubcountrycode', models.CharField(max_length=2, null=True)),
                ('pctpubnumber', models.CharField(max_length=13, null=True)),
                ('pctpubdate', models.CharField(max_length=10, null=True)),
                ('pubkindtype', models.CharField(max_length=2, null=True)),
                ('printedasamendedcountrycode', models.CharField(max_length=2, null=True)),
                ('claimstext', models.TextField(null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('patentnumber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patents.pt_main')),
            ],
        ),
        migrations.CreateModel(
            name='pt_abstract',
            fields=[
                ('abstractsequencenumber', models.IntegerField(null=True)),
                ('abstractlangcode', models.CharField(max_length=2, null=True)),
                ('abstractlang', models.CharField(max_length=25, null=True)),
                ('abstracttext', models.TextField(null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('patentnumber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patents.pt_main')),
            ],
        ),
    ]
