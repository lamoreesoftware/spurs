FROM docker.io/library/alpine:3.22.2

RUN apk add --no-cache python3=3.12.12-r0 py3-pip=25.1.1-r0 bash=5.2.37-r0

WORKDIR /app

COPY main.py requirements.txt run.sh ./

RUN /usr/bin/python3 -m venv .venv && \
  source .venv/bin/activate && \
  pip install -r requirements.txt && \
  chmod 755 /app/run.sh

CMD /app/run.sh
