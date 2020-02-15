import cv2
import dlib

imagem = cv2.imread("fotos/grupo.0.jpg")
detector = dlib.get_frontal_face_detector()
facesDetectadas = detector(imagem, 4)
#parametro que conforme mais alto, ele apura em imagens menores

print(facesDetectadas)
for faces in facesDetectadas:
    e, t, d, b = (int(faces.left()), int(faces.top()), int(faces.right()), int(faces.bottom()))
    cv2.rectangle(imagem, (e, t), (d, b), (0, 255, 255), 2)

cv2.imshow("Detectar Hog", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
