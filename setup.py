from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(name='infinity',
      version='0.1',
      description='Infinity for use when comparing ints and floats',
      url='http://github.com/Djsurry/infinity',
      author='David Surry',
      author_email='djsurry@gmail.com',
      license='MIT',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['infinity'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
	]
)

