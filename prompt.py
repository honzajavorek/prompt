import os
import re
import subprocess
from pathlib import Path


VIRTUAL_ENV = os.getenv('VIRTUAL_ENV')


# https://stackoverflow.com/a/33206814/325365
COLOR_CYAN = '\033[1;36m'
COLOR_YELLOW = '\033[1;33m'
COLOR_LIGHT_RED = '\033[1;31m'
COLOR_GRAY = '\033[1;37m'
COLOR_RESET = '\033[0m'


def c(text, color_code):
    return f'{color_code}{text}{COLOR_RESET}'


cwd = Path(os.getcwd())
venv_path = Path(VIRTUAL_ENV) if VIRTUAL_ENV else None


if venv_path:
    if venv_path.parent == cwd:
        venv_name = venv_path.name
    else:
        home = str(Path.home())
        venv_segment = str(venv_path).replace(home, '~')
        cwd_segment = str(cwd).replace(home, '~') + '/'
        venv_name = venv_segment.replace(cwd_segment, '')
    venv = f'({venv_name})'
else:
    venv = None


is_git_dir = False
for tested_dir in ([cwd] + list(cwd.parents)):
    is_git_dir = (tested_dir / '.git').exists()
    if is_git_dir:
        break


if is_git_dir:
    git_branch_output = subprocess.getoutput('git rev-parse --abbrev-ref HEAD')
    git_branch_name = git_branch_output.strip()
    if git_branch_name:
        git_branch = c(f'[{git_branch_name}]', COLOR_YELLOW)
    else:
        git_branch = None
else:
    git_branch = None


prompt = ' '.join(filter(None, [
    venv,
    c('\w', COLOR_CYAN),  # path
    git_branch
]))
print(f'\n{prompt}\n\$ ')
