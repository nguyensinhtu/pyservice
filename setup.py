from setuptools import setup

setup(name='pyservice',
      version='0.0.1',
      description='Python utilities to run service',
      url='https://github.com/tuns/pservice',
      author='Tuns',
      author_email='tuns@vng.com.vn',
      packages=['pyservice'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['psutil==5.7.0'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3',
          'Topic :: Applications ::micro-services'
      ])