from gitlab_api_client import get_groups
from tools import random_string

def create_users_and_databases():
    f = open("create_users.sql","a+")
    g = open("mysql_user_credentials.txt", "a+")
    groups = get_groups()
    for group in groups:
        user = group.replace(" ", "_").replace("-","_")
        password = random_string()
        g.write("{}\t{}\n".format(user, password))
        f.write("CREATE DATABASE {};\n".format(user))
        f.write("CREATE USER {}@'localhost' IDENTIFIED BY '{}';\n".format(user, password))
        f.write("GRANT USAGE ON *.* TO {}@'%' IDENTIFIED BY '{}';\n".format(user, password))
        f.write("GRANT ALL PRIVILEGES ON {}.* TO {}@'%' IDENTIFIED BY '{}';\n".format(user, user, password))
    f.close()
    g.close()

def delete_users_and_databases():
    f = open("delete_users.sql", "a+")
    groups = get_groups()
    for group in groups:
        user = group.replace(" ", "_").replace("-","_")
        f.write("DROP DATABASE {};\n".format(user))
        f.write("REVOKE ALL PRIVILEGES, GRANT OPTION FROM {}@'%';\n".format(user))
        f.write("DROP USER {}@'localhost';\n".format(user))
        f.write("DROP USER {}@'%';\n".format(user))
    f.close()

if __name__=='__main__':
    create_users()
    delete_users()

