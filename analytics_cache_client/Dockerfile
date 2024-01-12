FROM ruby:3.2

ENV ANALYTICS_SERVER_HOST=127.0.0.1
ENV ANALYTICS_SERVER_PORT=8080

WORKDIR /usr/src/app

COPY main.rb /usr/src/app/

CMD ["ruby", "main.rb"]
