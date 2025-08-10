"""
The setup.py file is an essential part of packaging and distributing Python projects. 
It is used by setuptools to define the configuration of your projects, such as its metadata,
dependencies and more.
"""


from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]: 
    """
    This function will return the list of requirements
    """
    requirement_list:List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            # Read lines from the file
            lines = file.readlines()

            # Process each lines
            for line in lines:
                requirement = line.strip()

                # Ignore the empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Kavya Bansal",
    author_email="kavyabansal2000@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)