import cv2
import numpy as np

def selecionar_kvizinho():
    print("Digite o nome e a extensão da imagem que deseja abrir para editar.")
    read = input("Nome da imagem: ")
    img = cv2.imread(read)
    altura, largura, _ = img.shape

    pontos = []

    def pegar_cor(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            color = img[y, x]
            pontos.append(tuple(color))
            print(f"Ponto adicionado: {color}")

    cv2.imshow("Imagem", img)
    cv2.setMouseCallback("Imagem", pegar_cor)
    cv2.waitKey(0)

    nponto = int(input("Quantos pontos você deseja introduzir? "))
    raiooo = float(input("Qual o tamanho do raio que deseja? "))

    for cor in pontos:
        for i in range(altura):
            for j in range(largura):
                dist = np.linalg.norm(img[i, j] - cor)
                if dist < raiooo:
                    img[i, j] = [255, 255, 255]

    write = input("Como você gostaria de chamar esta imagem? ")
    cv2.imwrite(write, img)
    print("Imagem salva com sucesso!")

    if input("Deseja visualizar a imagem agora? [Y] [N]: ").strip().upper() == "Y":
        cv2.imshow("Imagem", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
