from setuptools import setup, find_namespace_packages

ns_name = 'somenamespace'
sub_name = 'bar'

setup(
    name=f'{ns_name}-{sub_name}',
    version='0.0.1',

    packages=find_namespace_packages(include=[f'{ns_name}.*']),
    namespace_packages=[ns_name],
)
