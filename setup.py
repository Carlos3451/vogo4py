
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='vogo',
    version='1.0.0',
    packages=find_packages(),
    description='Librería Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Juan Carlos Ticona Fiesta',
    author_email='qarlos123@outlook.com',
    url='https://github.com/Carlos3451/vogo4py',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='voice commands, gesture recognition, human-computer interaction, hands-free control',
    install_requires=[
        'numpy>=1.21.0',
        'opencv-python>=4.5.0',
        'speechrecognition>=3.8.0',
        'pyaudio>=0.2.11',
        'mediapipe>=0.8.0',
    ],
    python_requires='>=3.7',
    project_urls={
        'Documentation': 'https://github.com/Carlos3451/vogo4py/docs',
        'Source': 'https://github.com/Carlos3451/vogo4py',
    },
)