import machine
import utime

# Importa a classe HCSR04 da biblioteca hcsr04.py
from hcsr04 import HCSR04

# Definir os pinos de controle da ponte H
IN1_LEFT_PIN = 21
IN2_LEFT_PIN = 22

IN1_RIGHT_PIN = 27
IN2_RIGHT_PIN = 28

# Configurar os pinos como saídas
in1_left = machine.Pin(IN1_LEFT_PIN, machine.Pin.OUT)
in2_left = machine.Pin(IN2_LEFT_PIN, machine.Pin.OUT)
in1_right = machine.Pin(IN1_RIGHT_PIN, machine.Pin.OUT)
in2_right = machine.Pin(IN2_RIGHT_PIN, machine.Pin.OUT)

# Define os pinos do Raspberry Pi Pico conectados ao módulo HC-SR04
hcsr04_left_trigger_pin = 14
hcsr04_left_echo_pin = 15
hcsr04_right_trigger_pin = 16
hcsr04_right_echo_pin = 17

# Define o timeout para o módulo HC-SR04 em ms
hcsr04_timeout_ms = 20

# Instancia o objeto HCSR04 com os pinos definidos
hcsr04_left_sensor = HCSR04(hcsr04_left_trigger_pin,
                            hcsr04_left_echo_pin, hcsr04_timeout_ms)
hcsr04_right_sensor = HCSR04(
    hcsr04_right_trigger_pin, hcsr04_right_echo_pin, hcsr04_timeout_ms)
# Definir a direção do motor


def set_motor_direction(direction):
    if direction == 'forward':
        in1_left.on()
        in2_left.off()

        in1_right.on()
        in2_right.off()
    elif direction == 'backward':
        in1_left.off()
        in2_left.on()

        in1_right.off()
        in2_right.on()
    elif direction == 'stop':
        in1_left.off()
        in2_left.off()

        in1_right.off()
        in2_right.off()
    elif direction == 'left':
        in1_left.on()
        in2_left.off()

        in1_right.off()
        in2_right.on()


# Exemplo de uso
while True:
    set_motor_direction('forward')
    # Obtém a distância medida pelo sensor HC-SR04 em cm
    distance_cm_left = hcsr04_left_sensor.get_distance_cm()
#     distance_cm_left = 10
    distance_cm_right = hcsr04_right_sensor.get_distance_cm()
    print(f"sensor esquerdo: {distance_cm_left}")
    print(f"sensor direito: {distance_cm_right}")
    if (distance_cm_left < 12 and distance_cm_left > 1) or (distance_cm_right < 12 and distance_cm_right > 1):
        set_motor_direction('stop')
        utime.sleep(1)
        set_motor_direction('backward')
        utime.sleep(1)
        set_motor_direction('left')
        utime.sleep(1.5)
        set_motor_direction('stop')
        utime.sleep(2)
