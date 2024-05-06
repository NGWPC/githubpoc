from setuptools import setup, find_packages

setup(
    name='simple_server',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'simple_server=simple_server.simple_server:main'
        ]
    },
    install_requires=[],
    extras_require={
        'testing': ['requests==2.31.0', 'pytest==7.3.1', 'flake8==7.0.0', 'coverage'],
    },
)
