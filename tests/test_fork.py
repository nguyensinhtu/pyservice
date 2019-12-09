# Created by tuns at 2019-12-07 18:26:38
# Email tuns@vng.com.vn

import sys
import os
def test_fork():
    pid = os.getpid()
    print('parent process, pid %s'% (pid))
    try:
        # return twice, 0 in child process 
        # and pid of child in parent process
        pid = os.fork()
        if pid > 0: # return value of child's pid
            print('fork a child process, pid: %s' % (pid))
            # sys.exit(0)
        elif pid == 0: # child
            print("child process is executed here!!")
    except OSError as ex:
        print("error fork new process from %s"% (pid))
        sys.exit(1)
    
if __name__ == "__main__":
    test_fork()