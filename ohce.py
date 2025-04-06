class Ohce:
    def __init__(self, name):
        self.name = name
        
    def reverse_echo(self, text):
        reversed_text = text[::-1]
        
        # If the original text equals the reversed text, it's a palindrome
        if text == reversed_text:
            return f"{reversed_text}\n¡Bonita palabra!"
        
        return reversed_text