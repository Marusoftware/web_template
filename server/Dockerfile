FROM python:3.10.9-slim

WORKDIR /usr/src/app/server
COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN adduser --system --shell /bin/bash nonroot && \
    pip install --no-cache-dir --upgrade poetry wheel pysu && \
    chmod +rx /usr/local/bin/docker-entrypoint.sh

USER nonroot

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry install --no-cache --no-root --with dev --with postgres

USER root
EXPOSE 8000
ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]
CMD poetry run aerich upgrade && poetry run uvicorn --host 0.0.0.0 --port 8000 --reload changeme:app
