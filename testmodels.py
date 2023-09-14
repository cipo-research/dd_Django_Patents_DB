# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class PtAbstract(models.Model):
    patentnumber = models.ForeignKey('PtMain', models.DO_NOTHING, db_column='patentnumber', blank=True, null=True)
    abstractsequencenumber = models.IntegerField(blank=True, null=True)
    abstractlangcode = models.CharField(max_length=2, blank=True, null=True)
    abstractlang = models.CharField(max_length=25, blank=True, null=True)
    abstracttext = models.TextField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pt_abstract'


class PtClaim(models.Model):
    patentnumber = models.ForeignKey('PtMain', models.DO_NOTHING, db_column='patentnumber', blank=True, null=True)
    claimtextsequencenumber = models.IntegerField(blank=True, null=True)
    parentappnumber = models.CharField(max_length=7, blank=True, null=True)
    pctarticle2239fulfilleddate = models.DateField(blank=True, null=True)
    pctappnumber = models.CharField(max_length=17, blank=True, null=True)
    pctsect371date = models.CharField(max_length=10, blank=True, null=True)
    pctpubcountrycode = models.CharField(max_length=2, blank=True, null=True)
    pctpubnumber = models.CharField(max_length=13, blank=True, null=True)
    pctpubdate = models.CharField(max_length=10, blank=True, null=True)
    pubkindtype = models.CharField(max_length=2, blank=True, null=True)
    printedasamendedcountrycode = models.CharField(max_length=2, blank=True, null=True)
    claimstext = models.TextField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pt_claim'


class PtDisclosure(models.Model):
    patentnumber = models.ForeignKey('PtMain', models.DO_NOTHING, db_column='patentnumber', blank=True, null=True)
    disclosuretextsequencenumber = models.IntegerField(blank=True, null=True)
    parentappnumber = models.CharField(max_length=7, blank=True, null=True)
    pctarticle2239fulfilleddate = models.DateField(blank=True, null=True)
    pctappnumber = models.CharField(max_length=17, blank=True, null=True)
    pctsect371date = models.CharField(max_length=10, blank=True, null=True)
    pctpubcountrycode = models.CharField(max_length=2, blank=True, null=True)
    pctpubnumber = models.CharField(max_length=13, blank=True, null=True)
    pctpubdate = models.CharField(max_length=10, blank=True, null=True)
    pubkindtype = models.CharField(max_length=2, blank=True, null=True)
    printedasamendedcountrycode = models.CharField(max_length=2, blank=True, null=True)
    disclosuretext = models.TextField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pt_disclosure'


class PtInterestedParty(models.Model):
    patentnumber = models.ForeignKey('PtMain', models.DO_NOTHING, db_column='patentnumber', blank=True, null=True)
    interestedpartycount = models.IntegerField(blank=True, null=True)
    agenttypecode = models.CharField(max_length=20, blank=True, null=True)
    appltypecode = models.CharField(max_length=20, blank=True, null=True)
    interestedpartytypecode = models.CharField(max_length=4, blank=True, null=True)
    partyname = models.TextField(blank=True, null=True)
    partyaddressline1 = models.CharField(max_length=100, blank=True, null=True)
    partyaddressline2 = models.CharField(max_length=100, blank=True, null=True)
    partyaddressline3 = models.CharField(max_length=100, blank=True, null=True)
    partyaddressline4 = models.CharField(max_length=100, blank=True, null=True)
    partyaddressline5 = models.CharField(max_length=100, blank=True, null=True)
    partycity = models.CharField(max_length=75, blank=True, null=True)
    partypostalcode = models.CharField(max_length=10, blank=True, null=True)
    partyprovincecode = models.CharField(max_length=2, blank=True, null=True)
    partyprovince = models.CharField(max_length=25, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pt_interested_party'


class PtIpcClassification(models.Model):
    patentnumber = models.ForeignKey('PtMain', models.DO_NOTHING, db_column='patentnumber', blank=True, null=True)
    ipcclasscount = models.IntegerField(blank=True, null=True)
    filingdate = models.CharField(max_length=10, blank=True, null=True)
    pctfilingdate = models.CharField(max_length=10, blank=True, null=True)
    classificationlevel = models.CharField(max_length=50, blank=True, null=True)
    classificationstatuscode = models.CharField(max_length=1, blank=True, null=True)
    classificationstatus = models.CharField(max_length=50, blank=True, null=True)
    classofficecountrycode = models.CharField(max_length=2, blank=True, null=True)
    generationofficecountry = models.CharField(max_length=70, blank=True, null=True)
    classlevelcode = models.CharField(max_length=1, blank=True, null=True)
    ipcsectioncode = models.CharField(max_length=1, blank=True, null=True)
    ipcsection = models.CharField(max_length=100, blank=True, null=True)
    ipcclasscode = models.CharField(max_length=2, blank=True, null=True)
    ipcclass = models.TextField(blank=True, null=True)
    ipcsubclasscode = models.CharField(max_length=1, blank=True, null=True)
    ipcsubclass = models.TextField(blank=True, null=True)
    ipcmaingroupcode = models.IntegerField(blank=True, null=True)
    ipcgroup = models.TextField(blank=True, null=True)
    ipcsubgroupcode = models.IntegerField(blank=True, null=True)
    ipcsubgroup = models.TextField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pt_ipc_classification'


class PtMain(models.Model):
    patentnumber = models.IntegerField(primary_key=True)
    filingdate = models.CharField(max_length=10, blank=True, null=True)
    pctfilingdate = models.CharField(max_length=10, blank=True, null=True)
    granteddate = models.CharField(max_length=11, blank=True, null=True)
    apptypecode = models.CharField(max_length=10, blank=True, null=True)
    appstatuscode = models.CharField(max_length=2, blank=True, null=True)
    bibliographicfileextractdate = models.CharField(max_length=10, blank=True, null=True)
    countryofpublicationcode = models.CharField(max_length=2, blank=True, null=True)
    documentkindtype = models.CharField(max_length=2, blank=True, null=True)
    examinationrequestdate = models.CharField(max_length=10, blank=True, null=True)
    filingcountrycode = models.CharField(max_length=2, blank=True, null=True)
    langfilingcode = models.CharField(max_length=2, blank=True, null=True)
    licenseforsaleindicator = models.BooleanField(blank=True, null=True)
    pctappnumber = models.CharField(max_length=17, blank=True, null=True)
    pctpubnumber = models.CharField(max_length=13, blank=True, null=True)
    pctpubdate = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pt_main'
