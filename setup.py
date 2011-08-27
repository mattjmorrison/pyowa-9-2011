from setuptools import find_packages, setup

setup(
    version="0.0.5",
    name="mattspackage",
    author="Matthew J. Morrison",
    author_email="mattjmorrison@mattjmorrison.com",
    description="Matt's Package will notify werewolf hunters when the next full moon will be.",
    long_description=open('README', 'r').read(),
    packages=find_packages(),
    install_requires=(
        'pyephem',
    ),
    tests_require=(
        'lettuce',
    ),
    test_suite='mattspackage.tests'
)
