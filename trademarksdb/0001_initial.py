# Generated by Django 4.2.5 on 2023-10-11 15:39

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        ###################################### New tm models below
        migrations.CreateModel(
            name='tm_main',
            fields=[
                ('applicationnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('filingdate', models.CharField(max_length=10, null=True)),
                ('publicationdate', models.CharField(max_length=10, null=True)),
                ('registrationdate', models.CharField(max_length=10, null=True)),
                ('registrationofficecountrycode', models.CharField(max_length=2, null=True)),
                ('receivingofficecountrycode', models.CharField(max_length=2, null=True)),
                ('receivingofficedate', models.CharField(max_length=10, null=True)),
                ('assigningofficecountrycode', models.CharField(max_length=2, null=True)),
                ('registrationnumber', models.CharField(null=True)),
                ('legislationcode', models.IntegerField(max_length=1, null=True)),
                ('filingplace', models.CharField(null=True)),
                ('applicationreferencenumber', models.CharField(null=True)),
                ('applicationlanguagecode', models.CharField(max_length=2, null=True)),
                ('expirydate', models.CharField(max_length=10, null=True)),
                ('terminationdate', models.CharField(max_length=10, null=True)),
                ('wipostatuscode', models.IntegerField(max_length=2, null=True)),
                ('currentstatusdate', models.CharField(max_length=10, null=True)),
                ('associationcategoryid', models.CharField(null=True)),
                ('ipofficecode', models.CharField(max_length=2, null=True)),
                ('associatedapplicationnumber', models.IntegerField(max_length=15, null=True)),
                ('markcategory', models.CharField(max_length=9, null=True)),
                ('divisionalapplicationcountrycode', models.CharField(max_length=2, null=True)),
                ('divisionalapplicationnumber', models.IntegerField(max_length=15, null=True)),
                ('divisionalapplicationdate', models.CharField(max_length=10, null=True)),
                ('internationalregistrationnumber', models.IntegerField(null=True)),
                ('marktypecode', models.IntegerField(max_length=2, null=True)),
                ('markverbalelementtext', models.CharField(null=True)),
                ('marksignificantverbalelementtext', models.CharField(null=True)),
                ('marktranslationtext', models.CharField(max_length=10, null=True)),
                ('expungementindicator', models.IntegerField(max_length=1, null=True)),
                ('distinctivenessindicator', models.IntegerField(max_length=1, null=True)),
                ('distinctivenessdescription', models.TextField(null=True)),
                ('evidenceofuseindicator', models.IntegerField(max_length=1, null=True)),
                ('evidenceofusedescription', models.TextField(null=True)),
                ('restrictionofusedescription', models.TextField(null=True)),
                ('cipostandardmessagedescription', models.TextField(null=True)),
                ('oppositionstartdate', models.CharField(max_length=10, null=True)),
                ('oppositionenddate', models.CharField(max_length=10, null=True)),
                ('totalniceclassificationsnumber', models.IntegerField(null=True)),
                ('foreignregistrationindicator', models.IntegerField(max_length=1, null=True)),
                ('usedincanadaindicator', models.IntegerField(max_length=1, null=True)),
                ('classificationtermofficecountrycode', models.CharField(max_length=2, null=True)),
                ('classificationtermsourcecategory', models.TextField(null=True)),
                ('classificationtermenglishdescription', models.TextField(null=True)),
                ('publicationid', models.CharField(max_length=20, null=True)),
                ('publicationstatus', models.CharField(max_length=20, null=True)),
                ('authorizationofusedate', models.CharField(max_length=10, null=True)),
                ('authorizationcode', models.IntegerField(max_length=1, null=True)),
                ('authorizationdescription', models.TextField(null=True)),
                ('registercode', models.IntegerField(max_length=1, null=True)),
                ('applicationabandoneddate', models.CharField(max_length=10, null=True)),
                ('cipostatuscode', models.IntegerField(max_length=2, null=True)),
                ('alloweddate', models.CharField(max_length=10, null=True)),
                ('renewaldate', models.CharField(max_length=10, null=True)),
                ('trademarkclasscode', models.IntegerField(max_length=2, null=True)),
                ('legislationcode', models.IntegerField(max_length=1, null=True)),
                ('geographicalindicationkindcategorycode', models.IntegerField(max_length=1, null=True)),
                ('geographicalindicationtranslationsequencenumber', models.IntegerField(max_length=2, null=True)),
                ('geographicalindicationtranslationtext', models.CharField(max_length=20, null=True)),
                ('doubtfulcaseapplicationnumber', models.IntegerField(max_length=10, null=True)),
                ('doubtfulcaseregistrationnumber', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tm_mark_description',
            fields=[
                ('languagecode', models.CharField(max_length=2, null=True)),
                ('markdescription', models.TextField(null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_cipo_classifications',
            fields=[
                ('classificationkindcode', models.CharField(max_length=4, null=True)),
                ('niceclassificationcode', models.IntegerField(max_length=2, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_applicant_classifications',
            fields=[
                ('classificationsequencenumber', models.CharField(max_length=20, null=True)),
                ('classificationindicatorlinesequencenumber', models.IntegerField(max_length=2, null=True)),
                ('classificationindicatordescription', models.TextField(null=True)),
                ('niceeditionnumber', models.IntegerField(max_length=2, null=True)),
                ('niceclassificationcode', models.IntegerField(max_length=2, null=True)),
                ('niceclassification', models.IntegerField(max_length=2, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_representation',
            fields=[
                ('representationtypecode', models.IntegerField(max_length=1, null=True)),
                ('viennacode', models.IntegerField(max_length=2, null=True)),
                ('viennadivisionnumber', models.IntegerField(max_length=2, null=True)),
                ('viennasectionnumber', models.IntegerField(max_length=2, null=True)),
                ('viennadescription', models.TextField(null=True)),
                ('viennadescriptionfr', models.TextField(null=True)),
                ('filename', models.CharField(max_length=20, null=True)),
                ('fileformat', models.CharField(max_length=20, null=True)),
                ('imagecolourclaimedsequencenumber', models.IntegerField(max_length=2, null=True)),
                ('imagecolourclaimed', models.TextField(null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_interested_party',
            fields=[
                ('partytypecode', models.IntegerField(max_length=2, null=True)),
                ('partylanguagecode', models.CharField(max_length=2, null=True)),
                ('partyname', models.TextField(null=True)),
                ('partyaddressline1', models.TextField(null=True)),
                ('partyaddressline2', models.TextField(null=True)),
                ('partyaddressline3', models.TextField(null=True)),
                ('partyaddressline4', models.TextField(null=True)),
                ('partyaddressline5', models.TextField(null=True)),
                ('partyprovincename', models.CharField(max_length=20, null=True)),
                ('partycountrycode', models.CharField(max_length=2, null=True)),
                ('partypostalcode', models.CharField(max_length=6, null=True)),
                ('contactlanguagecode', models.CharField(max_length=2, null=True)),
                ('contactname', models.TextField(null=True)),
                ('contactaddressline1', models.TextField(null=True)),
                ('contactaddressline2', models.TextField(null=True)),
                ('contactaddressline3', models.TextField(null=True)),
                ('contactprovincename', models.CharField(max_length=20, null=True)),
                ('contactcountrycode', models.CharField(max_length=2, null=True)),
                ('contactpostalcode', models.CharField(max_length=2, null=True)),
                ('currentownerlegalname', models.TextField(null=True)),
                ('agentnumber', models.IntegerField(max_length=20, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_claim',
            fields=[
                ('claimtext', models.TextField(null=True)),
                ('claimtype', models.IntegerField(max_length=2, null=True)),
                ('claimcode', models.IntegerField(max_length=2, null=True)),
                ('structureclaimdate', models.CharField(max_length=10, null=True)),
                ('claimyearnumber', models.IntegerField(max_length=4, null=True)),
                ('claimmonthnumber', models.IntegerField(max_length=2, null=True)),
                ('claimdaynumber', models.IntegerField(max_length=2, null=True)),
                ('claimcountrycode', models.CharField(max_length=2, null=True)),
                ('foreignregistrationnumber', models.IntegerField(max_length=10, null=True)),
                ('goodsservicesreferenceidentifier', models.CharField(max_length=15, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_priority_claim',
            fields=[
                ('priorityclaimtext', models.TextField(null=True)),
                ('prioritycountrycode', models.CharField(max_length=2, null=True)),
                ('priorityapplicationnumber', models.CharField(max_length=10, null=True)),
                ('priorityfilingdate', models.CharField(max_length=10, null=True)),
                ('classificationsequencenumber', models.CharField(max_length=15, null=True)),
                ('classificationdescription', models.TextField(null=True)),
                ('secondarysequencenumber', models.IntegerField(max_length=2, null=True)),
                ('niceeditionnumber', models.IntegerField(max_length=2, null=True)),
                ('niceclassificationcode', models.IntegerField(max_length=2, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_event',
            fields=[
                ('actiondate', models.CharField(max_length=10, null=True)),
                ('responsedate', models.CharField(max_length=10, null=True)),
                ('additionalinformationcomment', models.TextField(null=True)),
                ('wipoactiontype', models.TextField(null=True)),
                ('cipoactioncode', models.IntegerField(max_length=3, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_application_disclaimer',
            fields=[
                ('languagecode', models.CharField(max_length=2, null=True)),
                ('disclaimertextsequencenumber', models.IntegerField(max_length=2, null=True)),
                ('disclaimertext', models.TextField(null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_application_text',
            fields=[
                ('applicationtextcode', models.CharField(max_length=2, null=True)),
                ('sequencenumber', models.IntegerField(max_length=2, null=True)),
                ('secondarysequencenumber', models.IntegerField(max_length=2, null=True)),
                ('applicationtextchangeddate', models.CharField(max_length=10, null=True)),
                ('applicationtextdetails', models.TextField(null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_transliteration',
            fields=[
                ('marktransliterationtext', models.TextField(null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_footnote',
            fields=[
                ('footnotetextlinesequencenumber', models.IntegerField(max_length=2, null=True)),
                ('footnotetextlinedescription', models.TextField(null=True)),
                ('footnotenumber', models.IntegerField(max_length=2, null=True)),
                ('footnotecategorycode', models.IntegerField(max_length=2, null=True)),
                ('footnotechangedate', models.CharField(max_length=10, null=True)),
                ('footnoteregistrationdate', models.CharField(max_length=10, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_footnote_formatted',
            fields=[
                ('footnotenumber', models.IntegerField(max_length=2, null=True)),
                ('footnoteformattedtextsequencenumber', models.IntegerField(max_length=2, null=True)),
                ('footnoteformattedtext', models.TextField(null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_application_text',
            fields=[
                ('applicationtextcode', models.CharField(max_length=2, null=True)),
                ('sequencenumber', models.IntegerField(max_length=2, null=True)),
                ('secondarysequencenumber', models.IntegerField(max_length=2, null=True)),
                ('applicationtextchangeddate', models.CharField(max_length=10, null=True)),
                ('applicationtextdetails', models.TextField(null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_heading',
            fields=[
                ('indexheadingnumber', models.IntegerField(max_length=2, null=True)),
                ('indexheadingcomment', models.TextField(null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_cancellation_case',
            fields=[
                ('section4445casenumber', models.IntegerField(max_length=1, null=True)),
                ('legalproceedingtypedescriptioninenglish', models.CharField(max_length=40, null=True)),
                ('legalproceedingtypedescriptioninfrench', models.CharField(max_length=50, null=True)),
                ('section4445filingdate', models.CharField(max_length=10, null=True)),
                ('wiposection4445statuscategorycode', models.IntegerField(max_length=1, null=True)),
                ('section4445statuscode', models.IntegerField(max_length=1, null=True)),
                ('section4445statusdate', models.CharField(max_length=10, null=True)),
                ('entitynameofthelegalproceedingdefendant', models.TextField(null=True)),
                ('defendantlanguagecode', models.CharField(max_length=2, null=True)),
                ('defendantaddressline1', models.TextField(null=True)),
                ('defendantaddressline2', models.TextField(null=True)),
                ('defendantaddressline3', models.TextField(null=True)),
                ('defendantcountrycode', models.CharField(max_length=2, null=True)),
                ('contactnameofdefendant', models.TextField(null=True)),
                ('contactlanguagecodeofdefendant', models.CharField(max_length=2, null=True)),
                ('contactaddressline1ofdefendant', models.TextField(null=True)),
                ('contactaddressline2ofdefendant', models.TextField(null=True)),
                ('contactaddressline3ofdefendant', models.TextField(null=True)),
                ('contactprovincenameofdefendant', models.CharField(max_length=20, null=True)),
                ('contactcountrycodeofdefendant', models.CharField(max_length=2, null=True)),
                ('contactpostalcodeofdefendant', models.CharField(max_length=6, null=True)),
                ('agentnameofdefendant', models.TextField(null=True)),
                ('agentlanguagecodeofdefendant', models.CharField(max_length=2, null=True)),
                ('agentaddressline1ofdefendant', models.TextField(null=True)),
                ('agentaddressline2ofdefendant', models.TextField(null=True)),
                ('agentaddressline3ofdefendant', models.TextField(null=True)),
                ('agentprovincenameofdefendant', models.CharField(max_length=20, null=True)),
                ('agentcountrycodeofdefendant', models.CharField(max_length=2, null=True)),
                ('agentpostalcodeofdefendant', models.CharField(max_length=6, null=True)),
                ('plaintiffname', models.TextField(null=True)),
                ('plaintifflegalname', models.TextField(null=True)),
                ('plaintifflanguagecode', models.CharField(max_length=2, null=True)),
                ('plaintiffaddressline1', models.TextField(null=True)),
                ('plaintiffaddressline2', models.TextField(null=True)),
                ('plaintiffaddressline3', models.TextField(null=True)),
                ('plaintiffcountrycode', models.CharField(max_length=2, null=True)),
                ('contactnameofplaintiff', models.TextField(null=True)),
                ('contactlanguagecodeofplaintiff', models.CharField(max_length=2, null=True)),
                ('contactaddressline1ofplaintiff', models.TextField(null=True)),
                ('contactaddressline2ofplaintiff', models.TextField(null=True)),
                ('contactaddressline3ofplaintiff', models.TextField(null=True)),
                ('contactprovincenameofplaintiff', models.CharField(max_length=20, null=True)),
                ('contactcountrycodeofplaintiff', models.CharField(max_length=2, null=True)),
                ('contactpostalcodeofplaintiff', models.CharField(max_length=6, null=True)),
                ('agentnumberofplaintiff', models.IntegerField(max_length=10, null=True)),
                ('agentnameofplaintiff', models.TextField(null=True)),
                ('agentlanguagecodeofplaintiff', models.CharField(max_length=2, null=True)),
                ('agentaddressline1ofplaintiff', models.TextField(null=True)),
                ('agentaddressline2ofplaintiff', models.TextField(null=True)),
                ('agentaddressline3ofplaintiff', models.TextField(null=True)),
                ('agentprovincenameofplaintiff', models.CharField(max_length=20, null=True)),
                ('agentcountrycodeofplaintiff', models.CharField(max_length=2, null=True)),
                ('agentpostalcodeofplaintiff', models.CharField(max_length=6, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_cancellation_case_action',
            fields=[
                ('additionalcomment', models.TextField(null=True)),
                ('proceedingeffectivedate', models.CharField(max_length=10, null=True)),
                ('section4445casenumber', models.IntegerField(max_length=1, null=True)),
                ('legalproceedingtypedescriptioninenglish', models.CharField(max_length=40, null=True)),
                ('legalproceedingtypedescriptioninfrench', models.CharField(max_length=50, null=True)),
                ('section4445filingdate', models.CharField(max_length=10, null=True)),
                ('wiposection4445statuscategorycode', models.IntegerField(max_length=1, null=True)),
                ('section4445statuscode', models.IntegerField(max_length=1, null=True)),
                ('section4445statusdate', models.CharField(max_length=10, null=True)),
                ('section4445stagecode', models.IntegerField(max_length=3, null=True)),
                ('section4445casestatus', models.TextField(null=True)),
                ('section4445actionscode', models.CharField(max_length=3, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_opposition_case',
            fields=[
                ('oppositioncasenumber', models.IntegerField(max_length=2, null=True)),
                ('oppositioncasetypeenglishname', models.CharField(max_length=25, null=True)),
                ('oppositioncasetypefrenchname', models.CharField(max_length=30, null=True)),
                ('oppositiondate', models.CharField(max_length=10, null=True)),
                ('wipooppositioncasestatus', models.CharField(max_length=30, null=True)),
                ('oppositionwipostatusdate', models.CharField(max_length=10, null=True)),
                ('wipooppositionstatuscategory', models.IntegerField(max_length=1, null=True)),
                ('oppositioncasestatuscode', models.IntegerField(max_length=1, null=True)),
                ('cipooppositionstatusdate', models.CharField(max_length=10, null=True)),
                ('entitynameoftheoppositionproceedingdefendant', models.TextField(null=True)),
                ('defendantlanguagecode', models.CharField(max_length=2, null=True)),
                ('defendantaddressline1', models.TextField(null=True)),
                ('defendantaddressline2', models.TextField(null=True)),
                ('defendantaddressline3', models.TextField(null=True)),
                ('defendantcountrycode', models.CharField(max_length=2, null=True)),
                ('contactnameofdefendant', models.TextField(null=True)),
                ('contactlanguagecodeofdefendant', models.CharField(max_length=2, null=True)),
                ('contactaddressline1ofdefendant', models.TextField(null=True)),
                ('contactaddressline2ofdefendant', models.TextField(null=True)),
                ('contactaddressline3ofdefendant', models.TextField(null=True)),
                ('contactprovincenameofdefendant', models.CharField(max_length=20, null=True)),
                ('contactcountrycodeofdefendant', models.CharField(max_length=2, null=True)),
                ('contactpostalcodeofdefendant', models.CharField(max_length=6, null=True)),
                ('agentnameofdefendant', models.TextField(null=True)),
                ('agentlanguagecodeofdefendant', models.CharField(max_length=2, null=True)),
                ('agentaddressline1ofdefendant', models.TextField(null=True)),
                ('agentaddressline2ofdefendant', models.TextField(null=True)),
                ('agentaddressline3ofdefendant', models.TextField(null=True)),
                ('agentprovincenameofdefendant', models.CharField(max_length=20, null=True)),
                ('agentcountrycodeofdefendant', models.CharField(max_length=2, null=True)),
                ('agentpostalcodeofdefendant', models.CharField(max_length=6, null=True)),
                ('plaintiffname', models.TextField(null=True)),
                ('plaintifflegalname', models.TextField(null=True)),
                ('plaintifflanguagecode', models.CharField(max_length=2, null=True)),
                ('plaintiffaddressline1', models.TextField(null=True)),
                ('plaintiffaddressline2', models.TextField(null=True)),
                ('plaintiffaddressline3', models.TextField(null=True)),
                ('plaintiffcountrycode', models.CharField(max_length=2, null=True)),
                ('contactnameofplaintiff', models.TextField(null=True)),
                ('contactlanguagecodeofplaintiff', models.CharField(max_length=2, null=True)),
                ('contactaddressline1ofplaintiff', models.TextField(null=True)),
                ('contactaddressline2ofplaintiff', models.TextField(null=True)),
                ('contactaddressline3ofplaintiff', models.TextField(null=True)),
                ('contactprovincenameofplaintiff', models.CharField(max_length=20, null=True)),
                ('contactcountrycodeofplaintiff', models.CharField(max_length=2, null=True)),
                ('contactpostalcodeofplaintiff', models.CharField(max_length=6, null=True)),
                ('agentnumberofplaintiff', models.IntegerField(max_length=10, null=True)),
                ('agentnameofplaintiff', models.TextField(null=True)),
                ('agentlanguagecodeofplaintiff', models.CharField(max_length=2, null=True)),
                ('agentaddressline1ofplaintiff', models.TextField(null=True)),
                ('agentaddressline2ofplaintiff', models.TextField(null=True)),
                ('agentaddressline3ofplaintiff', models.TextField(null=True)),
                ('agentprovincenameofplaintiff', models.CharField(max_length=20, null=True)),
                ('agentcountrycodeofplaintiff', models.CharField(max_length=2, null=True)),
                ('agentpostalcodeofplaintiff', models.CharField(max_length=6, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tm_opposition_case_action',
            fields=[
                ('additionalcomment', models.TextField(null=True)),
                ('proceedingeffectivedate', models.CharField(max_length=10, null=True)),
                ('oppositioncasenumber', models.IntegerField(max_length=1, null=True)),
                ('oppositioncasetypeenglishname', models.CharField(max_length=30, null=True)),
                ('oppositioncasetypefrenchname', models.CharField(max_length=40, null=True)),
                ('oppositiondate', models.CharField(max_length=10, null=True)),
                ('wipooppositioncasestatus', models.CharField(max_length=50, null=True)),
                ('oppositionwipostatusdate', models.CharField(max_length=10, null=True)),
                ('wipooppositionstatuscategory', models.IntegerField(max_length=1, null=True)),
                ('oppositioncasestatuscode', models.IntegerField(max_length=1, null=True)),
                ('section4445actionscode', models.CharField(max_length=3, null=True)),
                ('cipooppositionstatusdate', models.CharField(max_length=10, null=True)),
                ('oppositionstagecode', models.IntegerField(max_length=3, null=True)),
                ('oppositionactioncategory', models.CharField(max_length=50, null=True)),
                ('oppositionactioncode', models.IntegerField(max_length=3, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddIndex(
            model_name='tm_main',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='trademarks_tm__search__a861b6_gin'),
        ),
        migrations.AddField(
            model_name='tm_mark_description',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mark_description', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_cipo_classifications',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cipo_classifications', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_applicant_classifications',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='applicant_classifications', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_representation',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='representation', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_interested_party',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='interested_party', to='trademarks.tm_main'),
        ),
        migrations.AddIndex(
            model_name='tm_claim',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='claim', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_priority_claim',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='priority_claim', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_event',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_application_disclaimer',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='application_disclaimer', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_application_text',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='application_text', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_transliteration',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transliteration', to='trademarks.tm_main'),
        ),
        migrations.AddIndex(
            model_name='tm_footnote',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='footnote', to='patents.trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_footnote_formatted',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='footnote_formatted', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_heading',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='heading', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_cancellation_case',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cancellation_case', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_cancellation_case_action',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cancellation_case_action', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_opposition_case',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='opposition_case', to='trademarks.tm_main'),
        ),
        migrations.AddField(
            model_name='tm_opposition_case_action',
            name='applicationnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='opposition_case_action', to='trademarks.tm_main'),
        ),
    ]
