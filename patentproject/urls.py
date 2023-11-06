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
# from django.conf.urls import url 
from django.urls import path, re_path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from dynamic_rest.routers import DynamicRouter
from patents import views
from patents.views import DisclosureList, IPCList, InterestedPartyList, ClaimList, AbstractList, MainList, pt_mainViewSet, pt_abstractViewSet, pt_disclosureViewSet, pt_interested_partyViewSet, pt_ipc_classificationViewSet, pt_claimViewSet

# pt_main router
pt_main_router = DynamicRouter()
pt_main_router.register(
    r'pt_main',
    pt_mainViewSet
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

schema_view = get_schema_view(
    openapi.Info(
        title="Patent Database API",
        default_version='v1',
        description="Your API description",
        # terms_of_service="https://www.yourapp.com/terms/",
        # contact=openapi.Contact(email="contact@yourapp.com"),
        # license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL patterns to access different tables, and their search funtionalities
urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(pt_main_router.urls)),
    #path('mainsearchpage/', MainList.as_view(), name="mainsearch-page"),
    #path('mainsearchpage/ftsearch-main/', views.pt_mainFullTextSearch, name='searchmain'),
]
