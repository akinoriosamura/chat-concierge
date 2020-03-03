FROM python:3.6

RUN apt-get update

# workdirの指定
WORKDIR /var/www

# 依存Pythonライブラリ一覧コピー
COPY Pipfile ./
COPY Pipfile.lock ./

# install pipenv
RUN pip install -U pip && \
    pip install pipenv && \
    pipenv install --dev --system

WORKDIR /var/www/src

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]