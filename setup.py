from setuptools import setup

setup(
    name='weatherapi',
    version='0.0.3',
    author='Martin Conur',
    author_email='martincontrerasur@gmail.com',
    packages=['weatherapi'],
    scripts=[],
    url='https://pypi.org/project/weatherapi/',
    license='LICENSE',
    description='weatherapi.com python access',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "requests >= 2.26.0"
    ],
)