FROM python:latest
ARG BUILD_DATE

LABEL build_version="Build-date:- ${BUILD_DATE}"
LABEL maintainer="Daniel Hufschläger"


COPY app ./
COPY app_frontend.py ./app/
COPY app_backend.py ./app/
COPY requirements.txt ./app/
COPY entrypoint.sh ./app/

RUN pip install --upgrade --no-cache-dir pip && \
    pip install --no-cache-dir -r ./app/requirements.txt && \
    chmod +x ./app/entrypoint.sh

EXPOSE 8002
ENTRYPOINT ["./app/entrypoint.sh"]