FROM python:3.7-buster

EXPOSE 5000

WORKDIR /usr/src/
COPY . .

RUN python -m pip install poetry
RUN poetry install

ENV FLASK_APP=research-environment-server/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["poetry", "run", "flask", "run"]