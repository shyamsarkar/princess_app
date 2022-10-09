# princess_app
carefully watch step counts....

## installation process ##
1. pip install -r requirements.txt

## Directly Run
2. python app.py

# alternative option

*** Flask Run with debug mode is on ***

### For PowerShell ###
2. $env:flask_app="app"
3. $env:flask_env="development"
4. flask run (if there is error then try python -m flask run)

### For Command Prompt ###

2. set FLASK_APP=app
3. set FLASK_ENV=development
4. flask run