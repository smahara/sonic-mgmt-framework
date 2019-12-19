#!/bin/sh

openssl genrsa -out $PWD/key.pem 2048

openssl req -new -x509 -key $PWD/key.pem -out $PWD/cert.pem -config /etc/ca.conf -days 3650
