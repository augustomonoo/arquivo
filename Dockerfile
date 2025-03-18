FROM python:3.12 as build-python

ENV WORKDIR "/app"
ENV DEPLOYMENT "${WORKDIR}/deployment"
ENV DEBIAN_FRONTEND=noninteractive 

WORKDIR ${WORKDIR}
COPY . ${WORKDIR}

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install --without=dev
RUN groupadd -g 1000 python
RUN useradd -u 1000 -g 1000 python
RUN mkdir -p ${DEPLOYMENT}
RUN mv ${WORKDIR}/.venv ${DEPLOYMENT}/.venv
RUN chown -R python:python ${WORKDIR}

FROM node:18.14.1 as build-node
ENV WORKDIR "/app"
ENV DEPLOYMENT "${WORKDIR}/deployment"

WORKDIR ${WORKDIR}
COPY . ${WORKDIR}

RUN mkdir -p ${DEPLOYMENT}
RUN npm install
RUN npm run build:docker

FROM python:3.12
LABEL maintainer="Carlos Augusto Monoo Pereira Barbosa <augustomonoo@gmail.com>"

ENV WORKDIR "/app"
ENV DEPLOYMENT "${WORKDIR}/deployment"
ENV VIRTUAL_ENV="${WORKDIR}/.venv"
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
ENV PUBLIC_PATH="${WORKDIR}/public"
ENV PRIVATE_PATH="${WORKDIR}/private"

COPY ./arquivo ${WORKDIR}/arquivo
COPY ./config ${WORKDIR}/config
COPY ./manage.py ${WORKDIR}/manage.py
COPY ./gunicorn.sh ${WORKDIR}/gunicorn.sh
COPY --from=build-python ${DEPLOYMENT}/.venv ${WORKDIR}/.venv
COPY --from=build-node ${DEPLOYMENT}/style.css ${WORKDIR}/arquivo/static/arquivo/style.css
COPY --from=build-node ${DEPLOYMENT}/bundle.js ${WORKDIR}/arquivo/static/arquivo/bundle.js

WORKDIR ${WORKDIR}

RUN apt-get update \
    && apt-get install -y gettext libgettextpo-dev \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -g 1000 python \
    && useradd -r -d ${WORKDIR} -u 1000 -g 1000 python \
    && mkdir -p ${WORKDIR}/public \
    && mkdir -p ${WORKDIR}/private \
    && chown -R 1000:1000 ${WORKDIR}
RUN DEBUG=False python manage.py collectstatic --noinput

VOLUME [ "${PUBLIC_PATH}", "${PRIVATE_PATH}"]

EXPOSE 8000
USER python

HEALTHCHECK CMD ["curl", "--fail", "http://127.0.0.1:8000"]
CMD [ "bash", "gunicorn.sh" ]