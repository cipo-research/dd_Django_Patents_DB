from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField

# Create your models here.

# Each "model" class represents a table in our database, with each field being a column
#   in its respective table.
# Each model also has a Meta subclass. These are necessary for us to be able to use full-text
#   search when querying in each table, but they have no effect on the actual structure of the
#   tables in the database

class pt_main(models.Model):
    patentnumber = models.IntegerField(null=False, primary_key=True)
    filingdate = models.CharField(max_length=10, null=True)
    pctfilingdate = models.CharField(max_length=10, null=True)
    grantdate = models.CharField(max_length=11, null=True)
    apptypecode = models.CharField(max_length=10, null=True)
    appstatuscode = models.CharField(max_length=2, null=True)
    bibliographicfileextractdate = models.CharField(max_length=10, null=True)
    countryofpublicationcode = models.CharField(max_length=2, null=True)
    documentkindtype = models.CharField(max_length=2, null=True)
    examinationrequestdate = models.CharField(max_length=10, null=True)
    filingcountrycode = models.CharField(max_length=2, null=True)
    langfilingcode = models.CharField(max_length=2, null=True)
    licenseforsaleindicator = models.BooleanField(null=True)
    pctappnumber = models.CharField(max_length=17, null=True)
    pctpubnumber = models.CharField(max_length=13, null=True)
    pctpubdate = models.CharField(max_length=10, null=True)
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = (GinIndex(fields=['search_vector']),)

class pt_priority_claim(models.Model):
    patentnumber = models.ForeignKey(pt_main, related_name='priority_claim', on_delete=models.PROTECT)
    foreignappnumber = models.IntegerField(null=True)
    priorityclaimkindcode= models.CharField(max_length=2, null=True) # subject to change
    priorityclaimcountrycode= models.CharField(max_length=2, null=True)
    priorityclaimcountry = models.CharField(max_length=100, null=True)
    calendardate = models.CharField(max_length=10, null=True)
    id = models.IntegerField(null=False, primary_key=True)
    # search_vector = SearchVectorField(null=True)

    # class Meta:
    #     indexes = (GinIndex(fields=['search_vector']),)

class pt_abstract(models.Model):
    patentnumber = models.ForeignKey(pt_main, related_name="abstract", on_delete=models.PROTECT)
    abstractsequencenumber = models.IntegerField(null=True)
    abstractlangcode = models.CharField(max_length=2, null=True)
    abstractlang = models.CharField(max_length=25, null=True)
    abstracttext = models.TextField(null=True)
    id = models.IntegerField(null=False, primary_key=True)
    # search_vector = SearchVectorField(null=True)

    # class Meta:
    #     indexes = (GinIndex(fields=['search_vector']),)

class pt_disclosure(models.Model):
    patentnumber = models.ForeignKey(pt_main, related_name='disclosure', on_delete=models.PROTECT)
    disclosuretextsequencenumber = models.IntegerField(null=True)
    parentappnumber = models.CharField(max_length=7, null=True)
    pctarticle2239fulfilleddate = models.DateField(null=True)
    pctappnumber = models.CharField(max_length=17, null=True)
    pctsect371date = models.CharField(max_length=10, null=True)
    pctpubcountrycode = models.CharField(max_length=2, null=True)
    pctpubnumber = models.CharField(max_length=13, null=True)
    pctpubdate = models.CharField(max_length=10, null=True)
    pubkindtype = models.CharField(max_length=2, null=True)
    printedasamendedcountrycode = models.CharField(max_length=2, null=True)
    disclosuretext = models.TextField(null=True)
    id = models.IntegerField(null=False, primary_key=True)
    #search_vector = SearchVectorField(null=True)

    #class Meta:
    #    indexes = (GinIndex(fields=['search_vector']),)

class pt_interested_party(models.Model):
    patentnumber = models.ForeignKey(pt_main, related_name='interested_party', on_delete=models.PROTECT)
    interestedpartycount = models.IntegerField(null=True)
    agenttypecode = models.CharField(max_length=25, null=True)
    appltypecode = models.CharField(max_length=25, null=True)
    interestedpartytypecode = models.CharField(max_length=4, null=True)
    partyname = models.CharField(max_length=300, null=True)
    partyaddressline1 = models.CharField(max_length=100, null=True)
    partyaddressline2 = models.CharField(max_length=100, null=True)
    partyaddressline3 = models.CharField(max_length=100, null=True)
    partyaddressline4 = models.CharField(max_length=100, null=True)
    partyaddressline5 = models.CharField(max_length=100, null=True)
    partycity = models.CharField(max_length=75, null=True)
    partypostalcode = models.CharField(max_length=10, null=True)
    partyprovincecode = models.CharField(max_length=2, null=True)
    partyprovince = models.CharField(max_length=25, null=True)
    id = models.IntegerField(null=False, primary_key=True)
    #search_vector = SearchVectorField(null=True)

    #class Meta:
    #    indexes = (GinIndex(fields=['search_vector']),)

class pt_ipc_classification(models.Model):
    patentnumber = models.ForeignKey(pt_main, related_name= 'ipc_classification', on_delete=models.PROTECT)
    ipcclasscount = models.IntegerField(null=True)
    filingdate = models.CharField(max_length=10, null=True)
    pctfilingdate = models.CharField(max_length=10, null=True)
    classificationlevel = models.CharField(max_length=50, null=True)
    classificationstatuscode = models.CharField(max_length=1, null=True)
    classificationstatus = models.CharField(max_length=50, null=True)
    classofficecountrycode = models.CharField(max_length=2, null=True)
    generationofficecountry = models.CharField(max_length=70, null=True)
    ipclevelcode = models.CharField(max_length=1, null=True)
    ipcsectioncode = models.CharField(max_length=1, null=True)
    ipcsection = models.CharField(max_length=100, null=True)
    ipcclasscode = models.CharField(max_length=2, null=True)
    ipcclass = models.TextField(null=True)
    ipcsubclasscode = models.CharField(max_length=1, null=True)
    ipcsubclass = models.TextField(null=True)
    ipcmaingroupcode = models.IntegerField(null=True)
    ipcgroup = models.TextField(null=True)
    ipcsubgroupcode = models.TextField(null=True)
    ipcsubgroup = models.TextField(null=True)
    id = models.IntegerField(null=False, primary_key=True)
    # search_vector = SearchVectorField(null=True)

    # class Meta:
    #    indexes = (GinIndex(fields=['search_vector']),)

class pt_claim(models.Model):
    patentnumber = models.ForeignKey(pt_main, related_name='claim', on_delete=models.PROTECT)
    claimtextsequencenumber = models.IntegerField(blank = True, null=True)
    parentappnumber = models.CharField(max_length=7, null=True)
    pctarticle2239fulfilleddate = models.DateField(null=True)
    pctappnumber = models.CharField(max_length=17, null=True)
    pctsect371date = models.CharField(max_length=10, null=True)
    pctpubcountrycode = models.CharField(max_length=2, null=True)
    pctpubnumber = models.CharField(max_length=13, null=True)
    pctpubdate = models.CharField(max_length=10, null=True)
    pubkindtype = models.CharField(max_length=2, null=True)
    printedasamendedcountrycode = models.CharField(max_length=2, null=True)
    claimstext = models.TextField(null=True)
    id = models.IntegerField(null=False, primary_key=True)
    # search_vector = SearchVectorField(null=True)

    # class Meta:
    #    indexes = (GinIndex(fields=['search_vector']),)