# ==================== setup.py ====================
"""
Setup configuration for vogo library.
Multimodal accessible interfaces - Voice, Gestures, and Commands recognition.
"""
from setuptools import setup, find_packages
import os

# Lee README.md de forma segura
def read_long_description():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, encoding="utf-8") as f:
            return f.read()
    return "Librería Python para interfaces multimodales accesibles"

# Lee la versión desde __init__.py si existe
def get_version():
    init_path = os.path.join(os.path.dirname(__file__), "src", "vogo", "__init__.py")
    if os.path.exists(init_path):
        with open(init_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("__version__"):
                    return line.split("=")[1].strip().strip('"').strip("'")
    return "0.1.0"

setup(
    name="vogo",
    version=get_version(),
    author="Carlos3451",
    author_email="qarlos123@outlook.com",
    description="Librería Python para interfaces multimodales accesibles - Reconocimiento de voz, gestos y comandos",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Carlos3451/vogo",  # Actualiza con tu repo
    project_urls={
        "Source": "https://github.com/Carlos3451/vogo",
        "Documentation": "https://github.com/Carlos3451/vogo#readme",
    },
    
    # Encuentra paquetes automáticamente en src/
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    
    # Dependencias obligatorias
    install_requires=[
        "nltk>=3.8.1",
        "lark>=1.1.7",
        "Pillow>=10.0.0",
        "pytesseract>=0.3.10",
        "SpeechRecognition>=3.10.0",
    ],
    
    # Versión mínima de Python
    python_requires=">=3.8",
    
    # Clasificadores para PyPI
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Accessibility",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: Spanish",
        "Natural Language :: English",
    ],
    
    # Palabras clave para búsqueda
    keywords=[
        "accessibility",
        "voice recognition",
        "gesture recognition",
        "multimodal",
        "nlp",
        "ocr",
        "speech recognition",
        "text processing",
        "grammar parsing",
        "assistive technology",
        "accesibilidad",
        "reconocimiento de voz",
        "comandos por voz",
    ],
    
    # Incluye archivos adicionales
    include_package_data=True,
    
    # Puntos de entrada (opcional - comandos de terminal)
    entry_points={
        "console_scripts": [
            "vogo-check=vogo.cli:check_dependencies",  # Si implementas CLI
        ],
    },
    
    # Licencia
    license="MIT",
    
    # Plataformas soportadas
    platforms=["any"],
    
    # ZIP safe
    zip_safe=False,
)