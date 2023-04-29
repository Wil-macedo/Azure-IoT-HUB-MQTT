from azure.iot.device import IoTHubDeviceClient, MethodResponse
from time import sleep 
import os

if os.name != 'nt':
        import RPi.GPIO as GPIO

PINLIST = {'A1':17, 'A2':18, 'A3':19, 'A4':20, 'A5':18}

def steupRaspbery():
    print('***INICIANDO SETUP RASPBERRY***')
    
    if os.name != 'nt':
        GPIO.setmode(GPIO.BCM)
        for key, pin in PINLIST.items():
            GPIO.setup(pin, GPIO.OUT)

            while True:
                GPIO.output(pin, GPIO.HIGH)  # Para iniciar o sistema desligado!
                status = GPIO.input(pin)
                if status == GPIO.HIGH:
                    print(f'pino({pin}) configurado como saída e status OFF')
                    break
                sleep(.1)
    else:
        print('***INICIANDO SISTEMA NO WINDOWS, NÃO POSSUÍ GPIO***')



def create_client():
    CONNECTION_STRING = f"HostName=coletores.azure-devices.net;DeviceId=Willian;SharedAccessKey=+rLE2638/MuS4RoH2iUsgDTQxhej1cpVf3K6Zn7pqC4="
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    def method_request_handler(method_request):
        command = method_request.payload
        floor = method_request.name
        result = controlFloor(command, floor)
        
        print(result)
        
        resp_payload = {"Response": result}
        method_response = MethodResponse(method_request.request_id, 200, resp_payload)
        client.send_method_response(method_response)

    try:    
        client.on_method_request_received = method_request_handler
    except: 
        client.shutdown()

    return client

def controlFloor(action, floor):
    global PINLIST
    
    if os.name != 'nt':
        if floor in PINLIST:
            pin = PINLIST[floor]

            command = GPIO.LOW if action == 'ligar' else GPIO.HIGH
            log = 'LIGADO' if action == 'ligar' else 'DESLIGADO'
            
            GPIO.output(pin, command)

            while True:
                status = GPIO.input(pin)  # Certeza que pino est desligado
                if status == command:
                    break
                else:
                    GPIO.output(pin, command)  # Envia novamente o comando
                    sleep(.1)
            
        return f'ANDAR {floor} {log} COM SUCESSO, PIN:{pin} !'
    
    print(f'{action.upper()} ANDAR {floor}')


def main():
    steupRaspbery()
    print ("***INICIANDO HUB ToT LOCAL***")
    client = create_client()

    print ("AGUARDANDO COMANDOS, PRESSIONA Ctrl-C PARA SAIR")
    try:
        while True: sleep(1000)
    except KeyboardInterrupt:
        print("IoTHubDeviceClient ENCERRADO")
    finally:
        print("DESLIGANDO IoT Hub Client")
        client.shutdown()

main()  # Start
