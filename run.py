import sys
import subprocess
import platform

# Runs the Flask app
def run():
    os_name = platform.system()
    print('Running app on ' + os_name)

    if os_name == "Windows":
        subprocess.call("set FLASK_APP=app.py & set FLASK_DEBUG=1 & python -m flask run", shell=True)
    elif os_name == "Darwin":
        subprocess.call("export FLASK_APP=app.py && export FLASK_DEBUG=1 && python -m flask run", shell=True)
    else:
        print('Your OS is not compatible...')

# Manage command exit
if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        # quit
        sys.exit()

