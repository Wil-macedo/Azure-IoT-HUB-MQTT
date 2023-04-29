from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import CloudToDeviceMethod

# methodName = andar_01, methodPayLoad = True/ False
def iothub_devicemethod_sample_run(methodName, methodPayLoad):
    CONNECTION_STRING = f"HostName=coletores.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=FCvJdZxbzerH8jUk5bG7dDP6tueJUOWv3MAHiKGJlUY="
    DEVICE_ID = "Willian"  # INFORMA O NOME DO DISPODITIVO
    try:
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)  # SE CONECTA AO Hub IoT DE ACORDO COM A CHAVE DE ACESSO

        deviceMethod = CloudToDeviceMethod(method_name=methodName, payload=methodPayLoad)  # ENVIA COMANDO PARA O RASPBERRY
        result = registry_manager.invoke_device_method(DEVICE_ID, deviceMethod)  # RECEBE RETORNO DO COMANDO

        return result.payload  # RETORNA COMANDO

    except Exception as ex:  # EXECUTA CASO ERRO.
        print ( "ERRO INESPERADO {0}".format(ex) )
        return
    except KeyboardInterrupt:  # COMANDO PARA PARADA NO TECLADO
        print ( "IoTHubDeviceMethod PARADA INESPERADA" )

if __name__ == '__main__':
    print ( "***Starting the IoT Hub Service Client***")
    iothub_devicemethod_sample_run()