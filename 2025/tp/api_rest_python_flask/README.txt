pip install Flask
---------------
flask --app hello run
----------------
http://127.0.0.1:5000
http://127.0.0.1:5000/hello
----------------
flask --app devise_api run
flask --app devise_api run --port 5005 --host 0.0.0.0
------------------
http://127.0.0.1:5000/devise-api/v1/devises/
http://localhost:5000/devise-api/v1/devises/
http://127.0.0.1:5000/devise-api/v1/devises/USD
http://127.0.0.1:5000/static/index.html

--------------------
docker run --name my_python -p5005:5000 -d my_python_image
http://127.0.0.1:5005/static/index.html ou autre (à tester via curl et via navigateur)
docker container stop my_python
docker container rm my_python
----------------
pytest -s
-------
doc sur test unitaires avec flask : https://www.digitalocean.com/community/tutorials/unit-test-in-flask

