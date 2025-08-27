# Detectar Parafusos

Este projeto implementa um pipeline simples de visão computacional para detecção e isolamento automático de parafusos em imagens industriais, utilizando Python e OpenCV.

## Objetivo
Processar automaticamente um conjunto de imagens contendo um parafuso em fundo controlado, segmentando o objeto e gerando imagens binárias e isoladas para análise posterior.

## Tecnologias utilizadas
- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)

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
    pip install opencv-python numpy
3. Coloque as imagens a serem processadas na pasta imagens/.
4. Execute o script no terminal:
    python detectar_parafusos.py
5. Os resultados serão salvos automaticamente na pasta resultados/.

## Saída

Para cada imagem, são gerados:

_original.png → Imagem original
_bordas.png → Detecção de bordas (Canny)
_threshold.png → Binarização com Otsu
_mascara.png → Máscara binária do parafuso
_parafuso_isolado.png → Parafuso isolado

## Notas

- O algoritmo utiliza Canny para detecção de bordas e Otsu para binarização automática.

- Caso a pasta resultados já contenha uma saída, o script não sobrescreve os arquivos.

- A abordagem é baseada em técnicas clássicas de visão computacional, sem uso de redes neurais, garantindo execução simples em ambiente local.