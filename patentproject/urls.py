"""patentproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from patents import views
from patents.views import DisclosureList, IPCList, InterestedPartyList, PriorityClaimList, ClaimList, AbstractList, MainList, pt_mainViewSet, pt_priority_claimViewSet, pt_abstractViewSet, pt_disclosureViewSet, pt_interested_partyViewSet, pt_ipc_classificationViewSet, pt_claimViewSet

# pt_main router
pt_main_router = routers.SimpleRouter()
pt_main_router.register(
    r'pt_main',
    pt_mainViewSet,
    basename='pt_main',
)

# pt_abstract router
pt_abstract_router = routers.SimpleRouter()
pt_abstract_router.register(
    r'pt_abstract',
    pt_abstractViewSet,
    basename='pt_abstract',
)

# pt_disclosure router
pt_disclosure_router = routers.SimpleRouter()
pt_disclosure_router.register(
    r'pt_disclosure',
    pt_disclosureViewSet,
    basename='pt_disclosure',
)

# pt_interested_party router
pt_interested_party_router = routers.SimpleRouter()
pt_interested_party_router.register(
    r'pt_interested_party',
    pt_interested_partyViewSet,
    basename='pt_interested_party',
)

# pt_ipc_classification router
pt_ipc_classification_router = routers.SimpleRouter()
pt_ipc_classification_router.register(
    r'pt_ipc_classification',
    pt_ipc_classificationViewSet,
    basename='pt_ipc_classification',
)

# pt_claim router
pt_claim_router = routers.SimpleRouter()
pt_claim_router.register(
    r'pt_claim',
    pt_claimViewSet,
    basename='pt_claim',
)

# URL patterns to access different tables, and their search funtionalities
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(pt_main_router.urls)),
    path('api/', include(pt_priority_claim_router.urls)),
    path('api/', include(pt_abstract_router.urls)),
    path('api/', include(pt_disclosure_router.urls)),
    path('api/', include(pt_interested_party_router.urls)),
    path('api/', include(pt_ipc_classification_router.urls)),
    path('api/', include(pt_claim_router.urls)),
    path('ftsearch-main/', views.pt_mainFullTextSearch, name='searchmain'),
    path('mainsearchpage/', MainList.as_view(), name="mainsearch-page"),
    path('ftsearch-abstract/', views.pt_abstractFullTextSearch, name='searchabstract'),
    path('abstractsearchpage/', AbstractList.as_view(), name="abstractsearch-page"),
    path('ftsearch-claim/', views.pt_claimFullTextSearch, name='searchclaim'),
    path('disclosuresearchpage/', DisclosureList.as_view(), name="disclosuresearch-page"),
    path('ftsearch-disclosure/', views.pt_disclosureFullTextSearch, name='searchdisclosure'),
    path('priorityclaimsearchpage/', PriorityClaimList.as_view(), name="priorityclaimsearch-page"),
    path('ftsearch-priorityclaim/', views.pt_priority_claimFullTextSearch, name='searchpriority'),
    path('interestedpartysearchpage/', InterestedPartyList.as_view(), name="interestedpartysearch-page"),
    path('ftsearch-interestedparty/', views.pt_interested_partyFullTextSearch, name='searchinterested'),
    path('ipcsearchpage/', IPCList.as_view(), name="ipcsearch-page"),
    path('ftsearch-ipcclassification/', views.pt_ipc_classificationFullTextSearch, name='searchipc'),
]
