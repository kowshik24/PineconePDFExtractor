import os
from setuptools import setup, find_packages

# Get the current directory where setup.py is located
here = os.path.abspath(os.path.dirname(__file__))

# Open README.md with the correct path
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PineconePDFExtractor',
    version='0.1.1',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='A library to process PDF files for Pineone',
    author='Kowshik Deb Nath',
    author_email='kowshikcseruet1998@gmail.com',
    url='https://github.com/kowshik24/PineconePDFExtractor',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        'PyPDF2==3.0.1',
    ],
)