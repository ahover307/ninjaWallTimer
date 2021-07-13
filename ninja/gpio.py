import RPi.GPIO as GPIO

start_button = 2
end_button = 3


def start_button_callback():
    print("Start pressed")


def end_button_callback():
    print("End pressed")


def init_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup([start_button, end_button], GPIO.IN)

    GPIO.add_event_callback(start_button, GPIO.RISING, callback=start_button_callback(), bouncetime=200)
    GPIO.add_event_callback(end_button, GPIO.RISING, callback=end_button_callback(), bouncetime=200)


def cleanup_gpio():
    GPIO.cleanup([start_button, end_button])
