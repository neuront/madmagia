import os.path
from setuptools import setup, find_packages

_URI = 'https://github.com/neuront/madmagia'

setup(
    name='madmagia',
    version='0.9.0',
    author='Neuron Teckid',
    author_email='lene13@gmail.com',
    license='MIT',
    keywords='Video Slice Merge Script',
    url=_URI,
    description='Python video slicing / merging script toolkit',
    packages=['madmagia'],
    long_description='Visit ' + _URI + ' for details please.',
    install_requires=[],
    zip_safe=False,
    entry_points=dict(
        console_scripts=[
            'madinit=madmagia.init:main',
            'madslice=madmagia.partial:slice',
            'madinspect=madmagia.partial:inspect',
            'madexport=madmagia.partial:export',
            'madsrt=madmagia.export_srt:srt',
            'madlrc=madmagia.export_srt:lrc',
            'madframe=madmagia.view_frame:main',
        ],
    ),
)