from setuptools import setup, find_packages
import io


setup(
    name='mmdesigner',
    description='Indoor model airplane design using OpenSCAD',
    long_description=io.open('README.rst', encoding='utf-8').read(),
    author='Roie R. Black',
    author_email='roie.black@gmail.com',
    url='https://github.com/rblack42/math-magik',
    license='BSD-3',
    version='0.1.3',
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
        'License :: OSI Approved :: BSD-3 License',
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
