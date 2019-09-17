use mysql;
update mysql.user set authentication_string=password("Jilin963389970") where user="root";
update user set plugin="mysql_native_password";
flush privileges;

