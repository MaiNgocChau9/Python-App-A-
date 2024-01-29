from pyvi import ViTokenizer

def spell_check(word):
    # Sử dụng thư viện pyvi để kiểm tra chính tả Tiếng Việt
    tokens = ViTokenizer.tokenize(word)
    
    if tokens == word:
        return f" là từ đúng chính tả! 🎉"
    else:
        return f"có thể là từ sai chính tả."

# Ví dụ sử dụng
word_to_check = input("Nhập văn bản muốn kiểm tra: ")
result = spell_check(word_to_check)
print(f"\"{word_to_check}\"{result}")