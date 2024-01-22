# Geração Procedural de Mapas para Jogos Através de Técnicas de Segmentação de Imagem

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Lds20k/senac-tcc/blob/main/README.md)

**Trabalho de Conclusão de Curso | Bacharelado em Ciência da Computação - Senac**

**Autores:**
- Lucas da Silva Santos
- Matheus Zanivan Andrade
- Rafael Nascimento Lourenço

## Requisitos do Sistema
* Debian

## Instalação

### UnityHub
```sh
su
## Inserir sua senha root ##

# Adicionar o certificado do repositório do Unity #
wget -qO - https://hub.unity3d.com/linux/keys/public | gpg --dearmor | sudo tee /usr/share/keyrings/Unity_Technologies_ApS.gpg > /dev/null

#  Adicionar o repositório do Unity #
sh -c 'echo "deb [signed-by=/usr/share/keyrings/Unity_Technologies_ApS.gpg] https://hub.unity3d.com/linux/repos/deb stable main" > /etc/apt/sources.list.d/unityhub.list'

# Atualizar a informações dos pacotes de todas as fontes #
apt update

# Instalar o UnityHub #
apt-get install unityhub
```

### Miniconda
```sh
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

### EfficientPS
```sh
conda env create -n senac-tcc --file=environment.yml
conda activate senac-tcc
conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=10.2 cudatoolkit-dev -c pytorch -c conda-forge
pip install -r requirements.txt

cd src/efficientNet
python setup.py develop

cd ..
python setup.py develop
```