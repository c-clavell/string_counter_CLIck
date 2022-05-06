from setuptools import setup, find_packages

setup(
    name='demo-str-count',
    description='demo python-click CLI tool to count input string elements',
    packages=find_packages(),
    author='Me',
    entry_points="""
    [console_scripts]
    cli_str_count=str_counter:main
    """,
    install_requires=['click'],
    version='0.0.1',
   
)
