import setuptools


#with open("README.md", "r") as fh:
#    long_description = fh.read()


install_requires = open('requirements.txt','r').readlines()
install_requires = [e.split('==')[0] for e in install_requires]


setuptools.setup(
    name="sublminer",
    version="0.0.1",
    author="Natan 'Albrigs' Fernandes dos Santos",
    author_email="natanfernandessantos@protonmail.com",
    description="",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://github.com/Albrigs/Subl_Miner",
    packages=['sublminer'],
    classifiers=[

    ],
    install_requires=install_requires,
    python_requires='>=3.6',
    entry_points = {
        'console_scripts': [
            'sublminer = sublminer.__main__:main'
        ]
    }
)