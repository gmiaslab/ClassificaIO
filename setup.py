"""
setup.py for ClassificaIO package
"""
from setuptools import setup, find_packages
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description=f.read()

setup(
    name='ClassificaIO',
    packages=find_packages(),
    version='1.1.2',
    description='Graphical User Interface for machine learning classification algorithms from scikit-learn',
    long_description=long_description,
    include_package_data=True,
    author='G. Mias Lab',
    author_email='gmiaslab@gmail.com',
    license='MIT',
    url='https://github.com/gmiaslab/ClassificaIO',
    download_url='https://github.com/gmiaslab/ClassificaIO/archive/1.1.2.tar.gz',
    keywords=['machine learning', 'classification','bioinformatics'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Topic :: Education',
        'Topic :: Utilities',
        ],
    install_requires=[
        'Pillow>=5.1.0',
        'pandas==0.22.0',
        'numpy>=1.14.3',
        'scikit-learn>=0.19.1',
        'scipy>=1.1.0'],
    zip_safe=False
)
