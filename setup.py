from numpy import long
from setuptools import setup, find_packages

setup(
    name='Modustry',
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        open('requirements.txt').read().split('\n'),
    ],
    entry_points={
        'console_scripts': [
            'modustry = sources.main:main'
        ],
    },
    author='',
    author_email='',
    description='A visual environment to make mod for Mindustry a lt easier.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", 
    ],
    python_requires='>=3.6',
)