# Created by tuns at 2019-12-08 21:48:40
# Email tuns@vng.com.vn

def test_sys_out():
    import sys
    sys.stdout.write('Hellow world!!')
    try:
        f = open('/zserver/tmp/abc.pidd', 'r')
    except IOError as err:
        print('error : %s\n'%err.strerror)
    import os
    os.dup2(f.fileno(), sys.stdout.fileno())
    f.close()

import sys
import os
import atexit

def exit_1():
    print('exit 1')

def exit_2():
    print('exit 2')

def test_atexit():
    # will be call last when exit app
    atexit.register(exit_1)
    atexit.register(exit_2)

if __name__ == "__main__":

    # test_sys_out() 
    os.remove('/zserver/tmp/abc.txt')