1) récupérer la dernière version du code via git et reconstruire demo.jar et l'image docker xyz/demo
   via Jenkins et job en version pipeline
2) télécharger l'image mariadb en version 10 ou MySQL en version 8
   docker image pull mariadb:10
3) se placer dans le répertoire /vagrant/conf-docker
4) lancer la commande suivante:
   docker-compose up &
------------------
NB: avec mariadb:latest (11.x) la connexion ne se faisait pas bien via le connecteur MySQL de l'application SpringBoot
    par contre avec mariadb:10 la connexion s'établit bien (mariadb:10 est mieux compatible avec mysql8 que mariadb11)
------------------
PB rencontré le mercredi 11/09 vers 17 résolu en remplaçant image mariadb:latest par mariadb:10
ça a fonctionné à 21h sur le PC du formateur et avec le code actuel du référentiel https://github.com/didier-tp/devOpsSeptembre2024
------------------
tester via http://localhost:8282 