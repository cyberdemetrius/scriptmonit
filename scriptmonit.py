# Monitor de Integridade de Arquivos para Analisar um Diretório no Linux

import os
import time
from datetime import datetime  # Importa a biblioteca para manipular datas e horas

# Função para comparar arquivos no diretório
def comparar_arquivos(diretorio, timestamps):
    for arquivo in os.listdir(diretorio):
        if arquivo.startswith(".") or arquivo == "scriptmonit.py": # Aqui, não monitoramos arquivos ocultos e o próprio script
            continue
        
        caminho_arquivo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_arquivo):
            if arquivo in timestamps:
                modificado = os.path.getmtime(caminho_arquivo)
                if modificado != timestamps[arquivo]:
                    timestamps[arquivo] = modificado
                    data_modificacao = datetime.fromtimestamp(modificado).strftime("%Y-%m-%d %H:%M:%S")
                    print(f"O arquivo {arquivo} foi modificado em {data_modificacao}.")
                    
# Função principal para monitorar os arquivos no diretório
def monitorar(diretorio):
    timestamps = {arquivo: None for arquivo in os.listdir(diretorio) if not arquivo.startswith(".")}
    
    while True:
        comparar_arquivos(diretorio, timestamps)
        time.sleep(5)

# Execução do programa ao ser chamado diretamente
if __name__ == "__main__":
    diretorio_monitorado = "/home/dvfernandes/myproptools/MIA_tool"
    monitorar(diretorio_monitorado)
