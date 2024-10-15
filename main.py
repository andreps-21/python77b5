import cv2
import numpy as np
import sys
from numpy.linalg import inv
from cubo import selecionar_cubo


while True:
    print("""
        +--------------------------------------+
        |         Selecione uma Opção          |
        +--------------------------------------+
        | [1] Seleção cuboide                  |
        | [2] Seleção esférica                 |
        | [3] Distância de Mahalanobis         |
        | [4] Distância K-Vizinhos             |
        | [5] Sair do programa                  |
        +--------------------------------------+
    """)
    
    opcao = int(input("Digite a opção escolhida: "))
    
    if opcao == 1:
        selecionar_cubo()
    elif opcao == 2:
        selecionar_esfera()
    elif opcao == 3:
        selecionar_mahalanobis()
    elif opcao == 4:
        selecionar_kvizinho()
    elif opcao == 5:
        print("Saindo do programa...")
        sys.exit()
    else:
        print("Opção inválida. Tente novamente.")
