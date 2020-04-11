import dlib
import cv2
import numpy as np

def imprimePontos(imagem, pontosFaciais):
    for p in pontosFaciais.parts():
        cv2.circle(imagem, (p.x, p.y), 2, (0, 255, 0), 2)

def imprimeNumero(imagem, pontosFaciais):
    for i, p in enumerate(pontosFaciais.parts()):
        cv2.putText(imagem, str(i), (p.x, p.y), fonte, .55, (0, 0, 255), 1)

def imprimeLinha(imagem, pontosFaciais):
    p68 = [[0, 16, False],
            [17, 21, False],
            [22, 26, False],
            [27, 30, False],
            [30, 35, True],
            [36, 41, True],
            [42, 47, True],
            [48, 59, True],
            [60, 67, True]]
    for k in range(0, len(p68)):
        pontos = []
        for i in range(p68[k][0], p68[k][1] + 1):
            ponto = [pontosFaciais.part(i).x, pontosFaciais.part(i).y]
            pontos.append(ponto)
        pontos = np.array(pontos, dtype=np.int32)
        cv2.polylines(imagem, [pontos], p68[k][2], (255, 0, 0), 2)


fonte = cv2.FONT_HERSHEY_COMPLEX_SMALL
imagem = cv2.imread("fotos/treinamento/ronald.0.1.jpg")
detectorFace = dlib.get_frontal_face_detector()
detectorPontos = dlib.shape_predictor("recursos/shape_predictor_68_face_landmarks.dat")
facesDetectadas = detectorFace(imagem, 2)
for face in facesDetectadas:
    pontos = detectorPontos(imagem, face)
    print(pontos.parts())
    imprimePontos(imagem, pontos)
    #imprimeNumero(imagem, pontos)
    #imprimeLinha(imagem, pontos)

cv2.imshow("Pontos faciais", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()