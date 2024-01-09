from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    """Downloads all the nessasary files required for the project"""

    requriements = []

    with open(file_path) as f:
        requriements = f.readlines()
        requriements = [req.replace("\n", "") for req in requriements if req != "-e ."]

        if "-e ." in requriements:
            requriements.remove("-e .")
        
    return requriements
    
setup(
    name = "Plant Detection",
    version= "0.0.1",
    author= "Sauren",
    author_email="sharmasaurenb@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
)