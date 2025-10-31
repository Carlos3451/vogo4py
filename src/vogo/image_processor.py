from typing import Dict, Any
import io
import pytesseract
from PIL import Image
from .base_processor import BaseProcessor

class ImageProcessor(BaseProcessor):

    def process(self, input: bytes) -> Dict[str, Any]:

        processed_text = self._extract_text_from_image(input)
        elements = self._nltk_tokenize_elements(processed_text)
        matches = self._match_grammar(processed_text)
        return self._build_result(processed_text, elements, matches)
    
    def _extract_text_from_image(self, image_bytes: bytes) -> str:

        try:
            img = Image.open(io.BytesIO(image_bytes))
            return pytesseract.image_to_string(img)
        except Exception as e:
            raise ValueError(f"Error in image OCR: {str(e)}")