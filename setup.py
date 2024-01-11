from setuptools import setup,find_packages
from typing import List
hyfan="-e."
def getfile(file:str)->List[str]:
    req=[]
    with open(file) as obj:
        req=obj.readlines()
        requirement=[reqe.replace("\n"," ") for reqe in req]
        if hyfan in requirement:
            requirement.remove(hyfan)
        
setup(name="MY FIRST ML PROJECT",version="0.0.1",author="SACHETAN HERALAGI",author_email="manuheralagi4@gmail.com",packages=find_packages(),install_requires=getfile("requirement.txt"))