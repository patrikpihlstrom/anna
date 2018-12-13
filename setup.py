import os
import codecs
from setuptools import setup

readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
description = None

with codecs.open(readme_path, mode='r', encoding='utf-8') as f:
    description = f.read()

setup(
    name='storobot',
    version='0.1',
    url='https://github.com/patrikpihlstrom/storobot',
    description=description,
    packages=['src'],
    install_requires=[
        'selenium'
    ]
)
