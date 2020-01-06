FROM python:3.7-slim-stretch AS base

ENV PYROOT /pyroot
ENV PYTHONUSERBASE $PYROOT


FROM base as builder

RUN apt update && \
    apt install -y python-pip && \
    apt -y clean && \
    pip install pipenv

# Update pipenv libs
COPY Pipfile* ./
RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 pipenv install --system --deploy --ignore-pipfile


FROM base

ARG CHROMEDRIVER_VERSION=79.0.3945.36

WORKDIR /root

RUN apt update && \
    apt install -y wget curl gnupg && \
    apt -y clean

# Chrome
RUN curl -sS -o - 'https://dl-ssl.google.com/linux/linux_signing_key.pub' | apt-key add
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt update && \
    apt install -y wget unzip \
        libx11-xcb1 libxcb1 libxcursor1 libxdamage1 libxext6 libnss3 libcups2 libxss1 libxrandr2 libasound2 libpangocairo-1.0-0 libatk1.0-0 libatk-bridge2.0-0 libgtk-3-0 \
        google-chrome-stable gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils && \
    apt -y clean

# Chromedriver
RUN wget -q https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip || exit 0 && \
    unzip chromedriver_linux64.zip -d /usr/sbin && \
    rm -f chromedriver_linux64.zip

# Python libs and sources
COPY --from=builder $PYROOT/lib/ $PYROOT/lib/
COPY flight-selenium.py .

CMD ["python", "flight-selenium.py"]
