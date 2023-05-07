import os  # Lib para comandos no sistema operacional.
if os.name != 'nt':  # Verifica se não é Windows.
        import RPi.GPIO as GPIO  # Lib Raspberry IO

PINLIST = {'A1':17, 'A2':18, 'A3':19, 'A4':20}  # Lista de I/O Raspberry.

def steupRaspbery():
    print('***INICIANDO SETUP RASPBERRY***')
    
    if os.name != 'nt':
        GPIO.setmode(GPIO.BCM)  # Define padrão de pinos.
        for key, pin in PINLIST.items():
            GPIO.setup(pin, GPIO.OUT)  # Define pinos como saída digital.

            while True:
                GPIO.output(pin, GPIO.HIGH)  # Para iniciar o sistema desligado.
                status = GPIO.input(pin)
                if status == GPIO.HIGH:
                    print(f'pino({pin}) configurado como saída e status OFF')
                    break
                sleep(.1)
    else:
        print('***INICIANDO SISTEMA NO WINDOWS, NÃO POSSUÍ GPIO***')


def pinStatus():
    pinValues = {}
    for key, pin in PINLIST.items():  # Olha todos os pinos da lista.
        if os.name != 'nt':
            status = GPIO.input(pin)  # Verifica nível lógico atual do pino.
            pinValues[key] = status
        else:
            print('***WINDOWS, NÃO POSSUÍ GPIO***')
    return pinValues  # Retorna lista com o status de todos os pinos.


def controlFloor(action, floor):
    global PINLIST
    
    if os.name != 'nt':
        if floor in PINLIST:
            pin = PINLIST[floor]

            command = GPIO.LOW if action == 'ligar' else GPIO.HIGH  # Verifica qual comando veio do servidor.
            log = 'LIGADO' if action == 'ligar' else 'DESLIGADO'
            
            GPIO.output(pin, command)   # ON/OFF , de acordo com o comando do servidor. 

            while True:
                status = GPIO.input(pin)
                if status == command:
                    break  # Sai do Loop infinito.
                else:
                    GPIO.output(pin, command)  # Envia novamente o comando.
                    sleep(.1)
            
        return f'ANDAR {floor} {log} COM SUCESSO, PIN:{pin} !'  # Retorno que irá para o servidor.
    
    print(f'{action.upper()} ANDAR {floor}')  # Caso Windows, apenas "loga".
