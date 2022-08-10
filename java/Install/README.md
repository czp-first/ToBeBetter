
# ubuntu20.04 install java8
```shell
apt update
apt install openjdk-8-jdk -y

java -version

vim /etc/profile.d/openjdk.sh
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin

source /etc/profile
```

