from setuptools import setup, find_packages

setup(
    name='motivational_quotes',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=3.2,<4.0',
        'requests>=2.25.1'
    ],
    entry_points={
        'console_scripts': [
            'manage=manage:main',
        ],
    },
)
