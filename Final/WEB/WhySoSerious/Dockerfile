FROM openjdk:8-jre-slim

WORKDIR /app

# 将 JAR 文件复制到容器中
COPY WhySoSerious-0.0.1-SNAPSHOT.jar /app/

# 设置环境变量
ENV GZCTF_FLAG=""

# 在容器启动时创建 /flag 文件并进行替换
CMD echo "flag{testflag}" > /flag && sed -i "s/flag{testflag}/$GZCTF_FLAG/" /flag && java -jar WhySoSerious-0.0.1-SNAPSHOT.jar
