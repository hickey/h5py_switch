from setuptools import setup, find_packages
from pathlib import Path


setup(
    name='h5py_switch',
    version='0.0.2',
    description='Either h5py or h5pyd. Seamlessly.',
    long_description=Path('./README.md').open('rt', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ajelenak/h5py_switch',
    author='Aleksandar Jelenak',
    author_email='aleksandar.jelenak@mailg.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    # keywords='sample setuptools development',
    # py_modules=["my_module"],
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    install_requires=[
        'h5py>=2.9.0',
        'h5pyd @ git+https://github.com/HDFGroup/h5pyd.git#egg=h5pyd-0.4.0'],
    # extras_require={},
    # package_data={},
    # data_files=[],
    # entry_points={},
    # project_urls={},
)
