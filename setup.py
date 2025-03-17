
from setuptools import setup
from quikprint import __version__


setup(
      name='quikprint',
      version=__version__,
      description='Simple Qt frontend of Printing command lp',
      long_description='Simple Qt frontend of Printing command lp',
      keywords='printing pyqt pyqt5 qt5',
      url='http://github.com/ksharindam/quikprint',
      author='Arindam Chaudhuri',
      author_email='ksharindam@gmail.com',
      license='GNU GPLv3',
      packages=['quikprint'],
      classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Environment :: X11 Applications :: Qt',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Operating System :: POSIX :: Linux',
      'Programming Language :: Python :: 3',
      ],
      entry_points={
          'gui_scripts': ['quikprint=quikprint.main:main'],
      },
      data_files=[
                 ('share/applications', ['data/quikprint.desktop']),
      ],
      include_package_data=True,
      zip_safe=False)
