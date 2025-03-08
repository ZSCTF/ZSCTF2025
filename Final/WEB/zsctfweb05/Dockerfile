# 使用基于 Debian Jessie 的基础镜像
FROM vulhub/phpmyadmin:4.4.15.6

# 设置环境变量
ENV FLAG=flag{your_flag_here}

# 复制配置文件
COPY ./config.inc.php /var/www/html/config.inc.php

# 修改权限
RUN chown -R www-data:www-data /var/www/html

# 替换为 Debian 存档源
RUN echo "deb http://archive.debian.org/debian jessie main" > /etc/apt/sources.list && \
    echo "deb http://archive.debian.org/debian-security jessie/updates main" >> /etc/apt/sources.list && \
    echo "Acquire::Check-Valid-Until false;" > /etc/apt/apt.conf.d/99no-check-valid && \
    echo "APT::Get::AllowUnauthenticated true;" >> /etc/apt/apt.conf.d/99no-check-valid && \
    apt-get update -o Acquire::AllowInsecureRepositories=true && \
    apt-get install -y --force-yes mysql-server-5.5 && \
    rm -rf /var/lib/apt/lists/*

# 初始化 MySQL
RUN service mysql start && \
    mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'root';" && \
    mysql -e "CREATE DATABASE test;" && \
    mysql -e "FLUSH PRIVILEGES;"

# 暴露端口
EXPOSE 80 3306

# 启动服务
CMD service mysql start && apache2-foreground