import re
from typing import Dict
from lark import Lark

class Grammar:
    def __init__(self, rules: Dict[str, str], type: str = 'regex'):
        
        if not rules:
            raise ValueError("Grammar rules cannot be empty.")
        
        self.type = type
        self.rules = rules
        self.parser = None
        
        if type == 'cfg':
            grammar_str = "\n".join([f"{k}: {v}" for k, v in rules.items()])
            try:
                self.parser = Lark(grammar_str, start=list(rules.keys())[0])
            except Exception as e:
                raise ValueError(f"Error in CFG grammar: {str(e)}")
        
        elif type == 'regex':
            for key, pattern in rules.items():
                try:
                    re.compile(pattern)
                except re.error as e:
                    raise ValueError(f"Invalid regex pattern for '{key}': {str(e)}")
        else:
            raise ValueError(f"Invalid grammar type: {type}. Must be 'regex' or 'cfg'.")