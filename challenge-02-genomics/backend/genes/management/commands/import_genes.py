import json
import csv
from django.core.management.base import BaseCommand
from genes.models import Gene


class Command(BaseCommand):
    help = 'Importa dados de genes dos arquivos siteA.txt e siteB.txt'

    def add_arguments(self, parser):
        parser.add_argument(
            '--siteA',
            type=str,
            default='siteA.txt',
            help='Caminho para o arquivo siteA.txt (TSV)'
        )
        parser.add_argument(
            '--siteB',
            type=str,
            default='siteB.txt',
            help='Caminho para o arquivo siteB.txt (JSON)'
        )

    def handle(self, *args, **options):
        site_a_path = options['siteA']
        site_b_path = options['siteB']

        self.stdout.write(self.style.SUCCESS('Iniciando importação de genes...'))

        # Carregar dados do siteB (JSON) em memória
        self.stdout.write('Carregando siteB.txt (JSON)...')
        try:
            with open(site_b_path, 'r', encoding='utf-8') as f:
                site_b_data = json.load(f)

            # Criar dicionário indexado por ncbiGeneID para busca rápida
            site_b_dict = {}
            if isinstance(site_b_data, list):
                for item in site_b_data:
                    ncbi_id = item.get('ncbiGeneID')
                    if ncbi_id:
                        site_b_dict[str(ncbi_id)] = item
            elif isinstance(site_b_data, dict):
                site_b_dict = site_b_data

            self.stdout.write(self.style.SUCCESS(f'✓ {len(site_b_dict)} registros carregados do siteB'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Arquivo {site_b_path} não encontrado!'))
            return
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(f'Erro ao decodificar JSON: {e}'))
            return

        # Processar siteA (TSV) e fazer o JOIN
        self.stdout.write('Processando siteA.txt (TSV) e realizando JOIN...')
        genes_to_create = []
        matched_count = 0
        unmatched_count = 0

        try:
            with open(site_a_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter='\t')

                for row in reader:
                    entrez_gene_id = row.get('Entrez Gene ID (NCBI)', '').strip()
                    mim_number = row.get('MIM Number', '').strip()

                    if not entrez_gene_id:
                        continue

                    # Buscar correspondência no siteB
                    site_b_match = site_b_dict.get(entrez_gene_id)

                    if site_b_match:
                        matched_count += 1

                        # Extrair dados do siteB
                        approved_name = site_b_match.get('approvedName', '')
                        symbol = site_b_match.get('approvedSymbol', '')

                        # Converter MIM Number para inteiro (se existir)
                        mim_int = None
                        if mim_number and mim_number.isdigit():
                            mim_int = int(mim_number)

                        # Criar objeto Gene
                        gene = Gene(
                            entrez_gene_id=int(entrez_gene_id),
                            mim_number=mim_int,
                            approved_name=approved_name,
                            symbol=symbol
                        )
                        genes_to_create.append(gene)

                        # Log de progresso a cada 100 registros
                        if matched_count % 100 == 0:
                            self.stdout.write(f'  Processados: {matched_count} matches...')
                    else:
                        unmatched_count += 1

            self.stdout.write(self.style.SUCCESS(f'✓ Processamento concluído'))
            self.stdout.write(f'  Matches encontrados: {matched_count}')
            self.stdout.write(f'  Sem match: {unmatched_count}')

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Arquivo {site_a_path} não encontrado!'))
            return
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao processar siteA: {e}'))
            return

        # Salvar no banco de dados usando bulk_create
        if genes_to_create:
            self.stdout.write('Salvando genes no banco de dados...')
            try:
                # Limpar dados existentes (opcional)
                Gene.objects.all().delete()

                # Bulk create para eficiência
                Gene.objects.bulk_create(genes_to_create, batch_size=500, ignore_conflicts=True)

                total_saved = Gene.objects.count()
                self.stdout.write(self.style.SUCCESS(f'✓ {total_saved} genes salvos com sucesso!'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Erro ao salvar no banco: {e}'))
        else:
            self.stdout.write(self.style.WARNING('Nenhum gene para salvar.'))

        self.stdout.write(self.style.SUCCESS('Importação concluída!'))
