# ARG DATASOURSE
# ARG RESULTS
FROM ubuntu:20.04

# FROM python:3.8

RUN apt-get update && \
   apt-get install --no-install-recommends -y python3 python3-pip

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY ./app.py app.py
# COPY ./dataset DATASOURSE
# COPY ./results RESULTS
COPY ./requirements.txt requirements.txt

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir results

# RUN git clone https://github.com/ultralytics/ultralytics && /
#     cd ultralytics && /
#     pip install -r requirements.txt && /
#     cd ..

# define the port number the container should expose
# EXPOSE 5000



# run the command
CMD ["python", "./app.py"]