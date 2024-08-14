from setuptools import find_packages
from setuptools import setup

setup(
    name="reshadow",
    version="0.0.22",
    license="GNU General Public License v2.0",
    author="Ali Can Gönüllü",
    author_email="alicangonullu@yahoo.com",
    description="PyShadow - ShadowCopy Anaylze Tool",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/alicangnll/pyshadow",
    project_urls={"Bug Report": "https://github.com/pyshadow/pymem/issues/new"},
    install_requires=["pywin32"],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["reshadow"],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)