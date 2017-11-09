"""
Parse relevant data from YAML file into BASH commands.
"""

from sys import argv
from yaml import load


BLOCK = "Test"
KEYS = ["gambit", "expected", "rtol"]


def yaml_to_bash(yaml_name):
    """
    :param yaml_name: Name of YAML file
    """
    with open(yaml_name) as yaml_file:
        data = load(yaml_file)
  
    bash = ['{}_{}="{}"'.format(BLOCK, k, data[BLOCK][k]) for k in KEYS]
    bash = ";".join(bash)
    return bash

   
if __name__ == "__main__":
    
    assert len(argv) == 2
    yaml_name = argv[1]
    print yaml_to_bash(yaml_name)
    
    