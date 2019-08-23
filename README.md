
Implements a simple Reg-ex replace for LDAP

This code is based upon px-ldap-group-cleanup

## Development environment

### PipEnv

Install dependencies
```bash
pipenv install
```

Execute the script directly
```bash
pipenv run ./px-ldap-replace
```

or activate the venv-first
```bash
pipenv shell
./px-ldap-replace
```


### Pip

Install dependencies
```bash
pip install -r requirements-devel.txt
```

Dynamically linking to the repo
```bash
python setup.py develop
```


## Installation

Install dependencies
```bash
pip install -r requirements.txt
```

Statically install the script
```bash
python setup.py install
```


## Configuration

All parameters set via command-line can also be set in the config.
Every config-parameter is optional.

`~/.config/px-ldap-replace.yaml`:
```yaml
---
# the ldap-servers domain-name or IP
host: ldap.example.org
# where to start searches
search_base: dc=example,dc=org
# object-filter defaults to '(objectclass=inetOrgPerson)'
search_filter: '(objectclass=groupOfUniqueNames)'
# user-dn for bind
bind_dn: cn=my-script-user,ou=admins,dc=example,dc=org
# user password
bind_pw: <better-use-stdin>
# LDAP-attributes to modify (defaults to all)
attributes: '*'
# regex search pattern
pattern: Foo
# regex replacement string
repl: Bar
...

```

## Example

If no password is is defined it will be requested via `getpass`:
```bash
px-ldap-replace \
  --host='ldap.example.org' \
  --search-base='dc=example,dc=org' \
  --bind-dn='cn=my-script-user,ou=admins,dc=example,dc=org' \
  --pattern='bad' \
  --repl='good'
```
