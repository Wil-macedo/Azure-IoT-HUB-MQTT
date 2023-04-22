import time
import os
from azure.iot.device import IoTHubDeviceClient, MethodResponse

PINLIST = {'A1':18, 'A2':19, 'A3':20, 'A4':18, 'A5':18}

def steupRaspbery():
    print('***INICIANDO SETUP RASPBERRY***')
    if os.name != 'nt':
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        for key, pin in pinList.items():
            GPIO.setup(pin, GPIO.OUT)
            print(f'pino({pin}) configurado como saída.')


def create_client():
    CONNECTION_STRING = f"HostName=coletores.azure-devices.net;DeviceId=Willian;SharedAccessKey=+rLE2638/MuS4RoH2iUsgDTQxhej1cpVf3K6Zn7pqC4="
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    def method_request_handler(method_request):
        result = ligarAndar(method_request.name) if 'ligar' == method_request.payload \
            else desligarAndar(method_request.name)
        print(result)
        
        resp_payload = {"Response": result}
        method_response = MethodResponse(method_request.request_id, 200, resp_payload)
        client.send_method_response(method_response)

    try:    client.on_method_request_received = method_request_handler
    except: client.shutdown()

    return client

def ligarAndar(andar):
    global PINLIST
    if os.name != 'nt':
        if andar in PINLIST:
            pin = pinList[andar]
            GPIO.output(pin, GPIO.HIGH)

        return f'ANDAR {pin} LIGADO COM SUCESSO !'
    print(f'LIGAR ANDAR {andar}')


def desligarAndar(andar):
    global PINLIST
    if os.name != 'nt':
        if andar in PINLIST:
            pin = pinList[andar]
            GPIO.output(pin, GPIO.HIGH)
        return f'ANDAR {pin} DESLIGADO COM SUCESSO !'
    print(f'LIGAR ANDAR {andar}')


def main():
    steupRaspbery()
    print ("***INICIANDO HUB ToT LOCAL***")
    client = create_client()

    print ("AGUARDANDO COMANDOS, PRESSIONA Ctrl-C PARA SAIR")
    try:
        while True: time.sleep(1000)
    except KeyboardInterrupt:
        print("IoTHubDeviceClient ENCERRADO")
    finally:
        print("DESLIGANDO IoT Hub Client")
        client.shutdown()

main()  # Start
