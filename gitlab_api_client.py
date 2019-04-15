import gitlab
from config import gitlab_host, gitlab_token


def connect():
    gl = gitlab.Gitlab(gitlab_host, private_token=gitlab_token)
    gl.auth()
    return gl

def get_groups():
    gl = connect()
    all_groups = gl.groups.list(all=True, owned=True)
    all_group_names = []
    for group in all_groups:
        all_group_names.append(group.name)
    return all_group_names

if __name__=='__main__':
    print(get_groups())
