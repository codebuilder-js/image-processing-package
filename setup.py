from setuptools import setup, find_packages

with open("README.md", "r") as f:
  page_description = f.read()

with open("requirements.txt") as f:
  requirements = f.read().splitlines()

setup(
  name="image-processing-test",
  version="0.0.2",
  author="Rafael Correa de Lima",
  author_email="rafael.script@gmail.com",
  description="Image processing package. This project belongs to Karina Tiemi Kato, Tech Lead, Machine Learning Engineer, Data Scientist Specialist at Take. This package is a demo for simulation of upload on the Test Pypi website, and it's from the Bootcamp developer full stack Python class. E-mail: karinatkato@gmail.com.",
  long_description="text/markdown",
  url="https://github.com/codebuilder-js/image-processing-package/",
  packages=find_packages(),
  install_requirements=requirements,
  python_requires='>=3.8',
)
