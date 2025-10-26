import re
import nltk
from typing import Dict, List, Any
from lark import ParseError
from .grammar import Grammar
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
            for key in self.grammar.rules:
                try:
                    tree = self.grammar.parser.parse(text)
                    matches.append({'type': key, 'matches': [str(tree)]})
                except ParseError:
                    pass
        return matches
    def _build_result(self, processed_text: str, elements: List[str], matches: List[Dict[str, Any]]) -> Dict[str, Any]:
        features = {
            'element_count': len(elements),
            'match_count': sum(len(m['matches']) for m in matches),
            'word_search': lambda word: word.lower() in [e.lower() for e in elements],
            'exact_match': lambda pattern: bool(re.search(pattern, processed_text))
        }
        return {
            'matches': matches,
            'elements': elements,
            'features': features
        }
