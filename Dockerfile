FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
COPY brp_bewoning_client-1.0.0-py3-none-any.whl /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt \
  && pip3 install brp_bewoning_client-1.0.0-py3-none-any.whl

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "brp.bewoning_api"]
