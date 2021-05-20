FROM python:3.7
EXPOSE 5000

RUN pip3 install Flask glob2
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt
COPY main.py /app/main.py
COPY templates /app/templates

WORKDIR /app/
CMD [ "python", "main.py" ]
