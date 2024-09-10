# setup.py

from setuptools import setup, find_packages

setup(
    name='my_git_sample_lib',  # パッケージ名
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # 依存関係があればここに記述
    description='A sample Python library',
)
