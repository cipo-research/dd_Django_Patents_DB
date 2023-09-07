from rest_framework import serializers
from .models import pt_main, pt_priority_claim, pt_abstract, pt_disclosure, pt_interested_party, pt_ipc_classification, pt_claim

class pt_mainSerializer(serializers.ModelSerializer):
    class Meta:
        model = pt_main
        fields = '__all__'

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