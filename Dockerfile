from python:3.7

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

RUN pip install --upgrade pip \
    && pip install --no-cache-dir \
    flask \
    flask-sqlalchemy \
    SQLAlchemy 

COPY ./app /app

WORKDIR /app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]