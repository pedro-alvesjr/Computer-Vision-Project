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

    # --- Pré-processamento ---
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, 9, 75, 75)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                  cv2.THRESH_BINARY_INV, 11, 2)

    # --- Operações morfológicas ---
    kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
    kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    
    mask = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel_rect)
    mask = cv2.dilate(mask, kernel_ellipse, iterations=2)
    
    # Preencher buracos internos
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    for i, cnt in enumerate(contours):
        if hierarchy[0][i][3] != -1:  
            cv2.drawContours(mask, [cnt], 0, 255, -1)
    
    mask = cv2.erode(mask, kernel_ellipse, iterations=2)
    mask = cv2.GaussianBlur(mask, (5,5), 0)
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

    # --- Isolar e recortar o parafuso ---
    isolado = cv2.bitwise_and(img, img, mask=mask)
    
    # Criar imagem com fundo transparente
    isolado_rgba = cv2.cvtColor(isolado, cv2.COLOR_BGR2RGBA)
    isolado_rgba[:, :, 3] = mask  

    # Recortar a região do parafuso
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        
        # Recortar a versão com transparência
        parafuso_transparente = isolado_rgba[y:y+h, x:x+w]
        
        # Recortar a versão normal para referência
        parafuso_recortado = isolado[y:y+h, x:x+w]

        # --- Salvar APENAS as imagens essenciais ---
        base_name = os.path.splitext(filename)[0]
        
        # 1. Imagem recortada com fundo transparente (MAIS IMPORTANTE)
        cv2.imwrite(os.path.join(output_folder, f"{base_name}_transparente.png"), parafuso_transparente)
        
        # 2. Imagem recortada normal (para visualização rápida)
        cv2.imwrite(os.path.join(output_folder, f"{base_name}_recortado.png"), parafuso_recortado)
        
        # 3. Máscara final (opcional, para debug)
        cv2.imwrite(os.path.join(output_folder, f"{base_name}_mascara.png"), mask)

    print(f"Processado: {filename}")

print("Processamento concluído!")