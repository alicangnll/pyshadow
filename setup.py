from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='reshadowcode',
    version='0.0.1',
    description='For Shadow Copy research in Windows',
    long_description=long_description,
    url='https://github.com/alicangnll/pyshadow',
    author='Ali Can Gönüllü',
    license='MIT',
    keywords=['Windows', 'VSS', 'win32', 'Shadow', 'Copy'],
    py_modules=['subprocess', 'pywin32'],
    install_requires=['pywin32', 're'],
)