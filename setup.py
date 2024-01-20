from setuptools import setup, find_packages

setup(
    name='PineconePDFExtractor',
    version='0.1',
    packages=find_packages(),
    long_description=open('README.md').read(),
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