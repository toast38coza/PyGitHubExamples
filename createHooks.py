"""
This will create service hooks for integrating your repo with external services like Github
"""

#!/usr/bin/python                                                                    

import sys
sys.path.append("./PyGithub");
from github import Github

import getpass
import argparse


from github import Github
from github import GithubException

parser = argparse.ArgumentParser(description='List all repos for an org')
parser.add_argument('repoName',help='github Repo name')

args = parser.parse_args()

username = raw_input("Github Username:")
pw = getpass.getpass()
g = Github(username, pw)
repoName = args.repoName

try:
    repo = g.get_repo(repoName)
except GithubException as ghe:
    print(ghe)

## this is where we create the actual repo: 
# for clarity in the exmaple, I will simply hardcode the details:
# note: for the below you would need appropriate settings to be defined

repo_hooks = [ ## (name,config)
    ( 'campfire', {'room': settings.CAMPFIRE_ROOM_NAME, 'sound': '', 'subdomain': settings.CAMPFIRE_SUBDOMAIN,'token': settings.CAMPFIRE_AUTH_ID } ),
    ( 'pivotaltracker', {'branch': '', 'endpoint': '', 'token': settings.PIVOTAL_TOKEN } )
]

"""
tip: if you want to see what an example config looks like. On a repo that has hooks defined, do: 
hooks = repo.get_hooks:
for hook in hooks:
    print hook.__dict__

This will fetch hooks from an existing repo, and print out their details. 
You will need the name and config details to configure a hook on a repo with the API as above
"""

try:
    for name,hook in repo_hooks:
        repo.create_hook(name,hook)
except GithubException as ghe:
    print(ghe)
