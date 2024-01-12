FROM openwrt/rootfs:latest

RUN mkdir -p /var/lock/ && \
    opkg update && \
    opkg install python3 python3-pip curl

ADD requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

ADD . /

CMD ["python3", "main.py"]
