from flask import Flask
import sys
try:
    from gpio import init_gpio
except RuntimeError as e:
    print("We are not running on a Rasp Pi. Not using GPIO")


app = Flask(__name__)
print('Testing if GPIO is imported')
if 'gpio' in sys.modules:
    print('Setting up GPIO')
    init_gpio()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
