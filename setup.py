# setup.py script for geomdl.shapes
from setuptools import setup
import os
import re


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


# Implemented from http://stackoverflow.com/a/41110107
def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(project + '/__init__.py').read())
    return result.group(1)


data = dict(
    name='geomdl.shapes',
    version=get_property('__version__', 'geomdl/shapes'),
    description='Generate common shapes with geomdl',
    long_description=read('README.rst'),
    license='MIT',
    author='Onur Rauf Bingol',
    author_email='nurbs-python@googlegroups.com',
    url='https://github.com/orbingol/geomdl-shapes',
    keywords='NURBS B-Spline curve surface volume CAD modeling visualization',
    packages=['geomdl.shapes'],
    install_requires=['geomdl>=5.0b5'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    project_urls={
        'Source': 'https://github.com/orbingol/geomdl-shapes',
        'Tracker': 'https://github.com/orbingol/geomdl-shapes/issues',
    },
)

if __name__ == '__main__':
    setup(**data)
