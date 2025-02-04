import ast
from flask import Flask, redirect, render_template, url_for, request  # Lib Framework Web FLASK.
import WEB.hub_Iot as hub_Iot  # Lib Azure IoT Hub.

connected = False

app = Flask(__name__)

@app.route("/")  # endpoint inicial da aplicação
def index():
    return redirect(url_for("conectar"))  # "Chama" o endpoin /login.


@app.route("/conectar") # endpoint de Login
def conectar():
    global connected

    if connected:
        return render_template("predio.html", pinStatus ={})  # Mostra pagína do prédio.        
    else:  # Devemos conectar.
        try:
            result = hub_Iot.iothubRun("True", "check")  # Envia comando para saber o status de cada pino.
            if result is not None:
                connected = True
                return redirect(url_for("predio", **result["Response"]))  # # "Chama" o endpoin /predio.
            else:
                return "DISPOSITIVO OFFLINE"
        except:
            return "FALHA AO TENTAR SE CONECTAR AO DISPOSITIVO"


@app.route("/predio")
def predio():
    if not connected:
        return redirect(url_for("conectar"))  # "Chama" o endpoin /login.

    status = request.args
    print(f"ACTION {status['resultAction']}")

    pinStatus = ast.literal_eval(status['pinStatus'])
    return render_template("predio.html", pinStatus = pinStatus)  # Mostra pagína do prédio.
    
    
@app.route("/mqtt/<andar>/<ligar>")  # Executa o comando MQTT.
def mqtt(andar, ligar):  # Tenta enviar o comando 2X
    for _ in range(0,2):
        result = hub_Iot.iothubRun(andar, ligar)  # Envia comando ON/OFF para o andar.
        if result is not None:
            return redirect(url_for("predio", **result["Response"]))  # # "Chama" o endpoin /predio.


if __name__ == "__main__":
   app.run()  # Ínicio da aplicação.
