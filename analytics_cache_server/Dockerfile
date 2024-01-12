FROM openwrt/rootfs:latest

ENV PORT=8080
ENV HOST=127.0.0.1

RUN mkdir -p /var/lock/ && \
    opkg update && \
    opkg install python3 python3-pip curl

ADD requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

ADD main.py /main.py

CMD ["python3", "main.py"]
