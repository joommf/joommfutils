import setuptools

with open("README.md", 'r+', encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name='joommfutil',
    version='0.8',
    description='A JOOMMF utilities package.',
    long_description=readme,
    url='https://joommf.github.io',
    author='Marijan Beg, Ryan A. Pepper, Thomas Kluyver, and Hans Fangohr',
    author_email='jupyteroommf@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=['numpy'],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: BSD License',
                 'Topic :: Scientific/Engineering :: Physics',
                 'Intended Audience :: Science/Research',
                 'Programming Language :: Python :: 3 :: Only']
)
