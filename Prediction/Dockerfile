FROM python:3.10-slim-bullseye
RUN mkdir -p /salesman-prediction
WORKDIR /salesman-prediction
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#CMD [ "python3", "-m" , "flask", "run", "-h","localhost",  "-p", "8090"]
CMD [ "python3", "main.py"]