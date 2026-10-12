# pip,virtual environment,.env file
# pip:pip installs packages.package manager

# virtual environments : A 'venv' is a directory that contains 
# 1. a copy of the python interpreter
# 2.  its own 'pip'
# 3. its won site-packages directory.Default target location 
# where python installs third party libraries
# 4. activation scripts that modify PATH

python --version 


python -m venv .venv

# activate 
.venv\scripts\activate.bat 

# deactivate
deactivate

#pip installation(install dependencies/libraries)
pip install pacakage_name # syntax

