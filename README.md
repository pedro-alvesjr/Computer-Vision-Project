# Detectar Parafusos

Este projeto implementa um pipeline simples de visão computacional para detecção e isolamento automático de parafusos em imagens industriais, utilizando Python e OpenCV.

## Objetivo
Processar automaticamente um conjunto de imagens contendo um parafuso em fundo controlado, segmentando o objeto e gerando imagens binárias e isoladas para análise posterior.

## Tecnologias utilizadas
- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/)

## Estrutura de pastas

COMPUTER VISION PROJECT/
│
├─ imagens/ # Conjunto de imagens originais (320 no dataset)
├─ resultados/ # Resultados gerados automaticamente
├─ detectar_parafusos.py # Script principal
└─ README.md # Documentação do projeto

## Como executar
1. Clone este repositório ou baixe os arquivos.  
2. Instale as dependências necessárias:
    pip install opencv-python
3. Coloque as imagens a serem processadas na pasta imagens/.
4. Execute o script no terminal:
    python detectar_parafusos.py
5. Os resultados serão salvos automaticamente na pasta resultados/.

## Saída

Para cada imagem, são gerados:

_transparente.png → Parafuso recortado com fundo transparente
_recortado.png → Parafuso recortado com fundo preto
_mascara.png → Máscara binária final do parafuso

## Notas importantes

O pipeline utiliza:

Conversão para escala de cinza e suavização com filtro bilateral.

Binarização adaptativa (Adaptive Gaussian Threshold).

Operações morfológicas para remover ruídos e preencher buracos internos.

Extração da maior componente conectada (parafuso).

Recorte e exportação com canal alfa (transparência).

Caso a pasta resultados/ já exista, os arquivos podem ser sobrescritos.

A abordagem é baseada em técnicas clássicas de visão computacional, sem uso de redes neurais, garantindo execução rápida e simples em qualquer máquina local.