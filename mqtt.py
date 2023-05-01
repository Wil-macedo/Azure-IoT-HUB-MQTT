from azure.iot.device import IoTHubDeviceClient, MethodResponse  # Lib IoT Hub.
from time import sleep # Lib para delay.
from raspberry import * # Lib de controle do Raspberry (apenas para organizar).

def create_client():  # Cria cliente IoT Hub.
    CONNECTION_STRING = f"HostName=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  # Conecta cliente ao IoT Hub

    def method_request_handler(method_request):
        command = method_request.payload  # Recebe comando IoT do servidor.
        if command == 'check': # Se for a primeira conexão, ele envia status dos pinos.
            result = pinStatus()
        else:
            floor = method_request.name # Identifica andar que será ligado.
            result = controlFloor(command, floor)  # Função de controle do andar.   
        print(result)
        
        resp_payload = {"Response": result}  # Monta resposta para o servidor.
        method_response = MethodResponse(method_request.request_id, 200, resp_payload)  
        client.send_method_response(method_response)  # Envia resposta. 
    try:    
        client.on_method_request_received = method_request_handler  # Loop que aguarda comandos.
    except: 
        client.shutdown()  # Delsiga serviço.
    return client

def main():  # Função principal
    steupRaspbery()  # Configura pinos do Raspberry.
    print ("***INICIANDO HUB ToT LOCAL***")
    client = create_client()

    print ("AGUARDANDO COMANDOS, PRESSIONA Ctrl+C PARA SAIR")
    try:
        while True: sleep(1000)  # Software roda em Thread.
    except KeyboardInterrupt:
        print("IoTHubDeviceClient ENCERRADO")
    finally:
        print("DESLIGANDO IoT Hub Client")
        client.shutdown()

if __name__ == '__main__':
    main()  # Ínicia aplicação.
