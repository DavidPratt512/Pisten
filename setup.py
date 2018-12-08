import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
        name='pisten',
        version='0.1',
        author='David Pratt',
        author_email='davidpratt512@gmail.com',
        description='A simple magic packet forwarder',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://githup.com/davidpratt512/pisten',
        packages=setuptools.find_packages(),
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: System Administrators',
            'Topic :: Internet',
            'Programming Language :: Python :: 3 :: Only',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent'
            ]
)

