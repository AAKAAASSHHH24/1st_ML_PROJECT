from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """This function is going to return list of requirement 
    mention in requirements.txt file"""

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove('-e .')

#DECLARING VARIABLES
PROJECT_NAME = 'housing-price-predictor'
VERSION = '0.0.2'
AUTHOR = 'AKASH'
DESCRIPTION ='1ST ML PROJECT'
PACKAGES = ['housing']
REQUIREMENT_FILE_NAME = 'requirements.txt'





setup(
    name= PROJECT_NAME,
     version = VERSION, 
     author= AUTHOR, 
     description=DESCRIPTION, 
     packages= find_packages(), 
     install_requires = get_requirements()
     )