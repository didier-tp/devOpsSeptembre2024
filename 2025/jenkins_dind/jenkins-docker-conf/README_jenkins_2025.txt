console d'admin: http://localhost:8888  (admin,admin)
----
complete docker volume name: jenkins-docker-conf_jenkins_home
----------

petit bug sur mémorisation des credentials, donc besoin de refaire partiellement/régulièrement:
Avec du temps, ça ce gère en améliorant le fichier jenkins-docker-conf/dockerfiles/jenkins.yaml
(doc : https://github.com/jenkinsci/configuration-as-code-plugin/tree/master/demos/credentials)

id:credential_dockerhub_didierdefrance69
username:didierdefrance69
password: MajSimpleDeuxF!   <---- partie pour l'instant à refaire après chaque redémarrage de jenkins

=====
pipelines:
tp_api , https://github.com/didier-mycontrib/tp-api , */main
ddc_api , https://github.com/didier-mycontrib/ddc-api , */main
ddc_app , https://github.com/didier-mycontrib/ddc-app , */main
qcm_api , https://github.com/didier-mycontrib/qcm-api , */main
qcm_app , https://github.com/didier-mycontrib/qcm-app , */main

