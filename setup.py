from setuptools import setup, find_packages
import io


setup(
    name='mmdesigner',
    description='Indoor model airplane design using OpenSCAD',
    long_description=re.compile(
        '^.. start-badges.*^.. end-badges',
        re.M | re.S
    ).sub(
        '',
        read('README.rst')
    ),
    long_description_content_type='text/x-rst',
    author='Roie R. Black',
    author_email='roie.black@gmail.com',
    url='https://github.com/rblack42/math-magik',
    license='BSD',
    version='0.1.4',
    package_dir={'': 'mmdesigner'},
    packages=find_packages('mmdesigner'),
    entry_points={
        'mmdesigner2': ['mmdesigner = mmdesigner.main'],
    },
    install_requires=['tox>=2.0'],
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: tox',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Testing',
    ],
)
