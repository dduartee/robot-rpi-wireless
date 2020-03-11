import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(40, GPIO.OUT)# S1
GPIO.setup(38, GPIO.OUT)# S2
GPIO.setup(37, GPIO.OUT)# S3
GPIO.setup(36, GPIO.OUT)# S4

GPIO.output(40, 0)
GPIO.output(38, 1)
GPIO.output(37, 0)
GPIO.output(36, 1)


