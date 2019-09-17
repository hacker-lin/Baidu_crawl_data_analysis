FROM mysql:5.7
ENV MYSQL_ALLOW_EMPTY_PASSWORD yes

ADD custom.cnf /etc/mysql/conf.d
COPY setup.sh /etc/mysql/setup.sh
COPY passwd.sql /etc/mysql/passwd.sql

# CMD ['sh', '/etc/mysql/setup.sh']
CMD sh /etc/mysql/setup.sh
# RUN sh /etc/mysql/setup.sh


