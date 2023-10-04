from rest_framework import serializers
from .models import pt_main, pt_abstract, pt_disclosure, pt_interested_party, pt_ipc_classification, pt_claim, pt_priority_claim

class pt_abstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = pt_abstract
        fields = '__all__'

class pt_disclosureSerializer(serializers.ModelSerializer):
    class Meta:
        model = pt_disclosure
        fields = '__all__'

class pt_interested_partySerializer(serializers.ModelSerializer):
    class Meta:
        model = pt_interested_party
        fields = '__all__'

class pt_ipc_classificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = pt_ipc_classification
        fields = '__all__'

class pt_claimSerializer(serializers.ModelSerializer):
    class Meta:
        model = pt_claim
        fields = '__all__'

class pt_priorityclaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = pt_priority_claim
        fields = '__all__'

class pt_mainSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('fields', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(pt_mainSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument. 
            # - Figure out why self.fields isnt working (maybe serializers.ModelSerializer -> ModelSerializer)
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    claim = pt_claimSerializer(many=True, read_only=True)
    abstract = pt_abstractSerializer(many=True, read_only=True)
    disclosure = pt_disclosureSerializer(many=True, read_only=True)
    interested_party = pt_interested_partySerializer(many=True, read_only=True)
    ipc_classification = pt_ipc_classificationSerializer(many=True, read_only=True)
    priority_claim = pt_priorityclaimSerializer(many=True, read_only=True)

    class Meta:
        model = pt_main
        #fields = '__all__'
        fields = ['patentnumber', 'filingdate', 'pctfilingdate', 'grantdate', 'apptypecode', 'appstatuscode', 'bibliographicfileextractdate', 'countryofpublicationcode', 'documentkindtype', 'examinationrequestdate', 'filingcountrycode', 'langfilingcode', 'licenseforsaleindicator', 'pctappnumber' , 'pctpubnumber', 'pctpubdate', 'claim', 'abstract', 'disclosure', 'interested_party', 'ipc_classification', 'priority_claim']