import re
import nltk
from typing import Dict, List, Any
from lark import ParseError
from .grammar import Grammar

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

class BaseProcessor:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
    
    def _nltk_tokenize_elements(self, text: str) -> List[str]:
        try:
            return nltk.word_tokenize(text)
        except Exception as e:
            raise ValueError(f"Error in NLTK tokenization: {str(e)}")
    
    def _match_grammar(self, text: str) -> List[Dict[str, Any]]:
        matches = []
        
        if self.grammar.type == 'regex':
            for key, pattern in self.grammar.rules.items():
                found = re.findall(pattern, text, re.IGNORECASE)
                if found:
                    matches.append({'type': key, 'matches': found})
        
        elif self.grammar.type == 'cfg':
            try:
                tree = self.grammar.parser.parse(text)
                matches.append({
                    'type': 'cfg_parse',
                    'tree': str(tree),
                    'matches': [text]
                })
            except ParseError:
                pass
        
        return matches
    
    def _build_result(self, processed_text: str, elements: List[str], 
                    matches: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            'text': processed_text,
            'tokens': elements,
            'matches': matches,
            'stats': {
                'token_count': len(elements),
                'match_count': sum(len(m['matches']) for m in matches),
                'unique_tokens': len(set(e.lower() for e in elements))
            }
        }
    