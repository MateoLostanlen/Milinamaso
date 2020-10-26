#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Package installation setup
"""

import os
import subprocess
from setuptools import setup, find_packages

version = '0.1.0a0'
sha = 'Unknown'
package_name = 'milinamaso'

cwd = os.path.dirname(os.path.abspath(__file__))

try:
    sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=cwd).decode('ascii').strip()
except Exception:
    pass

if os.getenv('BUILD_VERSION'):
    version = os.getenv('BUILD_VERSION')
elif sha != 'Unknown':
    version += '+' + sha[:7]
print("Building wheel {}-{}".format(package_name, version))


def write_version_file():
    version_path = os.path.join(cwd, 'milinamaso', 'version.py')
    with open(version_path, 'w') as f:
        f.write("__version__ = '{}'\n".format(version))


write_version_file()

with open('README.md') as f:
    readme = f.read()

requirements = [
	'pylocron>=0.1.2',
    'torch>=1.5.1',
    'torchvision>=0.6.1',
    'tqdm>=4.1.0',
    'numpy>=1.17.2',
    'fastprogress>=1.0.0',
    'matplotlib>=3.0.0',
    'contiguous_params@git+https://github.com/philjd/contiguous_pytorch_params.git#egg=contiguous_params',
]

setup(
    name=package_name,
    version=version,
    author='Mateo Lostanlen',
    description='Everything necessary to train a computer vision model in PyTorch',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='hhttps://github.com/MateoLostanlen/Milinamaso',
    download_url='https://github.com/MateoLostanlen/Milinamaso/archive/v_1.0.tar.gz',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['pytorch', 'deep learning', 'vision', 'models'],
    packages=find_packages(exclude=('test',)),
    zip_safe=True,
    python_requires='>=3.6.0',
    include_package_data=True,
    install_requires=requirements,
    package_data={'': ['LICENSE']},
)
