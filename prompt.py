import os
import re
import subprocess
import datetime


color_blue = '\033[1;34m'
color_yellow = '\033[1;33m'
color_light_red = '\033[1;31m'
color_gray = '\033[1;37m'
color_reset = '\033[0m'


def c(text, color_code):
    return f'{color_code}{text}{color_reset}'


now = datetime.datetime.now()
time = c('{:%H:%M}'.format(now), color_gray)


path = c('\w', color_blue)


virtual_env_path = os.getenv('VIRTUAL_ENV')
if virtual_env_path:
    cwd = os.getcwd()
    if os.path.dirname(virtual_env_path) == cwd:
        virtual_env_name = os.path.basename(virtual_env_path)
    else:
        home = os.path.expanduser('~')
        venv_segment = virtual_env_path.replace(home, '~')
        cwd_segment = cwd.replace(home, '~') + '/'
        virtual_env_name = venv_segment.replace(cwd_segment, '')
    virtual_env = f'({virtual_env_name})' # c(f'({virtual_env_name})', color_yellow)
else:
    virtual_env = None


git_branch_output = subprocess.getoutput('git branch --no-color 2> /dev/null')
match = re.search(r'\* (.+)', git_branch_output)
if match:
    git_branch_name = match.group(1)
    git_branch = c(f'[{git_branch_name}]', color_yellow)
else:
    git_branch = None


prompt = ' '.join(filter(None, [time, virtual_env, path, git_branch]))
print(f'\n{prompt}\n\$ ')
