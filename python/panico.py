import RPi.GPIO as GPIO
import subprocess

ativado = 1
desativado = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(40, GPIO.OUT)# rele de frente
GPIO.setup(38, GPIO.OUT)# rele de re
GPIO.setup(37, GPIO.OUT)# rele de esquerda
GPIO.setup(36, GPIO.OUT)# rele de direita

GPIO.cleanup()
GPIO.cleanup()
GPIO.cleanup()


