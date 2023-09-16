# Request_Days_Off_Application
 
## Instalations

1) You have to install kubernetes docker and python

### Kubernetes commands

#### Execute the following commands

1) microk8s kubectl apply -f docker-secret.yaml
2) cd Version1
3) cd kubernetes-mysql
4) microk8s kubectl apply -f mysql-pv.yaml
5) microk8s kubectl apply -f mysql-pvc.yaml
6) microk8s kubectl apply -f mysql-secret.yaml
7) microk8s kubectl apply -f mysql-stateful.yaml
8) microk8s kubectl apply -f mysql-service.yaml
9) cd ../kubernetes-broker
10) microk8s kubectl apply -f mosquitto-config.yaml
11) microk8s kubectl apply -f mosquitto-stateful.yaml
12) microk8s kubectl apply -f mosquitto-service.yaml
13) cd ..

### pip install commands

1) cd backend
2) pip install -r requirements.txt
3) cd ..
4) cd days_off
5) pip install -r requirements.txt

### run app

1) cd backend
2) python3 backend-service.py
3) open new terminal
4) cd ../days_off
5) python manage.py runserver


### open the app

1) open the link http://127.0.0.1:8000/accounts/login
