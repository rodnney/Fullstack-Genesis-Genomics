from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Gene


class GeneModelTest(TestCase):
    """Testes para o modelo Gene"""

    def setUp(self):
        self.gene = Gene.objects.create(
            approved_name="Test Gene",
            entrez_gene_id=999999,
            mim_number=123456,
            symbol="TEST"
        )

    def test_gene_creation(self):
        """Testa criação de gene"""
        self.assertEqual(self.gene.symbol, "TEST")
        self.assertEqual(self.gene.entrez_gene_id, 999999)
        self.assertEqual(self.gene.mim_number, 123456)

    def test_gene_str(self):
        """Testa representação string do gene"""
        self.assertEqual(str(self.gene), "TEST (999999)")

    def test_unique_entrez_gene_id(self):
        """Testa unicidade do entrez_gene_id"""
        with self.assertRaises(Exception):
            Gene.objects.create(
                approved_name="Duplicate Gene",
                entrez_gene_id=999999,  # Duplicado
                mim_number=654321,
                symbol="DUP"
            )


class GeneAPITest(APITestCase):
    """Testes para a API de genes"""

    def setUp(self):
        self.gene1 = Gene.objects.create(
            approved_name="Gene 1",
            entrez_gene_id=100001,
            mim_number=100000,
            symbol="GENE1"
        )
        self.gene2 = Gene.objects.create(
            approved_name="Gene 2",
            entrez_gene_id=100002,
            mim_number=200000,
            symbol="GENE2"
        )

    def test_list_genes(self):
        """Testa listagem de genes"""
        response = self.client.get('/api/genes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_get_gene_detail(self):
        """Testa obtenção de detalhes de um gene"""
        response = self.client.get(f'/api/genes/{self.gene1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['symbol'], 'GENE1')

    def test_create_gene(self):
        """Testa criação de gene via API"""
        data = {
            'approved_name': 'New Gene',
            'entrez_gene_id': 100003,
            'mim_number': 300000,
            'symbol': 'NEW'
        }
        response = self.client.post('/api/genes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Gene.objects.count(), 3)

    def test_update_gene(self):
        """Testa atualização de gene"""
        data = {
            'approved_name': 'Updated Gene',
            'entrez_gene_id': 100001,
            'mim_number': 100000,
            'symbol': 'UPDATED'
        }
        response = self.client.put(f'/api/genes/{self.gene1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.gene1.refresh_from_db()
        self.assertEqual(self.gene1.symbol, 'UPDATED')

    def test_delete_gene(self):
        """Testa deleção de gene"""
        response = self.client.delete(f'/api/genes/{self.gene1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Gene.objects.count(), 1)

    def test_filter_by_mim_range(self):
        """Testa filtro por intervalo de MIM Number"""
        response = self.client.get('/api/genes/?mim_min=150000&mim_max=250000')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['symbol'], 'GENE2')

    def test_search_by_symbol(self):
        """Testa busca por símbolo"""
        response = self.client.get('/api/genes/?search=GENE1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['symbol'], 'GENE1')

    def test_ordering(self):
        """Testa ordenação"""
        response = self.client.get('/api/genes/?ordering=-mim_number')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        self.assertEqual(results[0]['symbol'], 'GENE2')
        self.assertEqual(results[1]['symbol'], 'GENE1')
