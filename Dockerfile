FROM python:3.7-alpine

WORKDIR /px-ldap-replace

COPY * ./

RUN pip install -r requirements.txt && \
    python setup.py install

ENTRYPOINT ["px-ldap-replace"]


