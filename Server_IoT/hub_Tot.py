from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import CloudToDeviceMethod

CONNECTION_STRING = f"HostName=coletores.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=FCvJdZxbzerH8jUk5bG7dDP6tueJUOWv3MAHiKGJlUY="
DEVICE_ID = "Willian"  # INFORMA O NOME DO DISPODITIVO
CONNECTION = IoTHubRegistryManager(CONNECTION_STRING)  # SE CONECTA AO Hub IoT DE ACORDO COM A CHAVE DE ACESSO

# methodName = andar_01, methodPayLoad = True/ False
def iothubRun(methodName, methodPayLoad):
    try:
        deviceMethod = CloudToDeviceMethod(method_name=methodName, payload=methodPayLoad)  # ENVIA COMANDO PARA O RASPBERRY
        result = CONNECTION.invoke_device_method(DEVICE_ID, deviceMethod)  # RECEBE RETORNO DO COMANDO
        return result.payload  # RETORNA COMANDO

    except Exception as ex:  # EXECUTA CASO ERRO.
        print ( "ERRO INESPERADO {0}".format(ex) )
        return
    except KeyboardInterrupt:  # COMANDO PARA PARADA NO TECLADO
        print ( "IoTHubDeviceMethod PARADA INESPERADA" )