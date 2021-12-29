from sys import version
import versioneer

from setuptools import setup, find_packages

setup(name='MusicGraph', author='Jonathan Elsner',
      description='A graph to find music similar to that which you already listen.',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      packages=find_packages(where='music_graph'))
