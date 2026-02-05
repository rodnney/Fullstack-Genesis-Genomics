from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Gene
from .serializers import GeneSerializer


class GeneViewSet(viewsets.ModelViewSet):
    """
    ViewSet para operações CRUD em genes.
    Permite filtrar por mim_number (min e max).
    """
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['mim_number', 'symbol']
    search_fields = ['approved_name', 'symbol']
    ordering_fields = ['entrez_gene_id', 'mim_number', 'symbol']
    ordering = ['entrez_gene_id']

    def get_queryset(self):
        """
        Permite filtrar por intervalo de MIM Number.
        """
        queryset = super().get_queryset()

        mim_min = self.request.query_params.get('mim_min', None)
        mim_max = self.request.query_params.get('mim_max', None)

        if mim_min is not None:
            queryset = queryset.filter(mim_number__gte=mim_min)
        if mim_max is not None:
            queryset = queryset.filter(mim_number__lte=mim_max)

        return queryset
