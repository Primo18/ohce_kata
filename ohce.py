class Ohce:
    def __init__(self, name):
        self.name = name
        
    def reverse_echo(self, text):
        reversed_text = text[::-1]
        
        if self._is_palindrome(text):
            return f"{reversed_text}\n¡Bonita palabra!"
        
        return reversed_text
    
    def _is_palindrome(self, text):
        """Check if a text is a palindrome."""
        return text == text[::-1]