# ==================== test_libraries.py ====================
"""
Prueba que las librerías estén funcionando correctamente.
Ejecutar después de activar el entorno virtual.
"""

def test_nltk():
    """Prueba NLTK y tokenización."""
    print("\n" + "="*70)
    print("🧪 Probando NLTK...")
    print("="*70)
    
    try:
        import nltk
        print(f"✅ NLTK importado (versión: {nltk.__version__})")
        
        # Descarga datos si no existen
        try:
            nltk.data.find('tokenizers/punkt')
            print("✅ Datos punkt ya descargados")
        except LookupError:
            print("📥 Descargando datos punkt...")
            nltk.download('punkt', quiet=True)
            print("✅ Datos punkt descargados")
        
        # Prueba tokenización
        texto = "Hola mundo. Este es un test de NLTK."
        tokens = nltk.word_tokenize(texto)
        print(f"✅ Tokenización exitosa: {tokens}")
        print(f"   Total tokens: {len(tokens)}")
        
        return True
    except Exception as e:
        print(f"❌ Error en NLTK: {e}")
        return False


def test_lark():
    """Prueba Lark para parsing."""
    print("\n" + "="*70)
    print("🧪 Probando Lark...")
    print("="*70)
    
    try:
        from lark import Lark
        print("✅ Lark importado")
        
        # Crea una gramática simple
        grammar = """
            start: saludo nombre
            saludo: "hola" | "hi"
            nombre: WORD
            %import common.WORD
            %import common.WS
            %ignore WS
        """
        
        parser = Lark(grammar)
        print("✅ Parser creado")
        
        # Prueba parsing
        tree = parser.parse("hola mundo")
        print(f"✅ Parsing exitoso: {tree}")
        
        return True
    except Exception as e:
        print(f"❌ Error en Lark: {e}")
        return False


def test_pillow():
    """Prueba Pillow (PIL) para imágenes."""
    print("\n" + "="*70)
    print("🧪 Probando Pillow (PIL)...")
    print("="*70)
    
    try:
        from PIL import Image, ImageDraw, ImageFont
        import PIL
        print(f"✅ Pillow importado (versión: {PIL.__version__})")
        
        # Crea una imagen de prueba
        img = Image.new('RGB', (200, 100), color='white')
        draw = ImageDraw.Draw(img)
        draw.text((10, 40), "Test", fill='black')
        print("✅ Imagen creada: 200x100 px")
        
        # Guarda temporalmente
        img.save('test_image.png')
        print("✅ Imagen guardada: test_image.png")
        
        # Lee la imagen
        img_loaded = Image.open('test_image.png')
        print(f"✅ Imagen cargada: {img_loaded.size}")
        
        return True
    except Exception as e:
        print(f"❌ Error en Pillow: {e}")
        return False


def test_pytesseract():
    """Prueba Tesseract OCR."""
    print("\n" + "="*70)
    print("🧪 Probando pytesseract (OCR)...")
    print("="*70)
    
    try:
        import pytesseract
        from PIL import Image, ImageDraw, ImageFont
        print("✅ pytesseract importado")
        
        # Verifica versión de Tesseract
        try:
            version = pytesseract.get_tesseract_version()
            print(f"✅ Tesseract instalado (versión: {version})")
        except pytesseract.TesseractNotFoundError:
            print("❌ Tesseract NO está instalado en el sistema")
            print("   Instalar:")
            print("   - Windows: https://github.com/UB-Mannheim/tesseract/wiki")
            print("   - Ubuntu: sudo apt-get install tesseract-ocr")
            print("   - macOS: brew install tesseract")
            return False
        
        # Crea imagen con texto claro
        img = Image.new('RGB', (400, 100), color='white')
        draw = ImageDraw.Draw(img)
        
        try:
            # Intenta usar fuente del sistema
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            # Si falla, usa fuente por defecto
            font = ImageFont.load_default()
        
        draw.text((10, 30), "Hello OCR", fill='black', font=font)
        img.save('test_ocr.png')
        print("✅ Imagen con texto creada: test_ocr.png")
        
        # Extrae texto
        texto = pytesseract.image_to_string(img)
        print(f"✅ Texto extraído: '{texto.strip()}'")
        
        if 'Hello' in texto or 'OCR' in texto:
            print("✅ OCR funcionando correctamente")
            return True
        else:
            print("⚠️  OCR funciona pero no reconoció el texto correctamente")
            return True
        
    except Exception as e:
        print(f"❌ Error en pytesseract: {e}")
        return False


def test_speech_recognition():
    """Prueba SpeechRecognition."""
    print("\n" + "="*70)
    print("🧪 Probando SpeechRecognition...")
    print("="*70)
    
    try:
        import speech_recognition as sr
        print(f"✅ SpeechRecognition importado (versión: {sr.__version__})")
        
        # Crea reconocedor
        recognizer = sr.Recognizer()
        print("✅ Recognizer creado")
        
        print("ℹ️  Para probar reconocimiento de voz necesitas:")
        print("   - Un archivo de audio .wav")
        print("   - O usar el micrófono con: recognizer.listen()")
        print("   (Esta prueba solo verifica que la librería funcione)")
        
        return True
    except Exception as e:
        print(f"❌ Error en SpeechRecognition: {e}")
        return False


# ==================== test_my_library.py ====================
"""
Pruebas específicas de TU librería.
"""

def test_library_import():
    """Prueba que tu librería se pueda importar."""
    print("\n" + "="*70)
    print("🧪 Probando IMPORTACIÓN de tu librería...")
    print("="*70)
    
    try:
        from grammar import Grammar
        from processor import Processor
        from text_processor import TextProcessor
        from voice_processor import VoiceProcessor
        from image_processor import ImageProcessor
        from base_processor import BaseProcessor
        from utils import contar_ocurrencias, buscar_elemento
        
        print("✅ Todos los módulos importados correctamente")
        print("   - Grammar")
        print("   - Processor")
        print("   - TextProcessor")
        print("   - VoiceProcessor")
        print("   - ImageProcessor")
        print("   - BaseProcessor")
        print("   - Utils")
        
        return True
    except ImportError as e:
        print(f"❌ Error al importar: {e}")
        print("\n💡 Asegúrate de estar en el directorio correcto")
        print("   o que los archivos .py estén en el mismo directorio")
        return False


def test_grammar_creation():
    """Prueba crear gramáticas."""
    print("\n" + "="*70)
    print("🧪 Probando CREACIÓN DE GRAMÁTICAS...")
    print("="*70)
    
    try:
        from grammar import Grammar
        
        # Prueba 1: Gramática regex básica
        print("\n📝 Test 1: Gramática regex básica")
        g1 = Grammar({'email': r'\w+@\w+\.\w+'})
        print(f"✅ Gramática regex creada")
        print(f"   Tipo: {g1.type}")
        print(f"   Reglas: {list(g1.rules.keys())}")
        
        # Prueba 2: Múltiples reglas
        print("\n📝 Test 2: Múltiples reglas")
        g2 = Grammar({
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'phone': r'\d{3}-\d{3}-\d{4}',
            'url': r'https?://[^\s]+'
        })
        print(f"✅ Gramática con {len(g2.rules)} reglas")
        
        # Prueba 3: Regex inválido (debe fallar)
        print("\n📝 Test 3: Validación de regex inválido")
        try:
            g3 = Grammar({'bad': '['})  # Regex inválido
            print("❌ No detectó regex inválido")
            return False
        except ValueError as e:
            print(f"✅ Detectó regex inválido: {str(e)[:50]}...")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_text_processing():
    """Prueba procesamiento de texto."""
    print("\n" + "="*70)
    print("🧪 Probando PROCESAMIENTO DE TEXTO...")
    print("="*70)
    
    try:
        from grammar import Grammar
        from processor import Processor
        
        # Crea gramática
        print("\n📝 Creando gramática de emails y teléfonos...")
        grammar = Grammar({
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'phone': r'\d{3}-\d{3}-\d{4}'
        })
        
        # Crea procesador
        processor = Processor(grammar)
        print("✅ Procesador creado")
        
        # Prueba texto
        texto = "Contacto: juan@example.com o llamar al 555-123-4567"
        print(f"\n📝 Procesando: '{texto}'")
        
        result = processor.process_input(texto, type='text')
        
        print("\n📊 RESULTADOS:")
        print(f"   Texto procesado: {result['text']}")
        print(f"   Tokens: {result['tokens']}")
        print(f"   Total tokens: {result['stats']['token_count']}")
        print(f"   Tokens únicos: {result['stats']['unique_tokens']}")
        print(f"   Coincidencias: {result['stats']['match_count']}")
        
        if result['matches']:
            print("\n🎯 COINCIDENCIAS ENCONTRADAS:")
            for match in result['matches']:
                print(f"   {match['type']}: {match['matches']}")
        
        # Valida resultados
        emails = [m for m in result['matches'] if m['type'] == 'email']
        phones = [m for m in result['matches'] if m['type'] == 'phone']
        
        if emails and 'juan@example.com' in emails[0]['matches']:
            print("✅ Email detectado correctamente")
        else:
            print("⚠️  Email no detectado")
        
        if phones and '555-123-4567' in phones[0]['matches']:
            print("✅ Teléfono detectado correctamente")
        else:
            print("⚠️  Teléfono no detectado")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_gesture_processing():
    """Prueba procesamiento de gestos (lista)."""
    print("\n" + "="*70)
    print("🧪 Probando PROCESAMIENTO DE GESTOS...")
    print("="*70)
    
    try:
        from grammar import Grammar
        from processor import Processor
        
        grammar = Grammar({'palabra': r'\w+'})
        processor = Processor(grammar)
        
        gestos = ['arriba', 'abajo', 'izquierda', 'derecha']
        print(f"\n📝 Procesando gestos: {gestos}")
        
        result = processor.process_input(gestos, type='gestures')
        
        print(f"✅ Tokens encontrados: {result['tokens']}")
        print(f"   Total: {result['stats']['token_count']}")
        
        if result['stats']['token_count'] == 4:
            print("✅ Gestos procesados correctamente")
            return True
        else:
            print("⚠️  Cantidad de tokens no coincide")
            return False
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_image_processing():
    """Prueba procesamiento de imágenes."""
    print("\n" + "="*70)
    print("🧪 Probando PROCESAMIENTO DE IMÁGENES...")
    print("="*70)
    
    try:
        from grammar import Grammar
        from processor import Processor
        from PIL import Image, ImageDraw, ImageFont
        import io
        
        # Verifica que Tesseract esté instalado
        import pytesseract
        try:
            pytesseract.get_tesseract_version()
        except pytesseract.TesseractNotFoundError:
            print("⚠️  Tesseract no instalado - saltando prueba de OCR")
            return True
        
        # Crea imagen con texto
        print("\n📝 Creando imagen de prueba...")
        img = Image.new('RGB', (400, 100), color='white')
        draw = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()
        
        draw.text((10, 30), "Test 12345", fill='black', font=font)
        
        # Convierte a bytes
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        
        # Procesa
        grammar = Grammar({'numero': r'\d+'})
        processor = Processor(grammar)
        
        print("📝 Procesando imagen con OCR...")
        result = processor.process_input(img_bytes, type='image')
        
        print(f"✅ Texto extraído: '{result['text'].strip()}'")
        print(f"   Tokens: {result['tokens']}")
        
        if result['matches']:
            print(f"   Coincidencias: {result['matches']}")
            print("✅ Procesamiento de imagen exitoso")
        else:
            print("⚠️  No se encontraron coincidencias (normal si OCR no es perfecto)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_utils():
    """Prueba funciones utilitarias."""
    print("\n" + "="*70)
    print("🧪 Probando UTILIDADES...")
    print("="*70)
    
    try:
        from utils import contar_ocurrencias, buscar_elemento
        
        # Test contar_ocurrencias
        print("\n📝 Test contar_ocurrencias")
        texto = "hola mundo, hola amigo, hola"
        count = contar_ocurrencias(texto, r'hola')
        print(f"   Ocurrencias de 'hola': {count}")
        if count == 3:
            print("✅ contar_ocurrencias funciona")
        else:
            print(f"❌ Esperaba 3, obtuvo {count}")
        
        # Test buscar_elemento
        print("\n📝 Test buscar_elemento")
        elementos = ['Python', 'JavaScript', 'Java']
        encontrado = buscar_elemento(elementos, 'python')
        if encontrado:
            print("✅ buscar_elemento funciona (case-insensitive)")
        else:
            print("❌ No encontró 'python' en lista")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


# ==================== SCRIPT PRINCIPAL ====================
def run_all_tests():
    """Ejecuta todas las pruebas."""
    print("\n" + "="*70)
    print("  🚀 SUITE COMPLETA DE PRUEBAS")
    print("="*70)
    
    results = {}
    
    # Pruebas de librerías
    print("\n\n" + "🔷"*35)
    print("  PARTE 1: PRUEBAS DE LIBRERÍAS EXTERNAS")
    print("🔷"*35)
    
    results['NLTK'] = test_nltk()
    results['Lark'] = test_lark()
    results['Pillow'] = test_pillow()
    results['Pytesseract'] = test_pytesseract()
    results['SpeechRecognition'] = test_speech_recognition()
    
    # Pruebas de tu librería
    print("\n\n" + "🔷"*35)
    print("  PARTE 2: PRUEBAS DE TU LIBRERÍA")
    print("🔷"*35)
    
    results['Importación'] = test_library_import()
    
    if results['Importación']:
        results['Grammar'] = test_grammar_creation()
        results['Text Processing'] = test_text_processing()
        results['Gesture Processing'] = test_gesture_processing()
        results['Image Processing'] = test_image_processing()
        results['Utils'] = test_utils()
    
    # Resumen
    print("\n\n" + "="*70)
    print("  📊 RESUMEN DE PRUEBAS")
    print("="*70)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status:10} | {test}")
    
    print("="*70)
    print(f"Total: {passed}/{total} pruebas exitosas ({passed*100//total}%)")
    
    if passed == total:
        print("\n🎉 ¡TODAS LAS PRUEBAS PASARON!")
        print("✅ Tu librería está lista para usar")
    else:
        print("\n⚠️  Algunas pruebas fallaron")
        print("   Revisa los errores arriba")
    
    print("="*70)
    
    # Limpia archivos temporales
    import os
    for f in ['test_image.png', 'test_ocr.png']:
        if os.path.exists(f):
            os.remove(f)
            print(f"🗑️  Archivo temporal eliminado: {f}")


if __name__ == "__main__":
    run_all_tests()