from rest_framework import serializers
from .models import Gene


class GeneSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Gene.
    """
    class Meta:
        model = Gene
        fields = ['id', 'approved_name', 'entrez_gene_id', 'mim_number', 'symbol', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
