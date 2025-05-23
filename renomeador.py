import os
os.system

def renomear_arquivos(pasta, novo_nome):
    arquivos = os.listdir(pasta)
    arquivos.sort()
    for i, nome_original in enumerate(arquivos):
        caminho_antigo = os.path.join(pasta, nome_original)

        if os.path.isfile(caminho_antigo):
            extensao = os.path.splitext(nome_original)[1]
            novo_nome_completo = f"{novo_nome}_{i+1:03d}{extensao}"
            caminho_novo = os.path.join(pasta, novo_nome_completo)
            os.rename(caminho_antigo, caminho_novo)
            print(f'Renomeado: {nome_original} -> {novo_nome_completo}')

if __name__ == "__main__":
    pasta = input("Caminho da pasta: ").strip()
    nome_base = input("Novo nome base: ").strip()
    renomear_arquivos(pasta, nome_base)
