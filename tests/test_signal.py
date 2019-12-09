import os
import signal
import time

if __name__=='__main__':
    try:
        while True:
            os.kill(15294, signal.SIGTERM)
            time.sleep(0.1)
    except OSError as err:
        err_str = str(err)
        if err_str.find('No such process') > 0:
            print('not found')
        print(err.strerror)
        pass