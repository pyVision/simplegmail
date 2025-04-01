import setuptools

setuptools.setup(
    name="simplegmail",
    version="4.1.1",
    url="https://github.com/jeremyephron/simplegmail",
    author="Jeremy Ephron",
    author_email="jeremye@cs.stanford.edu",
    description="A simple Python API client for Gmail.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=[
        'beautifulsoup4>=4.0.0',
        'python-dateutil>=2.8.1',
        'lxml>=4.4.2',
        'google-auth>=2.16.0',
        'google-auth-oauthlib>=1.0.0',
        'google-auth-httplib2>=0.1.0',
        'google-api-python-client>=2.80.0',
    ],
    python_requires='>=3.6',
    # Removing setup_requires and tests_require in favor of modern practices
    # Tests should be configured in pyproject.toml or setup.cfg
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
