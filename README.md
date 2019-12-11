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

## Installation
```cmd
pip install git+https://github.com/nguyensinhtu/pyservice.git#egg=pyservice
```

## NOTE:
Để start được service bạn cần set APP_TMP
```cmd
export APP_TMP=/your_path/tmp/
```