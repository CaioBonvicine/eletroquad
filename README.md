# 🚁 ELETROQUAD -- Sistema Autônomo

Projeto desenvolvido para a **Competição EletroQuad SAE BRASIL 2026**.

------------------------------------------------------------------------

## 📦 Hardware Principal

-   🧠 Raspberry Pi 4 Model B\
-   ✈️ Pixhawk 2 (PX4 Firmware)\
-   📡 Telemetria 915 MHz\
-   🛰️ GPS PX4\
-   📷 Intel RealSense D435i (modo RGB)

------------------------------------------------------------------------

# ⚙️ Configuração do Ambiente

## 1️⃣ Criação do Ambiente Virtual

### 🔄 Atualizar o sistema

``` bash
sudo apt update
sudo apt upgrade -y
```

### 📦 Instalar suporte a ambiente virtual

``` bash
sudo apt install python3-venv python3-pip -y
```

### 📁 Criar pasta do projeto

``` bash
mkdir ~/eletroquad
cd ~/eletroquad
```

### 🧪 Criar ambiente virtual

``` bash
python3 -m venv venv
```

### ▶️ Ativar ambiente

``` bash
source venv/bin/activate
```

------------------------------------------------------------------------

## 2️⃣ Instalação das Bibliotecas

Com o ambiente virtual ativado:

``` bash
pip install --upgrade pip
pip install mavsdk
pip install pymavlink
pip install opencv-python
pip install opencv-contrib-python
pip install numpy
pip install pyrealsense2
```

### ⚠️ Caso `pyrealsense2` falhe:

``` bash
sudo apt install librealsense2-dev
```

------------------------------------------------------------------------

# ▶️ Execução do Sistema

## 3️⃣ Execução Manual (Testes)

``` bash
source venv/bin/activate
python main.py
```

------------------------------------------------------------------------

## 4️⃣ Execução Automática (Recomendado)

### Criar `start.sh`

``` bash
#!/bin/bash
cd /home/pi/eletroquad
source venv/bin/activate
python main.py
```

``` bash
chmod +x start.sh
```

------------------------------------------------------------------------

### Criar serviço systemd

``` bash
sudo nano /etc/systemd/system/eletroquad.service
```

Conteúdo do serviço:

``` ini
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
```

### Ativar serviço

``` bash
sudo systemctl daemon-reload
sudo systemctl enable eletroquad.service
```

### Reiniciar sistema

``` bash
sudo reboot
```

------------------------------------------------------------------------

# 🚀 Procedimento de Decolagem na Competição

1.  Ligar drone\
2.  Aguardar boot da Raspberry (\~20s)\
3.  Abrir QGroundControl\
4.  Verificar:
    -   Telemetria conectada\
    -   GPS fixado\
    -   Bateria \> 95%\
    -   Geofence 7m ativa\
5.  Executar `start_mission.py` no notebook\
6.  Drone arma e decola automaticamente

------------------------------------------------------------------------

# 🔒 Segurança

-   Failsafe configurado para **LAND**\
-   Monitoramento de bateria ativo\
-   Função **STOP** via notebook\
-   Botão **LAND** no QGroundControl

------------------------------------------------------------------------

# 📌 Estrutura Recomendada do Projeto

    eletroquad/
    │
    ├── venv/
    ├── main.py
    ├── start.sh
    ├── start_mission.py
    └── README.md
