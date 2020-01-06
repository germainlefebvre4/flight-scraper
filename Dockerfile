FROM python:3-alpine as base

ENV PYROOT /pyroot
ENV PYTHONUSERBASE $PYROOT

ENV CHROMEDRIVER_URL = 'https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip'

WORKDIR /tmp
RUN apk update && \
    apk add wget unzip py-pip && \
    apk clean
RUN wget ${CHROMEDRIVER_URL} && \
    unzip chromedriver_linux64.zip -d /usr/src/app && \
    rm -f chromedriver_linux64.zip

WORKDIR /usr/src/app
COPY Pipfile* .
RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 pipenv install --system --deploy --ignore-pipfile
#RUN pip install pipenv && \
#    pipenv update


FROM base

COPY --from=builder $PYROOT/lib/ $PYROOT/lib/
COPY flight-selenium.py .

CMD ["python3", "main.py"]
