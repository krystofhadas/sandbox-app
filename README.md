# How to start
## Install requirements.txt
```pip install requirements.txt```
## Set up pythonpath
```
echo 'export PYTHONPATH=.' >> ~/.bash_profile
source ~/.bash_profile
```
## Run backend
### Locally:
```uvicorn main:app --reload --host 0.0.0.0 --port 8080```
### In docker (k8s):
