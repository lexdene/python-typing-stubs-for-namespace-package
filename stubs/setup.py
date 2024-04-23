from setuptools import setup, find_namespace_packages

ns_name = 'somenamespace'

setup(
    name=f'{ns_name}-stubs',
    version='0.0.1',

    package_data={
        f'{ns_name}-stubs': [
            'bar/say.pyi',
        ]
    },
)
