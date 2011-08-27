from setuptools import find_packages, setup

setup(
    version="0.1.5",
    name="mattspackage",
    author="Matthew J. Morrison",
    author_email="mattjmorrison@mattjmorrison.com",
    description="Matt's Package will notify werewolf hunters when the next full moon will be.",
    long_description=open('README', 'r').read(),
    packages=find_packages(),
    include_package_data=True,
    classifiers = [
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Environment :: Console',
    ],
    install_requires=(
        'pyephem',
    ),
    tests_require=(
        'lettuce',
    ),
    test_suite='mattspackage.tests'
)
