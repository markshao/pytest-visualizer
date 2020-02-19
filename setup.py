from setuptools import setup

setup(
    name="pytest-visualizer",
    use_scm_version={"write_to": "visualizer/_version.py"},
    long_description=open('README.txt').read(),
    packages=["visualizer"],
    license="MIT",
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["visualizer = visualizer.plugin"]},
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
