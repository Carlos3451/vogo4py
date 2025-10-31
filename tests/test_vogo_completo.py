

import unittest
import sys
import os
from unittest.mock import Mock, patch
import io

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import vogo
from vogo import Grammar, Processor
from vogo.text_processor import TextProcessor
from vogo.voice_processor import VoiceProcessor
from vogo.image_processor import ImageProcessor


class TestGrammar(unittest.TestCase):
    
    def test_grammar_creation_regex(self):
        """Probar creación de gramática regex"""
        rules = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'phone': r'\b\d{3}-\d{3}-\d{4}\b'
        }
        
        grammar = Grammar(rules, type='regex')
        self.assertEqual(grammar.type, 'regex')
        self.assertEqual(grammar.rules, rules)
    
    def test_grammar_creation_cfg(self):
        """Probar creación de gramática CFG"""
        rules = {
            'start': 'WORD+',
            'WORD': '/[a-zA-Z]+/'
        }
        
        grammar = Grammar(rules, type='cfg')
        self.assertEqual(grammar.type, 'cfg')
        self.assertIsNotNone(grammar.parser)
    
    def test_grammar_empty_rules(self):
        """Probar error con reglas vacías"""
        with self.assertRaises(ValueError):
            Grammar({}, type='regex')
    
    def test_grammar_invalid_regex(self):
        """Probar error con regex inválido"""
        rules = {'invalid': r'[a-z'}
        with self.assertRaises(ValueError):
            Grammar(rules, type='regex')
    
    def test_grammar_invalid_type(self):
        """Probar error con tipo inválido"""
        rules = {'test': 'pattern'}
        with self.assertRaises(ValueError):
            Grammar(rules, type='invalid_type')


class TestTextProcessor(unittest.TestCase):
    
    def setUp(self):
        rules = {
            'question': r'\?',
            'word': r'\b\w+\b'
        }
        self.grammar = Grammar(rules, type='regex')
        self.processor = TextProcessor(self.grammar)
    
    def test_process_text_string(self):
        """Probar procesamiento de texto string"""
        text = "Hello world? This is a test."
        result = self.processor.process(text)
        
        self.assertEqual(result['text'], text)
        self.assertIn('tokens', result)
        self.assertIn('matches', result)
        self.assertIn('stats', result)
        
        # Verificar que encuentra preguntas
        question_matches = [m for m in result['matches'] if m['type'] == 'question']
        self.assertTrue(len(question_matches) > 0)
    
    def test_process_text_list(self):
        """Probar procesamiento de lista de textos"""
        text_list = ["Hello", "world", "test?"]
        result = self.processor.process(text_list)
        
        self.assertEqual(result['text'], "Hello world test?")
        self.assertGreater(len(result['tokens']), 0)
    
    def test_process_empty_input(self):
        """Probar error con entrada vacía"""
        with self.assertRaises(ValueError):
            self.processor.process("")
        
        with self.assertRaises(ValueError):
            self.processor.process([])


class TestVoiceProcessor(unittest.TestCase):
    
    def setUp(self):
        rules = {
            'command': r'start|stop|pause',
            'number': r'\d+'
        }
        self.grammar = Grammar(rules, type='regex')
        self.processor = VoiceProcessor(self.grammar)
    
    def test_process_voice_text(self):
        """Probar procesamiento de texto de voz"""
        voice_text = "Start the process at 10 seconds"
        result = self.processor.process(voice_text)
        
        self.assertEqual(result['text'], voice_text)
        
        # Verificar que encuentra comandos y números
        command_matches = [m for m in result['matches'] if m['type'] == 'command']
        number_matches = [m for m in result['matches'] if m['type'] == 'number']
        
        self.assertTrue(len(command_matches) > 0)
        self.assertTrue(len(number_matches) > 0)


class TestImageProcessor(unittest.TestCase):
    
    def setUp(self):
        rules = {
            'word': r'\b\w+\b',
            'capitalized': r'\b[A-Z][a-z]+\b'
        }
        self.grammar = Grammar(rules, type='regex')
        self.processor = ImageProcessor(self.grammar)
    
    @patch('vogo.image_processor.pytesseract.image_to_string')
    @patch('vogo.image_processor.Image.open')
    def test_process_image(self, mock_image_open, mock_ocr):
        """Probar procesamiento de imagen con mock"""
        # Configurar mock
        mock_ocr.return_value = "Hello World Test Image"
        mock_image_open.return_value = Mock()
        
        # Probar con bytes de imagen simulados
        image_bytes = b"fake image bytes"
        result = self.processor.process(image_bytes)
        
        self.assertEqual(result['text'], "Hello World Test Image")
        self.assertIn('tokens', result)
        self.assertIn('matches', result)
        
        # Verificar que se llamó al OCR
        mock_ocr.assert_called_once()


class TestProcessor(unittest.TestCase):
    
    def setUp(self):
        rules = {
            'keyword': r'test|example|sample',
            'punctuation': r'[.,!?]'
        }
        self.grammar = Grammar(rules, type='regex')
        self.processor = Processor(self.grammar)
    
    def test_processor_initialization(self):
        """Probar inicialización del procesador principal"""
        self.assertEqual(self.processor.grammar, self.grammar)
        self.assertIn('text', self.processor.processors)
        self.assertIn('voice', self.processor.processors)
        self.assertIn('image', self.processor.processors)
    
    def test_process_text_input(self):
        """Probar procesamiento de texto"""
        result = self.processor.process_input("This is a test example.", "text")
        
        self.assertEqual(result['text'], "This is a test example.")
        self.assertIn('matches', result)
        
        # Verificar que encuentra keywords
        keyword_matches = [m for m in result['matches'] if m['type'] == 'keyword']
        self.assertTrue(len(keyword_matches) > 0)
    
    def test_process_voice_input(self):
        """Probar procesamiento de voz"""
        result = self.processor.process_input("Voice test example", "voice")
        self.assertEqual(result['text'], "Voice test example")
    
    def test_process_invalid_type(self):
        """Probar error con tipo inválido"""
        with self.assertRaises(ValueError):
            self.processor.process_input("test", "invalid_type")


class TestIntegration(unittest.TestCase):
    """Pruebas de integración entre componentes"""
    
    def test_full_text_processing_flow(self):
        """Probar flujo completo de procesamiento de texto"""
        # Configurar gramática compleja
        rules = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'url': r'https?://[^\s]+',
            'number': r'\b\d+\b'
        }
        grammar = Grammar(rules, type='regex')
        processor = Processor(grammar)
        
        # Texto con múltiples patrones
        text = "Contact me at test@example.com or visit https://example.com. Call 123-456-7890."
        result = processor.process_input(text, "text")
        
        # Verificar resultados
        self.assertEqual(result['text'], text)
        self.assertGreater(result['stats']['token_count'], 0)
        
        # Verificar que encontró patrones
        match_types = [m['type'] for m in result['matches']]
        self.assertIn('email', match_types)
        self.assertIn('url', match_types)


if __name__ == '__main__':
    # Ejecutar pruebas
    unittest.main(verbosity=2)