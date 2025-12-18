#installation de image docker java21/maven
docker image pull maven:3.9-amazoncorretto-21-debian


#verification de l'image docker java21/maven
docker container run -t -i maven:3.9-amazoncorretto-21-debian bash
# java --version
# mvn --version
# exit


#installation de image docker node:24
#docker image pull node:24

#construction de l'image node_ts_cypress (basée sur node:24)
#lancer le script build-docker-images/build_node_ts_cypress_image.sh
#après avoir visualiser (et éventuellement ajuster) build-docker-images/node_ts_cypress/Dockerfile

#verification de l'image docker node_ts_cypress 
docker container run -t -i node_ts_cypress bash
# node --version
# npm --version
# tsc --version
# http-server --version
# npx cypress --version
# exit

====================

Vérification du container docker correspondant au controleur Jenkins:

docker container exec -ti jenkins_controller_container bash