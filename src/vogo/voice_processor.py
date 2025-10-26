import speech_recognition as sr
from .base_processor import BaseProcessor
class VoiceProcessor(BaseProcessor):
    def process(self, input: bytes) -> Dict[str, Any]:
        processed_text = self._transcribe_voice(input)
        elements = self._nltk_tokenize_elements(processed_text)
        matches = self._match_grammar(processed_text)
        return self._build_result(processed_text, elements, matches)
    def _transcribe_voice(self, audio_bytes: bytes) -> str:
        recognizer = sr.Recognizer()
        audio = sr.AudioData(audio_bytes, sample_rate=16000, sample_width=2)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            raise ValueError("Could not transcribe the voice.")
        except sr.RequestError as e:
            raise ValueError(f"Error in voice service: {str(e)}")