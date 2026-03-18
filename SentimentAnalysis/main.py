from model import train_model

# train model
model, cv = train_model()

print("Sentiment Analysis Console App")
print("Type 'exit' to stop")

while True:

    text = input("Enter text: ")

    if text.lower() == "exit":
        break

    text_vector = cv.transform([text])

    result = model.predict(text_vector)

    print("Sentiment:", result[0])