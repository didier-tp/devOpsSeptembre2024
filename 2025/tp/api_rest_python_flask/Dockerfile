#FROM python:3.9
FROM python:3.13
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
#specific default port : 5005 , default url : http://127.0.0.1:5005/static/index.html
#si docker run --name my_python -p5005:5005 -d my_python_image
#debug via docker container exec -ti my_python sh
#alors http://127.0.0.1:5005/static/index.html
CMD ["flask", "--app" , "devise_api", "run" , "--port" , "5005"  , "--host" , "0.0.0.0"]