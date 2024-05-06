FROM registry.sh.nextgenwaterprediction.com/infrastructure/rockylinux/rockylinux:9.3

RUN dnf install -y python pip

WORKDIR /app

COPY . .

RUN pip install .

CMD ["simple_server"]
