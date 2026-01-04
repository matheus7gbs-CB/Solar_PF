import cv2
import os

# ==============================
# CONFIGURAÇÕES
# ==============================
IMAGE_DIR = "data/raw"
LABEL_DIR = "data/labels_yolo"

# Tamanho máximo da janela (apenas visualização)
MAX_WIDTH = 1200
MAX_HEIGHT = 800

print("🔍 Iniciando validação visual YOLO...\n")

# ==============================
# LOOP NAS IMAGENS
# ==============================
for img_name in os.listdir(IMAGE_DIR):

    # Aceita jpg, jpeg e png
    if not img_name.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    img_path = os.path.join(IMAGE_DIR, img_name)
    label_path = os.path.join(
        LABEL_DIR, os.path.splitext(img_name)[0] + ".txt"
    )

    if not os.path.exists(label_path):
        print(f"⚠️ Label YOLO não encontrado para {img_name}")
        continue

    print(f"✅ Visualizando {img_name}")

    # ==============================
    # LEITURA DA IMAGEM
    # ==============================
    img = cv2.imread(img_path)
    if img is None:
        print(f"❌ Erro ao carregar {img_name}")
        continue

    h, w, _ = img.shape
    print(f"   Resolução original: {w}x{h}")

    # ==============================
    # LEITURA DO LABEL YOLO
    # ==============================
    with open(label_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        if len(parts) != 5:
            continue

        cls, xc, yc, bw, bh = map(float, parts)

        # YOLO → pixels
        x1 = int((xc - bw / 2) * w)
        y1 = int((yc - bh / 2) * h)
        x2 = int((xc + bw / 2) * w)
        y2 = int((yc + bh / 2) * h)

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # ==============================
    # REDIMENSIONAMENTO (VISUAL)
    # ==============================
    scale = min(
        MAX_WIDTH / w,
        MAX_HEIGHT / h,
        1.0  # nunca aumenta, só reduz
    )

    new_w = int(w * scale)
    new_h = int(h * scale)

    img_resized = cv2.resize(img, (new_w, new_h))

    # ==============================
    # EXIBIÇÃO
    # ==============================
    cv2.imshow("YOLO - Validação Visual", img_resized)
    print("👉 Pressione qualquer tecla para a próxima imagem\n")
    cv2.waitKey(0)

cv2.destroyAllWindows()
print("🏁 Validação visual finalizada com sucesso!")
