import cv2

def probar_camara():
    """
    Abre la cámara unos segundos para verificar que funciona.
    Presiona 'q' para salir.
    """

    camara = cv2.VideoCapture(0)

    if not camara.isOpened():
        print("❌ No se pudo abrir la cámara")
        return

    print("📷 Cámara activa. Presiona 'q' para salir.")

    while True:
        ret, frame = camara.read()
        if not ret:
            break

        cv2.imshow("ATLAS - Cámara", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camara.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    probar_camara()
