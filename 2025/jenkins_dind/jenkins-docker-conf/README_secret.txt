cd secrets
echo temp_or_real_pwd > .d2f_dockerhub_pwd
=======
NB: le fichier jenkins-docker-conf/secrets/.d2f_dockerhub_pwd
doit être créé (même éventuellement à vide)
il comportera normalement le mot de passe nécessaire à la connexion à dockerhub (docker_registry)

OU BIEN
remplacer le contenu de docker-compose.yaml par celui de docker-compose.simple.yaml
