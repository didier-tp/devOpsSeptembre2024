git clone ….
cd …/demo  (là où il ya pom.xml)
mvn package
cd target
ls
cd ..
docker image build -t xyz/demo .
docker image ls


docker container run -d -p 8282:8181 xyz/demo
docker container ls