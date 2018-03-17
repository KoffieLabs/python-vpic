from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='python-vpic',
    version='0.1.3',
    description='Simple wrapper to the vPic API.',
    long_description=readme(),
    keywords='vPic',
    url='https://github.com/OmniRisk/python-vpic',
    author='Damian Hites',
    author_email='damian@omnirisk.co',
    license='MIT',
    packages=['vpic'],
    install_requires=[
        'requests'
    ],
    include_package_data=True,
    zip_safe=True,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
