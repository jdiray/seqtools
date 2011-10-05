import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup
from setuptools import find_packages

if __name__ == '__main__':
    setup(
        name='seqtools',
        version="0.5",
        description="Tools for sequence and alignment manipulation",
        author="Brant Faircloth",
        author_email="brant.faircloth+seqtools@gmail.com ",
        url="http://github.com/faircloth-lab/seqtools/",
        license="",
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Operating System :: OS Independent',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
             ],
        requires=['numpy(>=1.3)'],
        long_description=open('README.rst').read(),
        packages = find_packages('seqtools'),
        package_dir = {'':'seqtools'},
        include_package_data = True,
        test_suite = "sequence",
        )
