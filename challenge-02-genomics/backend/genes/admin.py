from django.contrib import admin
from .models import Gene


@admin.register(Gene)
class GeneAdmin(admin.ModelAdmin):
    list_display = ['entrez_gene_id', 'symbol', 'approved_name', 'mim_number', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['symbol', 'approved_name', 'entrez_gene_id']
    ordering = ['entrez_gene_id']
