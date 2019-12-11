from pyservice import app

@app.main(app_name='abc')
def main_app():
    while True:
        print('hello')

if __name__ == "__main__":
   main_app() 