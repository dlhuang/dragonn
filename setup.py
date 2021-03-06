from setuptools import setup,find_packages

config = {
    'include_package_data': True,
    'description': 'Deep RegulAtory GenOmic Neural Networks (DragoNN)',
    'version': '0.2.6',
    'packages': ['dragonn'],
    'setup_requires': [],
    'install_requires': ['numpy>=1.15', 'keras>=2.2.0','tensorflow>=1.6','deeplift>=0.6.9.0', 'shapely', 'matplotlib',
                         'scikit-learn>=0.20.0', 'pydot_ng==1.0.0', 'h5py','concise','seqdataloader>=0.124','simdna_dragonn','abstention'],
    'extras_requires':{'tensorflow with gpu':['tensorflow-gpu>=1.7']},
    'dependency_links': [],
    'scripts': [],
    'entry_points': {'console_scripts': ['dragonn = dragonn.__main__:main']},
    'name': 'dragonn'
}

if __name__== '__main__':
    setup(**config)
