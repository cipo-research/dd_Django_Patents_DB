from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from dynamic_rest.fields import DynamicRelationField
from dynamic_rest.serializers import DynamicModelSerializer
from .models import pt_main, pt_abstract, pt_disclosure, pt_interested_party, pt_ipc_classification, pt_claim, pt_priority_claim

class pt_abstractSerializer(DynamicModelSerializer):
    class Meta:
        model = pt_abstract
        name = 'pt_abstractSerializer'
        fields = ["patentnumber_id", "abstractsequencenumber", "langfilingcode", "abstractlangcode", "abstracttext", "id"]

class pt_disclosureSerializer(DynamicModelSerializer):
    class Meta:
        model = pt_disclosure
        name = 'pt_disclosureSerializer'
        fields = ["patentnumber_id", "disclosuretextsequencenumber", "langfilingcode", "disclosuretext", "id"]

class pt_interested_partySerializer(DynamicModelSerializer):
    class Meta:
        model = pt_interested_party
        name = 'pt_interested_partySerializer'
        fields = ["patentnumber_id", "agenttypecode", "appltypecode", "interestedpartytypecode", "interestedpartytype", "ownerenabledate", "ownerenddate", "partyname", "partyaddressline1", "partyaddressline2", "partyaddressline3", "partyaddressline4", "partyaddressline5", "partycity", "partyprovincecode", "partyprovince", "partypostalcode", "partycountrycode", "partycountry", "id"]

class pt_ipc_classificationSerializer(DynamicModelSerializer):
    class Meta:
        model = pt_ipc_classification
        name = 'pt_ipc_classificationSerializer'
        fields = ["patentnumber_id", "ipcclassificationsequencenumber", "ipcversiondate", "classificationlevel", "classificationstatuscode", "classificationstatus", "ipcsectioncode", "ipcsection", "ipcclasscode", "ipcclass", "ipcsubclasscode", "ipcsubclass", "ipcmaingroupcode", "ipcgroup", "ipcsubgroupcode", "ipcsubgroup", "id"]

class pt_claimSerializer(DynamicModelSerializer):
    class Meta:
        model = pt_claim
        name = 'pt_claimSerializer'
        fields = ["patentnumber_id", "claimtextsequencenumber", "langfilingcode", "claimstext", "id"]
        # depth = 1

class pt_priorityclaimSerializer(DynamicModelSerializer):
    class Meta:
        model = pt_priority_claim
        name = 'pt_priorityclaimSerializer'
        fields = ["patentnumber_id", "foreignappnumber", "priorityclaimkindcode", "priorityclaimcountrycode", "priorityclaimcountry", "calendardate", "id"]

class pt_mainSerializer(DynamicModelSerializer):   
    claim = DynamicRelationField(pt_claimSerializer, embed=True, many=True)
    abstract = DynamicRelationField(pt_abstractSerializer, embed=True, many=True)
    disclosure = DynamicRelationField(pt_disclosureSerializer, embed=True, many=True)
    interested_party = DynamicRelationField(pt_interested_partySerializer, embed=True, many=True)
    ipc_classification = DynamicRelationField(pt_ipc_classificationSerializer, embed=True, many=True)
    priority_claim = DynamicRelationField(pt_priorityclaimSerializer, embed=True, many=True)

    class Meta:
        model = pt_main
        name = 'pt_main'
        fields = ['patentnumber', 'filingdate', 'grantdate', 'appstatuscode', 'apptypecode', 'patenttitleenglish', 'patenttitlefrench', 'bibliographicfileextractdate', 'countryofpublicationcode', 'documentkindtype', 'examinationrequestdate', 'filingcountrycode', 'langfilingcode', 'licenseforsaleindicator', 'pctappnumber' , 'pctpubnumber', 'pctpubdate', 'parentappnumber', 'pctarticle2239fulfilleddate', 'pctsect371date', 'pctpubcountrycode', 'pubkindtype', 'printedasamendedcountrycode', 'claim', 'abstract', 'disclosure', 'interested_party', 'ipc_classification', 'priority_claim']