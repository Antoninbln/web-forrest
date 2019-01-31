import sys
import subprocess
import platform

# Runs the Flask app
def run():
    os_name = platform.system()
    print('Running app on ' + os_name)

    if os_name == "Windows":
        subprocess.call("set FLASK_APP=app.py & python -m flask run", shell=True)
    elif os_name == "Darwin":
        subprocess.call("export FLASK_APP=app.py && python -m flask run", shell=True)
    else:
        print('Your OS is not compatible...')

# Manage command exit
try:
    if __name__ == '__main__':
        run()
except KeyboardInterrupt:
    # quit
    sys.exit()

