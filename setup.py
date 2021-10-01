from setuptools import setup

setup(
    name='wapi',
    version='0.0.1',
    author='Martin Conur',
    author_email='martincontrerasur@gmail.com',
    packages=['wapi'],
    scripts=[],
    url='http://pypi.python.org/pypi/wapi/',
    license='LICENSE.txt',
    description='weatherapi.com python access',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 2.26.0"
    ],
)