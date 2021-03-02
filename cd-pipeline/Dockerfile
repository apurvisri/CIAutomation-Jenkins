#base image
#FROM alpine
FROM python:alpine

WORKDIR /Users/apurvisrivastava/Desktop/Apurvi/Jenkins/CIAutomation-Jenkins/cd-pipeline

COPY . .

#install python3 and pip
#RUN apk add --update python3
RUN /usr/local/bin/python -m pip install --upgrade pip

#install python modukes needed for the python app
#COPY requirements.txt /usr/src/app/
#RUN pip install -- -r requirement.txt

RUN pip install --trusted-host pypi.python.org -r requirement.txt

#copy files required for the app to run 
#COPY app.py /usr/src/app/
#COPY templates/index.html /usr/src/app/templates/



#Tell the port number the container should expose
EXPOSE 5000

ENV NAME earth

#Run the application
#RUN ["python", "app.py"]

ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 
