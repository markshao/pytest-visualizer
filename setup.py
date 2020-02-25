from setuptools import setup, find_packages

install_requires = [""]
setup(
    name="pytest-visualizer",
    use_scm_version={"write_to": "src/visual/_version.py"},
    long_description=open('README.md').read(),
    license="MIT",
    setup_requires=["setuptools_scm"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["visual = visual.plugin"]},
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest",
                 'Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: POSIX',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: MacOS :: MacOS X',
                 'Topic :: Software Development :: Testing',
                 'Topic :: Software Development :: Quality Assurance',
                 'Topic :: Utilities',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3',
                 ],
)
