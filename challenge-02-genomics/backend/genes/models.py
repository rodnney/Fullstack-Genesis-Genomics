from django.db import models


class Gene(models.Model):
    """
    Modelo para armazenar informações de genes.
    """
    approved_name = models.CharField(max_length=500, verbose_name="Nome Aprovado")
    entrez_gene_id = models.BigIntegerField(unique=True, verbose_name="Entrez Gene ID")
    mim_number = models.IntegerField(null=True, blank=True, verbose_name="MIM Number")
    symbol = models.CharField(max_length=100, verbose_name="Símbolo")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'genes'
        ordering = ['entrez_gene_id']
        verbose_name = 'Gene'
        verbose_name_plural = 'Genes'

    def __str__(self):
        return f"{self.symbol} ({self.entrez_gene_id})"
