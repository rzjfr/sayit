import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sayit",
    version="0.1.0",
    author="rzjfr",
    author_email="rzjfr@yahoo.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rzjfr/sayit",
    project_urls={
        "Bug Tracker": "https://github.com/rzjfr/sayit/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'fake-useragent==0.1.11',
        'requests==2.26.0',
        'playsound==1.3.0',
        'PyGObject==3.42.0',
        'bs4==0.0.1',
        'pyenchant==3.2.2',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': ['sayit=sayit:main']
    },
    setup_requires=['flake8', 'pytest-runner'],
    tests_require=['pytest'],
)
