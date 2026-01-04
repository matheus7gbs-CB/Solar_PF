# ☀️ Solar_PF  
**Detecção automática de painéis solares em imagens aéreas utilizando YOLO**

---

## 📌 Descrição do Projeto
Este repositório apresenta o desenvolvimento de um sistema de **visão computacional para detecção de painéis solares fotovoltaicos** em imagens, utilizando redes neurais convolucionais baseadas na arquitetura **YOLO (You Only Look Once)**.

O projeto possui caráter **acadêmico e experimental**, com foco em organização de dados, treinamento de modelos de detecção de objetos, avaliação de desempenho e reprodutibilidade científica.

---

## 🎯 Objetivos
- Desenvolver um modelo capaz de identificar painéis solares em imagens
- Avaliar métricas de desempenho como *precision*, *recall* e *mAP*
- Construir um pipeline reprodutível de treinamento e inferência
- Disponibilizar o código-fonte de forma clara e documentada

---

## 🧠 Metodologia

### 1. Coleta de Dados
Imagens de áreas urbanas contendo instalações fotovoltaicas foram utilizadas como base do estudo.

### 2. Anotação
As imagens foram anotadas no formato YOLO utilizando ferramentas como **LabelImg** ou **LabelMe**.

### 3. Pré-processamento
Conversão e organização das anotações para o padrão YOLO, garantindo compatibilidade com o framework Ultralytics.

### 4. Treinamento
Treinamento do modelo **YOLO11n** com ajuste de hiperparâmetros adequados ao problema.

### 5. Inferência e Avaliação
Avaliação qualitativa e quantitativa em imagens não vistas durante o treinamento.

---

## 🗂 Estrutura do Repositório

```text
Solar_PF/
│
├── data/
│   ├── dataset/
│   │   ├── images/        # Imagens anotadas (ignorado no Git)
│   │   ├── labels/        # Labels YOLO (ignorado no Git)
│   │   └── data.yaml      # Configuração do dataset
│   ├── raw/               # Imagens brutas (ignorado)
│
├── runs/
│   └── detect/            # Resultados de treino e inferência (ignorado)
│
├── src/
│   ├── labelme_to_yolo.py # Conversão de anotações
│   └── visualizar_yolo.py # Visualização de bounding boxes
│
├── .gitignore
├── dataset_description.md
├── README.md
├── LICENSE
```

### ⚙️ Tecnologias Utilizadas

### Python 3.10+
### Ultralytics YOLO
### PyTorch
### OpenCV
### NumPy
