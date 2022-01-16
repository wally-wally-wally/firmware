import GPIO
import PWM

pwmCtrl = PWM.signal()

class motor:
    def __init__(motor, pwmPin, directionPin):
        motor.pwmPin = pwmPin
        motor.directionPin = directionPin
        motor.speed = 0
        GPIO.setPin(motor.directionPin, 'OUT', 'NONE')

    def setFrequency(motor, frequency):
        if frequency < 15000:
            print ("Error: frequency is too low, please set it to a value between 15000 and 25000")
        elif frequency > 25000:
            print ("Error: frequency is too high, please set it to a value between 15000 and 25000")
        else:
            pwmCtrl.setPin(motor.pwmPin, frequency)
            print ("Successfully set frequency")

    def setDirection(motor, direction):
        if direction == 'CW':
            GPIO.write(motor.directionPin, 'LOW')
        elif direction == 'CCW':
            GPIO.write(motor.directionPin, 'HIGH')
        else:
            print ("Could not set motor direction, expected either: 'CW' or 'CCW'")

    def setSpeed(motor, speed):                     #speed in percentage
        if speed < 50:
            print ("Error: speed is too low, please set it to a value higher than 50%")
        else:
            motor.speed = speed

    def start(motor):
        pwmCtrl.begin(motor.speed)

    def stop(motor):
        pwmCtrl.stop()
