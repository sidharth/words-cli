from setuptools import setup
import sys

setup(
	name='words-cli',
	description='Learn some new words!',
	long_description='Preparing for the SAT/GRE/GMAT? Why not put those extra seconds of free time to some good use with this awesome CLI!'
	version='0.0.1',
	author='Sidharth Raja',
	author_email='sidharth15.raja@gmail.com'
	license='MIT',
	keywords='words word vocabulary gre gmat sat language',
	url='https://github.com/sidharth/words-cli',
	packages=['words-cli'],
    install_requires=[
        "click>=5.0",
    ],
    entry_points = {
        'console_scripts': [
        	'word = word.main:main'
      ],
    }
)
