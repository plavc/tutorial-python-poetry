FROM python:3.11.3-slim

LABEL author="Gregor Plavčak <plavc@users.noreply.github.com>"

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY gptool /app/gptool

ENTRYPOINT ["python", "/app/gptool/main.py"]
