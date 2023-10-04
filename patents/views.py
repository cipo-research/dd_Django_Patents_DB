from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import pt_main, pt_abstract, pt_disclosure, pt_interested_party, pt_ipc_classification, pt_claim
from .serializers import pt_mainSerializer, pt_abstractSerializer, pt_disclosureSerializer, pt_interested_partySerializer, pt_ipc_classificationSerializer, pt_claimSerializer
from django.db.models import Q, F, Sum
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.decorators.cache import cache_page

# Create your views here.
@method_decorator(cache_page(60 * 5), name="dispatch")
class MainList(ListView):
    model = pt_main
    context_object_name = "entries"
    template_name = "searchmain.html"

@method_decorator(cache_page(60 * 5), name="dispatch")
class AbstractList(ListView):
    model = pt_abstract
    context_object_name = "entries"
    template_name = "searchabstract.html"

@method_decorator(cache_page(60 * 5), name="dispatch")
class ClaimList(ListView):
    model = pt_claim
    context_object_name = "entries"
    template_name = "searchclaim.html"   

@method_decorator(cache_page(60 * 5), name="dispatch")
class DisclosureList(ListView):
    model = pt_disclosure
    context_object_name = "entries"
    template_name = "searchdisclosure.html"

@method_decorator(cache_page(60 * 5), name="dispatch")
class InterestedPartyList(ListView):
    model = pt_interested_party
    context_object_name = "entries"
    template_name = "searchinterestedparty.html"

@method_decorator(cache_page(60 * 5), name="dispatch")
class IPCList(ListView):
    model = pt_ipc_classification
    context_object_name = "entries"
    template_name = "searchipc.html"

@api_view(['GET'])
def pt_mainFullTextSearch(request):
    query = request.GET.get('query') # getting query from user
    fields = request.GET.get('fields') # getting fields from user
    if fields and len(fields) > 0: # fields is expected to be a comma-separated list (string)
        fields = fields.split(',')

    query = "|".join(query.split(' ')) #joining the space separated words with | for OR condition

    search_query = SearchQuery(query, search_type='raw', config='english')

    search_vector = SearchVector('patentnumber', weight='A', config='english') + SearchVector('filingdate', weight='B') + SearchVector('filingcountrycode', weight='C')

    records = pt_main.objects.annotate(
        search=search_vector,
        rank=SearchRank(search_vector, search_query)
    ).filter(search=search_query).order_by("-rank")
    
    # Dynamically generate the serializer class with user-specified fields
    if fields: # modifying serializer so that only specified fields are shown
        dynamic_serializer_class = type('pt_mainSerializer', (pt_mainSerializer,),
                                        {'Meta': type('Meta', (object,), {'model': pt_main, 'fields': fields})})
    else: # when no fields are specified, all fields will be displayed
        dynamic_serializer_class = pt_mainSerializer
    
    serializer = dynamic_serializer_class(records, many=True)
    
    data = {
        "Keyword": query,
        "results": serializer.data
    }
    return Response(data)

@api_view(['GET'])
def pt_abstractFullTextSearch(request):
    query  = request.GET.get('query')

    query = "|".join(query.split(' ')) #joining the space separated words with | for OR condition

    search_query = SearchQuery(query, search_type='raw', config='english')
    # search_vector contains information on which columns of the respective table will get searched for any query made
    search_vector = SearchVector('patentnumber', weight='A', config='english') + SearchVector('abstracttext', weight='B')

    records = pt_abstract.objects.annotate(
        search=search_vector,
        rank=SearchRank(search_vector, search_query)
    ).filter(search=search_query).order_by("-rank")
    
    serializer = pt_abstractSerializer(records, many=True)
    
    data = {
        "Keyword": query,
        "results": serializer.data
    }
    return Response(data)

@api_view(['GET'])
def pt_claimFullTextSearch(request):
    query  = request.GET.get('query')

    query = "|".join(query.split(' ')) #joining the space separated words with | for OR condition

    search_query = SearchQuery(query, search_type='raw', config='english')
    # search_vector contains information on which columns of the respective table will get searched for any query made
    search_vector = SearchVector('patentnumber', weight='A', config='english') + SearchVector('claimstext', weight='B')

    records = pt_claim.objects.annotate(
        search=search_vector,
        rank=SearchRank(search_vector, search_query)
    ).filter(search=search_query).order_by("-rank")
    
    serializer = pt_claimSerializer(records, many=True)
    
    data = {
        "Keyword": query,
        "results": serializer.data
    }
    return Response(data)

@api_view(['GET'])
def pt_disclosureFullTextSearch(request):
    query  = request.GET.get('query')

    query = "|".join(query.split(' ')) #joining the space separated words with | for OR condition

    search_query = SearchQuery(query, search_type='raw', config='english')
    # search_vector contains information on which columns of the respective table will get searched for any query made
    search_vector = SearchVector('patentnumber', weight='A', config='english') + SearchVector('disclosuretext', weight='B')

    records = pt_disclosure.objects.annotate(
        search=search_vector,
        rank=SearchRank(search_vector, search_query)
    ).filter(search=search_query).order_by("-rank")
    
    serializer = pt_disclosureSerializer(records, many=True)
    
    data = {
        "Keyword": query,
        "results": serializer.data
    }
    return Response(data)

@api_view(['GET'])
def pt_interested_partyFullTextSearch(request):
    query  = request.GET.get('query')

    query = "|".join(query.split(' ')) #joining the space separated words with | for OR condition

    search_query = SearchQuery(query, search_type='raw', config='english')
    # search_vector contains information on which columns of the respective table will get searched for any query made
    search_vector = SearchVector('patentnumber', weight='A', config='english') + SearchVector('partyname', weight='B') + SearchVector('partyprovince', weight='C')

    records = pt_interested_party.objects.annotate(
        search=search_vector,
        rank=SearchRank(search_vector, search_query)
    ).filter(search=search_query).order_by("-rank")
    
    serializer = pt_interested_partySerializer(records, many=True)
    
    data = {
        "Keyword": query,
        "results": serializer.data
    }
    return Response(data)

@api_view(['GET'])
def pt_ipc_classificationFullTextSearch(request):
    query  = request.GET.get('query')

    query = "|".join(query.split(' ')) #joining the space separated words with | for OR condition

    search_query = SearchQuery(query, search_type='raw', config='english')
    # search_vector contains information on which columns of the respective table will get searched for any query made
    search_vector = SearchVector('patentnumber', weight='A', config='english') + SearchVector('ipcclass', weight='B') + SearchVector('ipcsubclass', weight='C') + SearchVector('ipcsection', weight='D')

    records = pt_ipc_classification.objects.annotate(
        search=search_vector,
        rank=SearchRank(search_vector, search_query)
    ).filter(search=search_query).order_by("-rank")
    
    serializer = pt_ipc_classificationSerializer(records, many=True)
    
    data = {
        "Keyword": query,
        "results": serializer.data
    }
    return Response(data)

class pt_mainViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = pt_mainSerializer
    queryset = pt_main.objects.all()

class pt_abstractViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = pt_abstractSerializer
    queryset = pt_abstract.objects.all()

class pt_disclosureViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = pt_disclosureSerializer
    queryset = pt_disclosure.objects.all()

class pt_interested_partyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = pt_interested_partySerializer
    queryset = pt_interested_party.objects.all()

class pt_ipc_classificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = pt_ipc_classificationSerializer
    queryset = pt_ipc_classification.objects.all()

class pt_claimViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = pt_claimSerializer
    queryset = pt_claim.objects.all()