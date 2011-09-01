from setuptools import find_packages, setup

from mattspackage import VERSION

setup(
    version=VERSION,
    name="mattspackage",
    author="Matthew J. Morrison",
    author_email="mattjmorrison@mattjmorrison.com",
    description="Matt's Package will notify werewolf hunters when the next full moon will be.",
    long_description=open('README', 'r').read(),
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Environment :: Console',
    ],
    license='License :: OSI Approved :: MIT License',
    install_requires=('pyephem',),
    tests_require=('lettuce',),
    test_suite='mattspackage.tests'
)
