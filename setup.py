from setuptools import setup, find_packages

name = 'auf.django.piwik'
version = '1.1'

setup(name=name,
      version=version,
      description="Middleware pour incorper le code de tracking de Piwik",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Django Piwik',
      author='Olivier Larchev\xc3\xaaque',
      author_email='olivier.larcheveque@auf.org',
      url='http://pypi.auf.org/%s' % name,
      license='GPL',
      namespace_packages = ['auf', 'auf.django', ],
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
