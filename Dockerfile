FROM python:3.8
LABEL MAINTAINER = "mohammadrzapodineh | mohammadrzapodineh.ir | sunlearn.ir"
ENV PYTHONUNBUFFERED 1
WORKDIR /code/
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py collectstatic --no-input
CMD ["gunicorn", "--chdir", "SmartBlog", "--bind", ":8000", "SmartBlog.wsgi:application"]