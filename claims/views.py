from rest_framework.generics import ListCreateAPIView
from django.views.generic import TemplateView, CreateView
from rest_framework import viewsets, mixins

from claims.forms import ClaimCreateForm
from claims.serializers import ClaimSerializer
from claims.models import Claim


class ClaimCreateView(CreateView):
    template_name = 'claims/claim_create.html'
    success_url = '/claims/success/'
    form_class = ClaimCreateForm

    def get_success_url(self):
        return '/claims/success/?claim_id=' + str(self.object.id)


class SuccessView(TemplateView):
    template_name = 'claims/success.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['claim_id'] = self.request.GET.get('claim_id', 0)
        return data


class ClaimListCreateAPIView(ListCreateAPIView):
    serializer_class = ClaimSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Claim.objects.all()
            return queryset
        return []


class ClaimViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """Заявки"""

    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer