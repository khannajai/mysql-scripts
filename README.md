# Gitlab and MySQL setup for a Databases course

## Gitlab setup

https://docs.gitlab.com/omnibus/docker/

After running your Gitlab docker container on an internal server, create groups and repositories for students to push their HWs.

## Create databases for each group.

Once the groups have been set up, we have to create MySQL users and databases for each group. For this, we will run a Python script that will generate MySQL scripts to be imported.

First, set up the environment variables, for example:

```
export GITLAB_HOST="mygitlab.jacobs-university.de"
export GITLAB_TOKEN="sometoken"
```

Make sure your Gitlab token has access to read all groups. 

Setup your `virtualenv` and install required packages into it:
```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Now, run the script `python create_mysql_scripts.py`.

This will read all groups from Gitlab, and will generate two MySQL scripts: one, to create MySQL users and databases for each group, and the other to delete those users and databases.

Another file, `mysql_user_credentials.txt`, will contain the generated MySQL usernames and passwords for the student groups.