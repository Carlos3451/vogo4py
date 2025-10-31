from typing import Union, List, Dict, Any
import io
import speech_recognition as sr
from .base_processor import BaseProcessor

class VoiceProcessor(BaseProcessor):
    
    def process(self, input: Union[str, bytes]) -> Dict[str, Any]:
        
        # Si es texto, usarlo directamente (para pruebas)
        if isinstance(input, str):
            processed_text = input
        # Si es audio, transcribirlo
        elif isinstance(input, bytes):
            processed_text = self._transcribe_voice(input)
        else:
            raise ValueError("Input must be str (text) or bytes (audio)")
        
        if not processed_text:
            raise ValueError("No text could be processed from input")
        
        elements = self._nltk_tokenize_elements(processed_text)
        matches = self._match_grammar(processed_text)
        return self._build_result(processed_text, elements, matches)
    
    def _transcribe_voice(self, audio_bytes: bytes) -> str:
        """Transcribe audio bytes to text"""
        try:
            recognizer = sr.Recognizer()
            
            # Convert bytes to AudioFile
            with sr.AudioFile(io.BytesIO(audio_bytes)) as source:
                audio = recognizer.record(source)
            
            return recognizer.recognize_google(audio, language='es-ES')
            
        except sr.UnknownValueError:
            raise ValueError("Could not understand audio")
        except sr.RequestError as e:
            raise ValueError(f"Error with speech recognition service: {e}")
        except Exception as e:
            raise ValueError(f"Error in voice transcription: {str(e)}")