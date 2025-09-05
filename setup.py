from setuptools import setup, find_packages

setup(
    name='databases_companion',
    version='0.1.2',
    description='Auxiliary modules for database libraries',
    author='Ioannis Tsakmakis, Nikolaos Kokkos',
    author_email='itsakmak@envrio.org, nkokkos@envrio.org',
    packages=find_packages(),
    python_requires='>=3.12',
    install_requires=[
        'envrio_logger @ git+ssh://git@github.com/Envrio-hub/envrio_logger.git@0.1.0'
    ],
    classifiers=[  
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.12',
        'Framework :: Flask',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
