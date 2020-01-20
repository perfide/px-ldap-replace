FROM python:alpine

WORKDIR /opt/px-ldap-replace

COPY * ./

RUN pip install --requirement=requirements.txt && \
    python setup.py install

ENTRYPOINT ["px-ldap-replace"]
