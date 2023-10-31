FROM ubuntu:20.04

RUN apt-get update && \
   apt-get install --no-install-recommends -y python3 python3-pip

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY ./val.py val.py

COPY ../requirements.txt requirements.txt

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir results

# run the command
CMD ["python", "./val.py"]