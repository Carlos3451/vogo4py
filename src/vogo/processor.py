from typing import Union, List, Dict, Any
from .grammar import Grammar
from .text_processor import TextProcessor
from .voice_processor import VoiceProcessor
from .image_processor import ImageProcessor
class Processor:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.processors = {
            'text': TextProcessor(grammar),
            'voice': VoiceProcessor(grammar),
            'gestures': TextProcessor(grammar),  # Reuse for gestures
            'image': ImageProcessor(grammar),
            'video': ImageProcessor(grammar)
        }
    def process_input(self, input: Union[str, List[str], bytes], type: str = 'text') -> Dict[str, Any]:
        if type not in self.processors:
            raise ValueError("Invalid input type.")
        return self.processors[type].process(input)