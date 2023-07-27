import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup_args = dict(
    name="skywatchpy",
    version="0.1.1",
    description="",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Abdurakhmon Asatullayev",
    author_email="abduraxmonasatullayev35@gmail.com",
    url='https://github.com/Abduraxmonnn/SkyWatchPy.git',
    license="MIT",
    packages=["skywatchpy"],
    zip_safe=False
)

install_requires = [
    'requests',
    'python-dotenv',
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
