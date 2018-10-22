FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-dev

RUN ln -s /usr/bin/python3 /usr/bin/python; ln -s /usr/bin/pip3 /usr/bin/pip;

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["api.py"]
