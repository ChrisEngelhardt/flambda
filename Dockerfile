FROM python:3.7

RUN pip3 install Flask glob2
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt
COPY main.py /app/main.py

WORKDIR /app/
CMD [ "python", "main.py" ]