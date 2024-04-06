from setuptools import setup,find_packages

HYPEN_E_DOT="-e ."
def get_requirements(requirement):
    requirements=[]

    with open(requirement) as file_obj:
        requirements=file_obj.readlines()
        requirements=[lib.replace("\n","") for lib in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="source_code_analysis",
    version="0.0.1",
    author="kps",
    author_email="kps@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)

        