# ELETROQUAD - Sistema Autônomo

Projeto desenvolvido para Competição EletroQuad SAE BRASIL 2026.

Hardware principal:
- Raspberry Pi 4 Model B
- Pixhawk 2 (PX4 Firmware)
- Telemetria 915 MHz
- GPS PX4
- Intel RealSense D435i (modo RGB apenas)

---

# 1️⃣ CRIAÇÃO DO AMBIENTE VIRTUAL

Atualizar sistema:

sudo apt update
sudo apt upgrade -y

Instalar suporte a venv:

sudo apt install python3-venv python3-pip -y

Criar pasta do projeto:

mkdir ~/eletroquad
cd ~/eletroquad

Criar ambiente virtual:

python3 -m venv venv

Ativar ambiente:

source venv/bin/activate

---

# 2️⃣ INSTALAÇÃO DAS BIBLIOTECAS

Dentro do ambiente virtual:

pip install --upgrade pip
pip install mavsdk
pip install pymavlink
pip install opencv-python
pip install opencv-contrib-python
pip install numpy
pip install pyrealsense2

Se pyrealsense2 falhar:

sudo apt install librealsense2-dev

---

# 3️⃣ EXECUÇÃO MANUAL (PARA TESTES)

source venv/bin/activate
python main.py

---

# 4️⃣ EXECUÇÃO AUTOMÁTICA (RECOMENDADO)

Criar start.sh:

#!/bin/bash
cd /home/pi/eletroquad
source venv/bin/activate
python main.py

chmod +x start.sh

Criar serviço systemd:

sudo nano /etc/systemd/system/eletroquad.service

Conteúdo:

[Unit]
Description=EletroQuad Autonomous System
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/eletroquad
ExecStart=/home/pi/eletroquad/start.sh
Restart=always

[Install]
WantedBy=multi-user.target

Ativar:

sudo systemctl daemon-reload
sudo systemctl enable eletroquad.service

Reiniciar:

sudo reboot

---

# 5️⃣ PROCEDIMENTO DE DECOLAGEM NA COMPETIÇÃO

1. Ligar drone
2. Aguardar boot da Raspberry (~20s)
3. Abrir QGroundControl
4. Verificar:
   - Telemetria conectada
   - GPS fixado
   - Bateria > 95%
   - Geofence 7m ativa
5. Executar start_mission.py no notebook
6. Drone arma e decola automaticamente

---

# 6️⃣ SEGURANÇA

- Failsafe configurado para LAND
- Monitoramento de bateria ativo
- Função STOP via notebook
- Botão LAND no QGroundControl