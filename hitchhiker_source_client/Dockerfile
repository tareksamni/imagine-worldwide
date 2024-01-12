FROM ruby:3.2

ENV HITCHHIKER_HOST=127.0.0.1
ENV HITCHHIKER_PORT=50051

WORKDIR /usr/src/app

RUN gem install grpc

COPY . /usr/src/app/

CMD ["ruby", "main.rb"]
