from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='PJdilly',
   version='1.0',
   description='Test for Dillygence',
   license="MIT",
   long_description=long_description,
   author='Hongbo ZHANG',
   author_email='zhbinsa@gmail.com',
   url="https://github.com/hbzhinsa",
   packages=['PYdilly'],  #same as name
   #install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
)