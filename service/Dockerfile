FROM python:3.9.0

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY VideoTracker.py /

ENTRYPOINT ["python", "./VideoTracker.py"]
