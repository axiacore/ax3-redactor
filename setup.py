import setuptools

__VERSION__ = '1.0.14'

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ax3-redactor',
    version=__VERSION__,
    author='Axiacore',
    author_email='info@axiacore.com',
    description='A Django app to add support for redactor',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Axiacore/ax3-redactor',
    packages=setuptools.find_packages(),
    install_requires=['ax3-model-extras>=1.2.4'],
    include_package_data=True,
    zip_safe=False,  # because we're including static files
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
