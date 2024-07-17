import os
from cryptography.fernet import Fernet 

files = []

# Abra o arquivo que contém a chave secreta
with open("chave.key", "rb") as key_file:
    secretkey = key_file.read()

# Itera sobre os arquivos no diretório atual
for file in os.listdir():
    if file in ["madara.py", "LICENSE", ".gitattributes", "README.md", "chave.key", "desc.py"]:
        continue
    if os.path.isfile(file):
        files.append(file)

# Descriptografa os arquivos listados
for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_decrypted = Fernet(secretkey).decrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_decrypted)
