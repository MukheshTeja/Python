import re

class MyLangTokenizer:
    def __init__(self):
        self.patterns = {
            "url": r"https?://[^\s]+",  # URL
            "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",  # Email
            "number": r"\d{1,3}(?:,\d{2,3})*(?:\.\d+)?|\d+/\d+",  # Num
            "date": r"\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}",  # Date
            "handle": r"[@#][\w]+",
            "punctuation": r"[!?.,:;\"'()\[\]{}]",
            "word": r"[\p{L}\p{M}]+",
        }

    def tokenize(self, text):
        pattern = "|".join(f"(?P<{key}>{val})" for key, val in self.patterns.items())
        tokens = []
        for match in re.finditer(pattern, text, re.UNICODE):
            for key, value in match.groupdict().items():
                if value:
                    tokens.append((key, value))
        return tokens

text = "Visit https://example.com on 12/05/2024! Email me at test@example.com or call 3,22,243. Follow @user_handle."
tokenizer = MyLangTokenizer()
tokens = tokenizer.tokenize(text)
for token in tokens: print(token)
