# building-admin-app

## Features
* Django
* Real time chat
* Recommendation system (x)
* Docker (x)
* gRPC and Protocol buffers for realtime chat
* (Google) maps API
* authentication

## Frontend Requirments 
```
npm install axios
```

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Starts server 
```
cd server
python3 manage.py runserver
```

### Build and run docker image

```bash
# debug
./deploy_server.sh 

# prod
./deploy_server.sh -p 

```
