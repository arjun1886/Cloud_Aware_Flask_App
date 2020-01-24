FROM python:3.6-alpine
WORKDIR /app


COPY . /app


RUN apk update
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
RUN pip install -r requirements.txt


RUN apk add python3-dev
RUN pip install pymysql



EXPOSE 5003
EXPOSE 3306
EXPOSE 80




ENV TEAM_ID=CC_140_148_153_213


CMD ["python3", "cc_acts.py"]
