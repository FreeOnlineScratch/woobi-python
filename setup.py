from distutils.core import setup

setup(
    name='woobi-python',
    packages=['woobi', 'woobi.django'],
    version='0.0.1',
    author='Andrew Udvare',
    author_email='audvare@gmail.com',
    maintainer='Andrew Udvare',
    maintainer_email='audvare@gmail.com',
    url='https://github.com/FreeOnlineScratch/woobi-python',
    license='LICENSE.txt',
    description='Woobi API tool and Django module.',
    long_description='Woobi API tool and Django module.',
    install_requires=[
        'requests>=2.8.1',
        'six>=1.10.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Other/Nonlisted Topic',
    ],
)
