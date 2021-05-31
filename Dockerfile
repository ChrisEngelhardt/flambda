FROM python:3.7

RUN pip3 install Flask glob2
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt
COPY *.py /app/

COPY templates /app/templates

WORKDIR /app/
CMD [ "python", "main.py" ]