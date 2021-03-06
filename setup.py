from pathlib import Path
from setuptools import setup, find_packages
import os


def read_requirements(path):
    return list(Path(path).read_text().splitlines())


setup(
      name='u8timeseries',
      version="1.1.0",
      description='A collection of easy-to-use timeseries forecasting models',
      url='http://github.com/unit8co/u8timeseries',
      author='Unit8 SA',
      author_email='info@unit8.co',
      license='Apache License 2.0',
      packages=find_packages(),
      install_requires=read_requirements('requirements/main.txt'),
      zip_safe=False,
      python_requires='>=3.6'
)
