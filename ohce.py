from datetime import datetime

class RealClock:
    def get_current_hour(self):
        return datetime.now().hour

class Ohce:
    def __init__(self, name, clock=None):
        self.name = name
        self.clock = clock or RealClock()
        
    def reverse_echo(self, text):
        reversed_text = text[::-1]
        
        if self._is_palindrome(text):
            return f"{reversed_text}\n¡Bonita palabra!"
        
        return reversed_text
    
    def _is_palindrome(self, text):
        """Check if a text is a palindrome."""
        return text == text[::-1]
    
    def greet(self):
        hour = self.clock.get_current_hour()
        
        if 6 <= hour < 12:
            return f"¡Buenos días {self.name}!"
        elif 12 <= hour < 20:
            return f"¡Buenas tardes {self.name}!"
        else:  # 20-23 and 0-5
            return f"¡Buenas noches {self.name}!"