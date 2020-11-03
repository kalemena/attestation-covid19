FROM python:3.7

ENV TZ=Europe/Paris

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

RUN apt-get update --quiet --quiet \
    && apt-get install --yes --no-install-recommends \
        gettext-base \
        inkscape \
        make \
        pdftk \
        python-qrcode \
        python-scour \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

### USER covid
RUN useradd -ms /bin/bash -u 1000 covid

### Web Service tools
RUN pip install --no-cache-dir \
    flask \
    flask_restful \
    flask_jsonpify

COPY --chown=covid:covid [ ".", "/data/" ]
#VOLUME ["/data"]
WORKDIR /data

COPY --chown=covid:covid [ "docker-entrypoint.sh", "/" ]
RUN chmod +x /docker-entrypoint.sh

USER covid

# CMD [ "/docker-entrypoint.sh" ]
CMD [ "flask", "run", "--host", "0.0.0.0" ]
# CMD [ "/bin/bash" ]