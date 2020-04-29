from setuptools import setup, find_packages

setup(name='myAPI',
      packages=find_packages(),
      version='1.0',
      description='Employees',
      author='Anne Zhang',
      author_email='anne.zhang.work@gmail.com',
      url='https://github.ops.kobo.com/BigData/crm',
      install_requires=[
            'flask','pymysql'
      ],
      tests_require=[
          'pytest',
      ],
      test_suite='py.test myAPI',
)
