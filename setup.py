import setuptools

with open('README.md', 'r') as f:
    description = f.read()

setuptools.setup(
    name='magebot',
    version='0.1.2',
    author='Patrik Pihlstrom',
    author_email='patrik.pihlstrom@gmail.com',
    url='https://github.com/patrikpihlstrom/mage-bot.git',
    description='simulated & automated testing software',
    long_description=description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=[
        'selenium'
    ]
)
