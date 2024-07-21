FROM python:3.10-slim

RUN mkdir /workspace
COPY . /workspace/

WORKDIR /workspace
RUN apt-get update && apt-get install -y git
RUN pip install -r requirements.txt

ENV HOME=/workspace

CMD [ "python" , "main.py" ]

