# todo-app
- Testing nextjs and drf
- Have not tested using CRUD operations

## Client Side
- Used Nextjs with axios to retrieve api from the backend

## Server Side
- Created easy models and created a REST API with the Django REST Framework

## Screenshots
![Image of Frontend](https://github.com/CippyLOL/todo-app/blob/main/screenshots/Screenshot%202021-11-07%20at%206.05.58%20PM.png)
![Image of REST API - DRF](https://github.com/CippyLOL/todo-app/blob/main/screenshots/Screenshot%202021-11-07%20at%206.06.29%20PM.png)

## How to Run
(For Reference)

### Server
Install the relevant packages:
```sh
pip install django djangorestframework django-cors-headers
```
Then, run the following command to load the server.
```sh
python manage.py runserver
```
You can now find the API details at `localhost:8000/api`.

### Client
Firstly, run the following command:
```sh
cd client
npm i
```
Next, run the application:
```sh
npm run dev
```

Go to `localhost:3000` to see the existing application, with the Todos!
