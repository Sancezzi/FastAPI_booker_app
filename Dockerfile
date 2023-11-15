FROM python:3.10

RUN mkdir /booker

WORKDIR /booker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /booker/docker/*.sh
