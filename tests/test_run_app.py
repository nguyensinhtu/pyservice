import sys
sys.path.append('../pyservice')
from pyservice import app
import argparse

@app.main(app_name='app_abc')
def main_app():
    print(sys.argv)
    # arg_parser = argparse.ArgumentParser(description='Som integers')
    # arg_parser.add_argument('--inte', type=int, required=True)
    # args = arg_parser.parse_args()
    # print(args.inte)
    while True:
        continue
    print('hello')

if __name__=='__main__':
    main_app()