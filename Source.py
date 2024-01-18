import os
import glob
import shutil
from datetime import datetime

def criar_pasta_subpasta_por_nomes_e_meses(path, extensoes, meses_desejados):
    # Encontrar todos os arquivos no diretório com as extensões especificadas
    files = []
    for extensao in extensoes:
        files.extend(glob.glob(os.path.join(path, f"*.{extensao}")))

    # Iterar sobre os arquivos
    for arquivo in files:
        # Obter a data de modificação do arquivo
        data_modificacao = datetime.fromtimestamp(os.path.getmtime(arquivo))

        # Verificar se o mês da modificação está na lista de meses desejados
        if data_modificacao.month in meses_desejados:
            # Criar subpastas correspondentes ao ano e mês se não existirem
            ano_subpasta = str(data_modificacao.year)
            mes_subpasta = str(data_modificacao.month).zfill(2)  # Adiciona zero à esquerda para garantir dois dígitos

            pasta_ano = os.path.join(path, ano_subpasta)
            os.makedirs(pasta_ano, exist_ok=True)

            pasta_mes = os.path.join(pasta_ano, mes_subpasta)
            os.makedirs(pasta_mes, exist_ok=True)

            # Mover o arquivo para a subpasta correspondente ao ano e mês
            shutil.move(arquivo, pasta_mes)

# Exemplo de uso
caminho_diretorio = r"C:\Users\diogo.silva\Desktop\TesteFluxo"
extensoes_desejadas = ["txt", "csv", "xlsx", "pdf", "docx"]  # Adicione ou remova as extensões conforme necessário
meses_desejados = [7, 8, 9, 10, 11, 12]  # Adicione os meses desejados
criar_pasta_subpasta_por_nomes_e_meses(caminho_diretorio, extensoes_desejadas, meses_desejados)
