import cv2

def ver():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()

    if ret:
        cv2.imwrite("vision/ultima_imagen.jpg", frame)
        return "Imagen capturada"
    else:
        return "No se pudo acceder a la cámara"
