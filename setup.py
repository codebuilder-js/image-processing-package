from setuptools import setup, find_packages

with open("README.md", "r") as f:
  page_description = f.read()

with open("requirements.txt") as f:
  requirements = f.read().splitlines()

setup(
  name="package_name",
  version="0.0.1",
  author="my_name",
  author_email="my_email",
  description="My short description",
  long_description="text/markdown",
  url="my_github_repository_projetct_link",
  packages=find_packages(),
  install_requirements=requirements,
  python_requires='>=3.8',
)
