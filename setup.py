import setuptools

with open('README.md', 'r') as f:
    description = f.read()

setuptools.setup(
    name='libanna',
    version='1.0.0',
    author='Patrik Pihlstrom',
    author_email='patrik.pihlstrom@gmail.com',
    url='https://github.com/patrikpihlstrom/anna',
    description='simulated & automated end-to-end website testing software',
    long_description=description,
    long_description_content_type='text/markdown',
    packages=['anna'],
    entry_points={'anna': ['anna = anna.__main__:main']},
    install_requires=[
        'selenium'
    ]
)
