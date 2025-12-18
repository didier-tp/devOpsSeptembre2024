ce répertoire doit (lors du lancement de Jenkins) comporter un fichier .d2f_dockerhub_pwd
comportant le mot de passe nécessaire à une connexion sur dockerhub
--------
ce fichier "secret" ne doit absolument pas être placé dans un référentiel git
---- 
on pourra créer ce fichier via la commande suivante:
cd secrets
echo temp_or_real_pwd > .d2f_dockerhub_pwd
---
ce fichier sera pris en compte par:
jenkins-docker-conf/docker-compose.yml
jenkins-docker-conf/dockerfiles/Jenkins.yaml
voyant ce fichier via ${readFile:/run/secrets/jenkins_d2f_dockerhub_pwd}