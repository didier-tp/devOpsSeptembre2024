1) récupérer le code source de l'appli java/springBoot via git
------------------------
git clone https://github.com/didier-tp/devOpsSeptembre2024 
ou autre

2) construire l'application java via maven
----------------------------------
cd devOpsSeptembre2024/tp/appliJava/demo ou autre (là où il y a pom.xml)
mvn clean package
cd target
ls   (pour vérifier si demo.jar est bien généré)

3) construire l'image docker depuis le fichier Dockerfile
-------------------------------------------------------
cd .. (là ou il y a Dockerfile)
docker image build -t xyz/demo .
docker image ls

4) lancer le conteneur docker à partir de l'image construite:
-------------------------------------------------------
docker container run -d -p 8282:8181 xyz/demo
docker container ls
curl http://localhost:8282/demo/index.html