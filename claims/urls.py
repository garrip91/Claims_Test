from django.urls import path, include
from rest_framework.routers import DefaultRouter

from claims.views import ClaimCreateView, SuccessView, ClaimListCreateAPIView, ClaimViewSet


router = DefaultRouter()
router.register(r'claims', ClaimViewSet)

urlpatterns = [
    path('create/', ClaimCreateView.as_view(), name='claim-create'),
    path('success/', SuccessView.as_view(), name='success'),
    path('api/claim/', ClaimListCreateAPIView.as_view(), name='api_list_create_claim'),
    path('api/v1/', include(router.urls)),
]
