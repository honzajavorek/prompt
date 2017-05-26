# prompt

My bash prompt.

## Demo

```bash
20:36 (env) ~/Projects/python.cz [master]
$ cd ..

20:36 (python.cz/env) ~/Projects
$ ⎜
```

## Installation

Make sure you have Python 3 installed:

```bash
$ brew install python3
```

Put following to your `.bash_profile` (or equivalent file):

```bash
function set_bash_prompt () {
  PS1=$(python3 ~/path/to/the/file/prompt.py)
}
PROMPT_COMMAND=set_bash_prompt
```

## License

MIT
