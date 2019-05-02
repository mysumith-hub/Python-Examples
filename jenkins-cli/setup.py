from setuptools import setup
setup(
    name = 'jenkins-cli',
    version = '1.0.0',
    packages = ['jenkins-cli'],
    entry_points = {
        'console_scripts': [
            'jenkins-cli = jenkins-cli.__main__:main'
        ]
    })
