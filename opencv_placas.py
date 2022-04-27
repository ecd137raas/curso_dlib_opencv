import cv2

# carrega a imagem
image = cv2.imread('./recursos/Placas/carro1.jpg')

# converte em imagem cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# imagem em escala de branco
_, bin = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)

# desfocar a imagem
blur = cv2.GaussianBlur(bin, (5, 5), 0)

# procurar contorno
contour, hier = cv2.findContours(
    blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# pintar os contornos
#cv2.drawContours(image, contour, -1, (0, 255, 0), 2)

for c in contour:
    perimeter = cv2.arcLength(c, True)

    if perimeter > 120:
        aprox = cv2.approxPolyDP(c, 0.03 * perimeter, True)
        if len(aprox) == 4:
            (x, y, alt, lar) = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x+alt, y+lar), (0, 255, 0), 2)
            roi = image[y:y + lar, x:x + alt]
            cv2.imwrite('./recursos/Placas/placa.jpg', roi)

cv2.waitKey()
cv2.destroyAllWindows()
