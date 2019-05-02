Jenkins CLI
------------
- python3 -m venv jenkins-cli
- source jenkins-cli/bin/activate
- Create a package with following files
  ├─jenkins-cli
    ├── __init__.py  - This file (empty) is there to tell Python that directory contains a package
    ├── __main__.py
    ├── <any_class_files>.py
  ├─setup.py - The setup.py file is what ties it all together and tells Python how to handle it

This is positional argument`
parser.add_argument('jobname', help='Enter Job name')

This is optional argument`
parser.add_argument('--jobname', help='Enter Job name')
