import cv2
import numpy as np
from numpy.linalg import inv

def selecionar_mahalanobis():
    print("Digite o nome e a extensão da imagem que deseja abrir para editar.")
    print("Exemplo: imagem.jpg ")
    read= input("Nome da imagem: ")
    img = cv2.imread(read)


    altura=img.shape[0]
    largura=img.shape[1]
    canais=img.shape[2]




    m=[0]*3
    w=int(0)
    nponto = int(input("Quantos pontos você deseja introduzir? "))
    raiooo = float(input("Qual o tamanho do raio que deseja? "))
    vred=[0]*nponto
    vgreen=[0]*nponto
    vblue=[0]*nponto


    for w in range(nponto):
        pred=input("Digite o ponto nº: "+str(w)+" [RED] ")
        pgreen=input("Digite o ponto nº: "+str(w)+" [GREEN] ")
        pblue=input("Digite o ponto nº: "+str(w)+" [BLUE] ")
        vred[w]=float(pred)
        vgreen[w]=float(pgreen)
        vblue[w]=float(pblue)
        m[0] = float(m[0])+float(vred[w])
        m[1] = float(m[1])+float(vgreen[w])
        m[2] = float(m[2])+float(vblue[w])
                
    m[0] = m[0] / float(nponto)
    m[1] = m[1] / float(nponto)
    m[2] = m[2] / float(nponto)


    m_cov=np.zeros((3,3), dtype=np.float64)
    z=int(0)
    for z in range(nponto):
        m_cov[0,0]= ((vred[z]-m[0])*(vred[z]-m[0])) + m_cov[0,0]
        m_cov[1,0]= ((vred[z]-m[0])*(vgreen[z]-m[1])) + m_cov[1,0]
        m_cov[2,0]= ((vred[z]-m[0])*(vblue[z]-m[2])) + m_cov[2,0]
        m_cov[2,1]= ((vgreen[z]-m[1])*(vblue[z]-m[2])) + m_cov[2,1]
        m_cov[1,1]= ((vgreen[z]-m[1])*(vgreen[z]-m[1])) + m_cov[1,1]
        m_cov[2,2]= ((vblue[z]-m[2])*(vblue[z]-m[2])) + m_cov[2,2]


    m_cov[0,2]= m_cov[2,0]
    m_cov[1,2]= m_cov[2,1]
    m_cov[0,1]= m_cov[1,0] 


    n=float(nponto)
    i = int(0)
    j = int(0)
    for i in range(2):
        for j in range(2):
            m_cov[i,j]= (m_cov[i,j] / n)
    i_cov = inv(m_cov)
    vet=[0]*3
    for g in range(altura):
        for f in range(largura):
            vet[0]=float(img[g,f,2])-float(m[0])
            vet[1]=float(img[g,f,1])-float(m[1])
            vet[2]=float(img[g,f,0])-float(m[2])
            tvet=np.transpose(vet)
            aux = np.dot(i_cov,vet)
            dist=np.dot(tvet,aux)
            d=float(dist)
            if(d < raiooo):
                #print("D: ",d)
                img[g,f,2] = 255
                img[g,f,1] = 255
                img[g,f,0] = 255






    print("Como você gostaria de chamar esta imagem?")
    print("Exemplo: Editada.jpg")
    write = input("Nome da imagem: ")			


    cv2.imwrite(write,img)
    print("Imagem salva com sucesso!")	


    resposta=input("Deseja visualizar a imagem agora? [Y] [N] : ")
    if (resposta == "Y" or resposta=="y"):
        print("Digite qualquer tecla para fechar.")
        cv2.imshow("Exibição da Imagem",img)
        cv2.waitKey()
        cv2.destroyAllWindows()