import sys
sys.path.append('../pyservice')
from pyservice import app
import random
from time import sleep

def worker(i, quit, foundit):
    print("%d started" % i)
    while True:
        x = random.random()
        if x > 0.9:
            print ('%d found %g' % (i, x))
            foundit.set()
            continue
        sleep(0.1)
    print ("%d is done" % i)


@app.main(app_name='app-multiprocess')
def multiprocess_app():
    import multiprocessing as mp
    quit = mp.Event()
    foundit = mp.Event()
    for i in range(2):
        p = mp.Process(target=worker, args=(i, quit, foundit))
        p.start()
    foundit.wait()
    quit.set()

if __name__ == '__main__':
    multiprocess_app()