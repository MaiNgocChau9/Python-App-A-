from textblob import TextBlob

text = "Xin chào, tôi thích chạy đua"
blob = TextBlob(text)

for word, tag in blob.tags:
    print(f"{word} is a {tag}.")