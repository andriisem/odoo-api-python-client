from setuptools import setup
from setuptools import find_packages

setup(name='odooapiclient',
      version='0.5',
      description='Odoo API Client',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Andrii Semko',
      author_email='semko.andrey.i@gmail.com',
      url='https://github.com/andriisem/odoo-api-python-client.git',
      packages=find_packages(),
)
