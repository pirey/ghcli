import argparse
import requests

parser = argparse.ArgumentParser(
    prog='ghcli', description='Github cli.')
parser.add_argument('username', metavar='username', type=str,
                    help='Github username')
parser.add_argument('--all', action='store_true',
                    help='Show complete profile info.')
args = parser.parse_args()

print()

r = requests.get('https://api.github.com/users/%s' % args.username)
if r.status_code == 404:
    print('User not found')
    quit(1)
elif r.status_code != 200:
    print('Uh oh something went wrong, sorry')
    quit(1)

profile = r.json()
if (args.all):
    profile = r.json()
    for key in profile:
        print('%s : %s' % (key, profile[key]))
else:
    print('%s - %s' % (profile['login'], profile['bio']))
    print('-------------------')
    print('following : %s' % profile['following'])
    print('followers : %s' % profile['followers'])
    print('public repos : %s' % profile['public_repos'])
    print('public gist : %s' % profile['public_gists'])

