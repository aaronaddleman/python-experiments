"""
Python experiments
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='Python Experiments',
    version='0.0.1',
    description='Things to show off Python',
    long_description=long_description,
    url='https://github.com/aaronaddleman/python-experiements',
    author='Aaron Addleman',
    author_email='aaronaddleman@gmail.com',
    classifers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Testing',
        'License :: OSI Approvde :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='experiments',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.7, <4',
    install_requires=[],
    extra_requires={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    package_data={
        'sample': ['package_data.dat']
    },
    data_files=[('my_data', ['data/data_file'])],
    entry_points={
        'console_scripts': [
            'sample=sample:main'
        ]
    },
    project_urls={
        'Bug Reports': '',
        'Funding': '',
        'Say Thanks!': '',
        'Source': '',
    }
)