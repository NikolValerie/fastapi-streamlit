## FastAPI + streamlit

Simple example with fastAPI backend and streamlit interface for image classification

Build with Docker from `api` directory:
```
docker build -t fastapi .
``` 

Then run: 
```
docker run -d --name api-container -p 80:80 fastapi
```

Streamlit app can be run locally or from streamlit [platform](https://streamlit.io/). 

