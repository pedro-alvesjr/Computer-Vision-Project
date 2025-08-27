import cv2
import numpy as np
import os

# --- Criar pasta para resultados ---
os.makedirs("resultados", exist_ok=True)

# --- Pasta com as imagens ---
input_folder = "imagens"
output_folder = "resultados"

# --- Percorrer todas as imagens ---
for filename in os.listdir(input_folder):
    if not (filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg")):
        continue

    img_path = os.path.join(input_folder, filename)
    img = cv2.imread(img_path)

    if img is None:
        print(f"Erro ao ler {filename}. Pulando...")
        continue

    # --- Pré Processamento da imagem ---
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print(f"Nenhum contorno encontrado em {filename}. Pulando...")
        continue

    cnt = max(contours, key=cv2.contourArea)
    mask = np.zeros_like(gray)
    cv2.drawContours(mask, [cnt], -1, 255, -1)
    isolado = cv2.bitwise_and(img, img, mask=mask)

    # --- Salvar resultados ---
    base_name = os.path.splitext(filename)[0]

    files_to_save = {
        f"{base_name}_original.png": img,
        f"{base_name}_bordas.png": edges,
        f"{base_name}_threshold.png": thresh,
        f"{base_name}_mascara.png": mask,
        f"{base_name}_parafuso_isolado.png": isolado
    }

    for out_name, data in files_to_save.items():
        out_path = os.path.join(output_folder, out_name)
        if not os.path.exists(out_path): 
            cv2.imwrite(out_path, data)

    print(f"Processado: {filename}")
