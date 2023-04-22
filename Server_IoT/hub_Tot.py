from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import CloudToDeviceMethod

# methodName = andar_01, methodPayLoad = True/ False
def iothub_devicemethod_sample_run(methodName, methodPayLoad):
    CONNECTION_STRING = f"HostName=coletores.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=FCvJdZxbzerH8jUk5bG7dDP6tueJUOWv3MAHiKGJlUY="
    DEVICE_ID = "Willian"
    try:
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)

        deviceMethod = CloudToDeviceMethod(method_name=methodName, payload=methodPayLoad)
        result = registry_manager.invoke_device_method(DEVICE_ID, deviceMethod)

        return result.payload

    except Exception as ex:
        print ( "ERRO INESPERADO {0}".format(ex) )
        return
    except KeyboardInterrupt:
        print ( "IoTHubDeviceMethod PARADA INESPERADA" )

if __name__ == '__main__':
    print ( "***Starting the IoT Hub Service Client***")
    iothub_devicemethod_sample_run()