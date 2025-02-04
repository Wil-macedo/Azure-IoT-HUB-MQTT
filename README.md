# 📡 Projeto IoT Hub - Controle de Prédio com Raspberry Pi e Flask

Este projeto consiste em um sistema de controle remoto para um prédio, utilizando o **Azure IoT Hub**, um **Raspberry Pi** e um servidor **Flask** para interface web. 

## 📌 Estrutura do Projeto

O projeto está dividido em duas partes principais:

1. **🌐 Parte Web (Flask)**: Interface para o usuário acessar e controlar os andares do prédio e receber as menssagens do MQTT.
2. **🤖 Parte Raspberry Pi**: Código responsável por receber comandos e controlar os pinos GPIO do Raspberry.

---

## 🏗️ Tecnologias Utilizadas
- Python
- Flask
- Azure IoT Hub
- Raspberry Pi
- MQTT (Protocolo de comunicação)

---

## 📂 Organização dos Arquivos

```
📦 Projeto-IoT
├── 🌐 Web (Servidor)
│
├── 🤖 Raspberry (Cliente)
│
├── 📄 README.md (Documentação)
└── 📜 requirements.txt (Dependências do projeto)
```

---

## 🌐 Parte Web (Flask)

A aplicação web foi desenvolvida usando Flask e fornece uma interface para os usuários controlarem os andares do prédio remotamente. 

### 🔧 Configuração do Servidor Web

1. Instale as dependências:
   ```bash
   pip install -r WEB/requirements.txt
   ```
2. Execute o servidor Flask:
   ```bash
   python app.py
   ```
3. Acesse no navegador:
   ```
   http://localhost:5000/conectar
   ```

### 🔗 Endpoints
- **`/conectar`** → Conecta com o IoT Hub e retorna o status dos andares.
- **`/predio`** → Interface gráfica com os andares.
- **`/mqtt/<andar>/<ligar>`** → Envia comandos ON/OFF para o Raspberry via Azure IoT Hub.

---

## 🤖 Parte Raspberry Pi

O código do Raspberry Pi gerencia os pinos GPIO para controlar os andares e se comunica com o **Azure IoT Hub**.

### 🛠️ Configuração do Raspberry Pi
1. Instale as bibliotecas necessárias:
   ```bash
   pip install -r requierements.txt
   ```
2. Execute o cliente IoT:
   ```bash
   python mqtt.py
   ```

### ⚙️ Controle GPIO
O Raspberry Pi recebe comandos via Azure IoT Hub e altera os estados dos pinos GPIO:

- **Pinos utilizados**: 
  ```python
  PINLIST = {"A1":17, "A2":18, "A3":19, "A4":20}
  ```
- **Comandos disponíveis**:
  - `ligar` → Liga o andar correspondente
  - `desligar` → Desliga o andar correspondente

---

## 🚀 Implantação com Azure IoT Hub

Para utilizar o **Azure IoT Hub**, configure a conexão no arquivo `iot_client.py` é necessário configurar:

***CONNECTION_STRING***, ***DEVICE_ID***
💡 **Importante**: Substitua `YOUR_KEY` & `YOUR_DEVICE` pela sua chave de acesso ao Azure IoT Hub.