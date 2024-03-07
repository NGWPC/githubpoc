FROM rockylinux/rockylinux:9

WORKDIR /app

RUN echo "Hello, World!" > hello.txt

CMD cat hello.txt
