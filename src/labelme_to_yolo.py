import json
import os

# ==============================
# CONFIGURAÇÕES
# ==============================
CLASSES = {
    "painel_solar": 0  # nome EXATO da classe no LabelMe
}

INPUT_DIR = "data/raw"
OUTPUT_DIR = "data/labels_yolo"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================
# CONVERSÃO
# ==============================
for file in os.listdir(INPUT_DIR):
    if not file.endswith(".json"):
        continue

    json_path = os.path.join(INPUT_DIR, file)

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    img_w = data["imageWidth"]
    img_h = data["imageHeight"]

    yolo_lines = []

    for shape in data["shapes"]:
        label = shape["label"]

        if label not in CLASSES:
            continue

        points = shape["points"]

        # 🔹 POLÍGONO → BOUNDING BOX
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]

        x_min = min(x_coords)
        x_max = max(x_coords)
        y_min = min(y_coords)
        y_max = max(y_coords)

        # 🔹 CONVERSÃO PARA YOLO
        x_center = ((x_min + x_max) / 2) / img_w
        y_center = ((y_min + y_max) / 2) / img_h
        width = (x_max - x_min) / img_w
        height = (y_max - y_min) / img_h

        class_id = CLASSES[label]

        yolo_lines.append(
            f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"
        )

    txt_name = file.replace(".json", ".txt")
    txt_path = os.path.join(OUTPUT_DIR, txt_name)

    with open(txt_path, "w") as f:
        f.write("\n".join(yolo_lines))

print("✅ Conversão LabelMe (polígono) → YOLO concluída com sucesso!")
