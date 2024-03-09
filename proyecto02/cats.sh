#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp cats.py tempdir/
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile

echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY cats.py /home/myapp/" >> tempdir/Dockerfile
# Añade la copia de la carpeta 'img' dentro de 'static'
echo "COPY ./static/img /home/myapp/static/img/" >> tempdir/Dockerfile

echo "EXPOSE 5270" >> tempdir/Dockerfile

echo "CMD python3 /home/myapp/cats.py" >> tempdir/Dockerfile

cd tempdir

docker build -t catpage .

docker run -t -d -p 5270:5270 --name catpagebroh catpage

docker ps -a

