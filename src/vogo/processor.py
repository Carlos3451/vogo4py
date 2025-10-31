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
            'gestures': TextProcessor(grammar),
            'image': ImageProcessor(grammar),
            'video': ImageProcessor(grammar)
        }
    
    def process_input(self, input: Union[str, List[str], bytes], 
                    type: str = 'text') -> Dict[str, Any]:

        if type not in self.processors:
            raise ValueError(
                f"Invalid input type: '{type}'. "
                f"Valid types: {list(self.processors.keys())}"
            )
        
        return self.processors[type].process(input)
