from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import pt_main, pt_abstract, pt_disclosure, pt_interested_party, pt_ipc_classification, pt_claim
from .serializers import pt_mainSerializer, pt_abstractSerializer, pt_disclosureSerializer, pt_interested_partySerializer, pt_ipc_classificationSerializer, pt_claimSerializer
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from dynamic_rest.viewsets import WithDynamicViewSetMixin
#from drf_yasg.utils import swagger_auto_schema

# # Create your views here.

@api_view(['GET'])
def pt_mainFullTextSearch(request):
    """
    API view for full-text search with dynamic field selection on pt_main entries and connected relations.
    
    This API view performs a full-text search on pt_main entries based on user-specified query and fields.
    It also allows for dynamic field selection on nested relations with the abstract, claim, disclosure, interested party, ipc classification, and priority claim tables.

    Args:
        request (rest_framework.request.Request): The HTTP request object.

    Query Parameters:
        - `query` (str): The search query for full-text search. The query should be a patentnumber
        - `fields` (str, optional): Comma-separated list of fields to search. If not provided, all fields will be searched.
        - `abstract` (str, optional): Comma-separated list of fields specific to patents_pt_abstract table to filter results. If not provided, all abstract fields will be displayed.
        - `claim` (str, optional): Comma-separated list of fields specific to patents_pt_claim table to filter results. If not provided, all claim fields will be displayed.
        - `disclosure` (str, optional): Comma-separated list of fields specific to patents_pt_disclosure table to filter results. If not provided, all disclosure fields will be displayed.
        - `interestedparty` (str, optional): Comma-separated list of fields specific to patents_pt_interested_party table to filter results. If not provided, all interested party fields will be displayed.
        - `ipcclassification` (str, optional): Comma-separated list of fields specific to patents_pt_ipc_classification table to filter results. If not provided, all ipc classification fields will be displayed.
        - `priorityclaim` (str, optional): Comma-separated list of fields specific to patents_pt_priority_claim table to filter results. If not provided, all priority claim fields will be displayed.
    """
    query = request.GET.get('query', None) # getting query from user
    fields = request.GET.get('fields', None) # getting fields from user
    claim_fields = request.GET.get('claim', None) # getting claim fields from user
    disclosure_fields = request.GET.get('disclosure', None) # getting disclosure fields from user
    interestedparty_fields = request.GET.get('interestedparty', None) # getting interested party fields from user
    ipc_fields = request.GET.get('ipcclassification', None) # getting ipc classification fields from user
    abstract_fields = request.GET.get('abstract', None) # getting abstract fields from user

    if fields and len(fields) > 0: # fields is expected to be a comma-separated list (string)
        fields = fields.split(',')
    if claim_fields and len(claim_fields) > 0: 
        claim_fields = claim_fields.split(',')
    if disclosure_fields and len(disclosure_fields) > 0: 
        disclosure_fields = disclosure_fields.split(',')
    if interestedparty_fields and len(interestedparty_fields) > 0:
        interestedparty_fields = interestedparty_fields.split(',')
    if ipc_fields and len(ipc_fields) > 0: 
        ipc_fields = ipc_fields.split(',')
    if abstract_fields and len(abstract_fields) > 0: 
        abstract_fields = abstract_fields.split(',')

    keyargs = {'main': fields, 'claim': claim_fields, 'disclosure': disclosure_fields, 'interestedparty': interestedparty_fields, 'ipc': ipc_fields, 'abstract': abstract_fields}

    # Possibly modify to remove any whitespace, and interpret query as a comma-separated list with
    #   use for '-' character to cover ranges of patent numbers
    query = "|".join(query.split(' ')) #joining the space separated words with | for OR condition

    search_query = SearchQuery(query, search_type='raw', config='english')

    search_vector = SearchVector('patentnumber', weight='A', config='english')

    # search results
    mainrecords = pt_main.objects.annotate(
        search=search_vector,
        rank=SearchRank(search_vector, search_query)
    ).filter(search=search_query).order_by("-rank")

    dynamic_serializer_class = pt_mainSerializer(mainrecords, many=True, context=keyargs)

    serializer = dynamic_serializer_class

    # Dynamically select fields for the main serializer data - add other table fields similarly
    # if fields:
    #     serializer_data = [{field: record[field] for field in fields} for record in serializer.data]
    # else:
    #     serializer_data = serializer.data 
    
    data = {
        "Keyword": query,
        "results": serializer.data
    }
    return Response(data)

class pt_mainViewSet(WithDynamicViewSetMixin, viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for accessing pt_main entries.

    This ViewSet provides read-only access to pt_main entries.

    Attributes:
        serializer_class (rest_framework.serializers.Serializer): The serializer class used for pt_main entries.
        queryset (django.db.models.QuerySet): The queryset representing all pt_main entries.
    """
    serializer_class = pt_mainSerializer
    # queryset = pt_main.objects.all()

    def get_queryset(self):
        fullqueryset = pt_main.objects.all()
        newqueryset = pt_main.objects.none()
        patentlist = self.request.query_params.get('patentnumber', None) # assume this is either a comma-separated list or None
        
        if patentlist is not None:
            try:
                patentrange = patentlist.split(',')
                for elem in patentrange:
                    # Idea is to identify patent numbers and define queryset based on it
                    if '-' in elem:
                        # assuming elements with '-' are of the form 'X-Y' where X and Y are positive integers and X < Y
                        ranges = elem.split('-') 
                        low = ranges[0]
                        high = ranges[1]
                        
                        # implement helper to check if low or high contain characters that are not numerical
                        for num in range(int(low), int(high) + 1):
                            newqueryset = newqueryset | fullqueryset.filter(patentnumber=num)
                    else:
                        # assuming all other element types are just singular patent numbers
                        # using same helper as above, verify elem only contains numerical characters
                        newqueryset = newqueryset | fullqueryset.filter(patentnumber=int(elem))
            except (ValueError, ValidationError) as e:
                # Handle invalid input format
                return Response({'error': 'Invalid patentnumber format'}, status=400)
        
        return newqueryset

class pt_abstractViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for accessing pt_abstract entries.

    This ViewSet provides read-only access to pt_abstract entries.

    Attributes:
        serializer_class (rest_framework.serializers.Serializer): The serializer class used for pt_abstract entries.
        queryset (django.db.models.QuerySet): The queryset representing all pt_abstract entries.
    """
    serializer_class = pt_abstractSerializer
    queryset = pt_abstract.objects.all()

class pt_disclosureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for accessing pt_disclosure entries.

    This ViewSet provides read-only access to pt_disclosure entries.

    Attributes:
        serializer_class (rest_framework.serializers.Serializer): The serializer class used for pt_disclosure entries.
        queryset (django.db.models.QuerySet): The queryset representing all pt_disclosure entries.
    """
    serializer_class = pt_disclosureSerializer
    queryset = pt_disclosure.objects.all()

class pt_interested_partyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for accessing pt_interested_party entries.

    This ViewSet provides read-only access to pt_interested_party entries.

    Attributes:
        serializer_class (rest_framework.serializers.Serializer): The serializer class used for pt_interested_party entries.
        queryset (django.db.models.QuerySet): The queryset representing all pt_interested_party entries.
    """
    serializer_class = pt_interested_partySerializer
    queryset = pt_interested_party.objects.all()

class pt_ipc_classificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for accessing pt_ipc_classification entries.

    This ViewSet provides read-only access to pt_ipc_classification entries.

    Attributes:
        serializer_class (rest_framework.serializers.Serializer): The serializer class used for pt_ipc_classification entries.
        queryset (django.db.models.QuerySet): The queryset representing all pt_ipc_classification entries.
    """
    serializer_class = pt_ipc_classificationSerializer
    queryset = pt_ipc_classification.objects.all()

class pt_claimViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for accessing pt_claim entries.

    This ViewSet provides read-only access to pt_claim entries.

    Attributes:
        serializer_class (rest_framework.serializers.Serializer): The serializer class used for pt_claim entries.
        queryset (django.db.models.QuerySet): The queryset representing all pt_claim entries.
    """
    serializer_class = pt_claimSerializer
    queryset = pt_claim.objects.all()