from typing import Union, List, Dict, Any
from .base_processor import BaseProcessor
class TextProcessor(BaseProcessor):
    def process(self, input: Union[str, List[str]]) -> Dict[str, Any]:
        if isinstance(input, list):  # Gestures
            processed_text = ' '.join(input)
        else:
            processed_text = input.strip()
        
        if not processed_text:
            raise ValueError("Input is empty.")
        
        elements = self._nltk_tokenize_elements(processed_text)
        matches = self._match_grammar(processed_text)
        return self._build_result(processed_text, elements, matches)