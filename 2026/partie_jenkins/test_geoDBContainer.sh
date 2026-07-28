export serv=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' geoDBContainer)
echo $serv
mariadb -h ${serv} -uroot -ppwd
