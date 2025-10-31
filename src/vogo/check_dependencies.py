# ==================== check_dependencies.py ====================
"""
Script para verificar que todas las dependencias estén instaladas.
Ejecuta este archivo antes de usar la librería.
"""

import sys
from typing import Dict, List, Tuple

def check_dependencies() -> Tuple[bool, List[str]]:
    """
    Verifica todas las dependencias necesarias.
    
    Returns:
        (todas_instaladas, lista_de_faltantes)
    """
    dependencies = {
        'nltk': 'Natural Language Toolkit para tokenización',
        'lark': 'Parser para gramáticas CFG',
        'pytesseract': 'OCR para extracción de texto de imágenes',
        'PIL': 'Python Imaging Library (Pillow)',
        'speech_recognition': 'Reconocimiento de voz'
    }
    
    missing = []
    installed = []
    
    print("🔍 Verificando dependencias...\n")
    
    for package, description in dependencies.items():
        try:
            # Intenta importar el paquete
            if package == 'PIL':
                __import__('PIL')
            else:
                __import__(package)
            
            # Obtiene la versión si es posible
            try:
                if package == 'PIL':
                    import PIL
                    version = PIL.__version__
                else:
                    module = __import__(package)
                    version = getattr(module, '__version__', 'unknown')
            except:
                version = 'unknown'
            
            print(f"✅ {package:20} v{version:10} - {description}")
            installed.append(package)
            
        except ImportError:
            print(f"❌ {package:20} {'':11} - {description} [FALTANTE]")
            missing.append(package)
    
    print(f"\n{'='*70}")
    print(f"Instaladas: {len(installed)}/{len(dependencies)}")
    
    if missing:
        print(f"\n⚠️  Faltan {len(missing)} dependencia(s):")
        for pkg in missing:
            print(f"   - {pkg}")
        return False, missing
    else:
        print("\n🎉 ¡Todas las dependencias están instaladas!")
        return True, []


def check_system_dependencies():
    """Verifica dependencias del sistema (Tesseract)."""
    print(f"\n{'='*70}")
    print("🔍 Verificando dependencias del sistema...\n")
    
    # Verifica Tesseract OCR
    try:
        import pytesseract
        version = pytesseract.get_tesseract_version()
        print(f"✅ Tesseract OCR v{version} está instalado")
        return True
    except pytesseract.TesseractNotFoundError:
        print("❌ Tesseract OCR no está instalado en el sistema")
        print("\n📝 Instalar Tesseract:")
        print("   Ubuntu/Debian: sudo apt-get install tesseract-ocr")
        print("   macOS: brew install tesseract")
        print("   Windows: Descargar de https://github.com/UB-Mannheim/tesseract/wiki")
        return False
    except ImportError:
        print("⚠️  pytesseract no está instalado, no se puede verificar Tesseract")
        return False


def check_nltk_data():
    """Verifica que los datos de NLTK estén descargados."""
    print(f"\n{'='*70}")
    print("🔍 Verificando datos de NLTK...\n")
    
    try:
        import nltk
        try:
            nltk.data.find('tokenizers/punkt')
            print("✅ NLTK punkt tokenizer está descargado")
            return True
        except LookupError:
            print("❌ NLTK punkt tokenizer no está descargado")
            print("\n📝 Descargar con: python -c \"import nltk; nltk.download('punkt')\"")
            return False
    except ImportError:
        print("⚠️  NLTK no está instalado")
        return False


def generate_requirements():
    """Genera el archivo requirements.txt."""
    requirements = """# Dependencias de la librería de procesamiento multimodal
nltk>=3.8.1
lark>=1.1.7
Pillow>=10.0.0
pytesseract>=0.3.10
SpeechRecognition>=3.10.0

# Opcional: Para mejor rendimiento
# numpy>=1.24.0
"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    
    print(f"\n{'='*70}")
    print("📄 Archivo requirements.txt generado")
    print("\n📝 Instalar todas las dependencias con:")
    print("   pip install -r requirements.txt")


def install_missing(missing: List[str]):
    """Intenta instalar dependencias faltantes."""
    if not missing:
        return
    
    print(f"\n{'='*70}")
    print("🔧 ¿Deseas instalar las dependencias faltantes? (s/n): ", end='')
    
    try:
        response = input().strip().lower()
        if response == 's':
            import subprocess
            
            # Mapeo de nombres de paquetes
            package_map = {
                'PIL': 'Pillow',
                'speech_recognition': 'SpeechRecognition'
            }
            
            for pkg in missing:
                install_name = package_map.get(pkg, pkg)
                print(f"\n📦 Instalando {install_name}...")
                
                try:
                    subprocess.check_call([
                        sys.executable, '-m', 'pip', 'install', install_name
                    ])
                    print(f"✅ {install_name} instalado correctamente")
                except subprocess.CalledProcessError:
                    print(f"❌ Error al instalar {install_name}")
    except KeyboardInterrupt:
        print("\n\n⚠️  Instalación cancelada")


# ==================== test_library.py ====================
"""
Script de pruebas básicas para verificar el funcionamiento.
"""

def test_basic_functionality():
    """Pruebas básicas de la librería."""
    print(f"\n{'='*70}")
    print("🧪 Ejecutando pruebas básicas...\n")
    
    try:
        # Intenta importar la librería
        from grammar import Grammar
        from processor import Processor
        print("✅ Importación exitosa")
        
        # Prueba 1: Crear gramática regex
        print("\n📝 Prueba 1: Gramática regex")
        grammar = Grammar({
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'number': r'\d+'
        })
        print("✅ Gramática creada")
        
        # Prueba 2: Procesar texto
        print("\n📝 Prueba 2: Procesamiento de texto")
        processor = Processor(grammar)
        result = processor.process_input(
            "Mi email es test@example.com y mi número es 12345",
            type='text'
        )
        
        print(f"   Tokens encontrados: {len(result['tokens'])}")
        print(f"   Matches encontrados: {len(result['matches'])}")
        
        if result['matches']:
            print("   Coincidencias:")
            for match in result['matches']:
                print(f"      {match['type']}: {match['matches']}")
        
        print("✅ Procesamiento exitoso")
        
        # Prueba 3: Procesar lista (gestos)
        print("\n📝 Prueba 3: Procesamiento de gestos")
        result = processor.process_input(['hola', 'mundo', '123'], type='gestures')
        print(f"   Tokens: {result['tokens']}")
        print("✅ Gestos procesados")
        
        print("\n🎉 ¡Todas las pruebas básicas pasaron!")
        return True
        
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        print("   Asegúrate de estar en el directorio correcto")
        return False
    except Exception as e:
        print(f"❌ Error en las pruebas: {e}")
        return False


def test_optional_features():
    """Prueba características opcionales (voz, imagen)."""
    print(f"\n{'='*70}")
    print("🧪 Probando características opcionales...\n")
    
    # Prueba de imagen
    print("📝 Prueba: Procesamiento de imagen")
    try:
        from processor import Processor
        from grammar import Grammar
        from PIL import Image
        import io
        
        # Crea una imagen de prueba simple
        img = Image.new('RGB', (200, 50), color='white')
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        
        grammar = Grammar({'word': r'\w+'})
        processor = Processor(grammar)
        
        # Nota: Esta prueba fallará si no hay texto en la imagen
        try:
            result = processor.process_input(img_bytes, type='image')
            print("✅ Procesador de imagen funciona")
        except ValueError as e:
            print(f"⚠️  Procesador funciona pero sin texto en imagen: {e}")
        
    except Exception as e:
        print(f"❌ Error en procesamiento de imagen: {e}")
    
    # Prueba de voz
    print("\n📝 Prueba: Procesamiento de voz")
    print("⚠️  Las pruebas de voz requieren archivos de audio reales")
    print("   Omitiendo prueba automática")


# ==================== SCRIPT PRINCIPAL ====================
if __name__ == "__main__":
    print("="*70)
    print("  VERIFICADOR DE DEPENDENCIAS - LIBRERÍA DE PROCESAMIENTO")
    print("="*70)
    
    # 1. Verifica dependencias Python
    all_ok, missing = check_dependencies()
    
    # 2. Verifica dependencias del sistema
    tesseract_ok = check_system_dependencies()
    
    # 3. Verifica datos de NLTK
    nltk_ok = check_nltk_data()
    
    # 4. Ofrece instalar faltantes
    if missing:
        install_missing(missing)
    
    # 5. Genera requirements.txt
    print(f"\n{'='*70}")
    print("📄 ¿Deseas generar/actualizar requirements.txt? (s/n): ", end='')
    try:
        if input().strip().lower() == 's':
            generate_requirements()
    except KeyboardInterrupt:
        print("\n")
    
    # 6. Ejecuta pruebas si todo está instalado
    if all_ok and tesseract_ok and nltk_ok:
        try:
            print(f"\n{'='*70}")
            print("🧪 ¿Deseas ejecutar pruebas básicas? (s/n): ", end='')
            if input().strip().lower() == 's':
                test_basic_functionality()
                test_optional_features()
        except KeyboardInterrupt:
            print("\n")
    
    # Resumen final
    print(f"\n{'='*70}")
    print("📋 RESUMEN")
    print("="*70)
    print(f"Dependencias Python: {'✅ OK' if all_ok else '❌ FALTAN'}")
    print(f"Tesseract OCR:       {'✅ OK' if tesseract_ok else '❌ FALTA'}")
    print(f"Datos NLTK:          {'✅ OK' if nltk_ok else '❌ FALTAN'}")
    
    if all_ok and tesseract_ok and nltk_ok:
        print("\n🎉 ¡Tu librería está lista para usarse!")
    else:
        print("\n⚠️  Completa la instalación de dependencias antes de usar la librería")
    
    print("="*70)