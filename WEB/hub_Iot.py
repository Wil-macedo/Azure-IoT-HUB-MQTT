from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import CloudToDeviceMethod

CONNECTION_STRING = "YOUR_KEY"  # https://devblogs.microsoft.com/iotdev/understand-different-connection-strings-in-azure-iot-hub/
DEVICE_ID = "YOUR_DEVICE"  # Device name.
CONNECTION = IoTHubRegistryManager(CONNECTION_STRING)  # SE CONECTA AO Hub IoT DE ACORDO COM A CHAVE DE ACESSO

# methodName = andar_01, methodPayLoad = True/ False
def iothubRun(methodName, methodPayLoad):
    try:
        deviceMethod = CloudToDeviceMethod(method_name=methodName, payload=methodPayLoad)  # ENVIA COMANDO PARA O RASPBERRY
        result = CONNECTION.invoke_device_method(DEVICE_ID, deviceMethod)  # RECEBE RETORNO DO COMANDO.
        return result.payload  # RETORNA COMANDO.

    except Exception as ex:  # EXECUTA CASO ERRO.
        print ( "ERRO INESPERADO {0}".format(ex) )
        return