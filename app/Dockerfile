FROM python:alpine3.8
RUN pip install Flask
COPY . /src/.
ENV NAME=unknown
EXPOSE  80
CMD ["python", "/src/app.py", "-p 80"]
