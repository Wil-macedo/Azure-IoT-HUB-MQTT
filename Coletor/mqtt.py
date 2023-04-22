import time
from azure.iot.device import IoTHubDeviceClient, MethodResponse

def create_client():
    CONNECTION_STRING = f"HostName=coletores.azure-devices.net;DeviceId=Willian;SharedAccessKey=+rLE2638/MuS4RoH2iUsgDTQxhej1cpVf3K6Zn7pqC4="
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    def method_request_handler(method_request):
        if 'ligar' == method_request.payload:
            result = ligarAndar(method_request.name)
        else:
            result = desligarAndar(method_request.name)
        print(result)
        
        resp_payload = {"Response": result}
        method_response = MethodResponse(method_request.request_id, 200, resp_payload)
        client.send_method_response(method_response)

    try:
        client.on_method_request_received = method_request_handler
    except:
        client.shutdown()

    return client

def ligarAndar(andar):
    if andar == 'A1':
        pass
    elif andar == 'A2':
        pass
    elif andar == 'A3':
        pass
    elif andar == 'A4':
        pass

    return f'ANDAR {andar[1]} LIGADO COM SUCESSO !'

def desligarAndar(andar):
    if andar == 'A1':
        pass
    elif andar == 'A2':
        pass
    elif andar == 'A3':
        pass
    elif andar == 'A4':
        pass
    
    return f'ANDAR {andar[1]} DESLIGADO COM SUCESSO !'


def main():
    print ("***INICIANDO HUB ToT LOCAL***")
    client = create_client()

    print ("AGUARDANDO COMANDOS, PRESSIONA Ctrl-C PARA SAIR")
    try:
        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        print("IoTHubDeviceClient ENCERRADO")
    finally:
        print("SDESLIGANDO IoT Hub Client")
        client.shutdown()

if __name__ == '__main__':
    main()
