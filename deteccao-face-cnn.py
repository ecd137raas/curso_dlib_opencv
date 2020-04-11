import dlib

imagem = cv2.imread("fotos/grupo.0.jpg")
detector = dlib
facesDetectadas = detector(imagem)
print(facesDetectadas)

cv2.imshow("Detector CNN", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

