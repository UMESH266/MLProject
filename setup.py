from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    """
    This function returns the list of libraries in requirements file.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements if req != '-e .']

    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='UMESH',
    author_email='umeshgoud143@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)