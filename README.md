# wrapper để run python services
ex:
```python
from pyservice import app

@app.main(app_name='some_app_name')
def main_app():
    #some code
    pass

if __name__=='__main__':
    main_app()
```