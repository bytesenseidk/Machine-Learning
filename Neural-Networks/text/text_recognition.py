import tensorflow as td
from tensorflow import keras
import numpy as np

data = keras.datasets.imdb  # Word dataset from imdb movie reviews

(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=88000)

word_index = data.get_word_index()

# Default values for frequent variables/words
word_index = {key:(value+3) for key, value in word_index.items()}
word_index["<PAD>"] = 0     # Padding
word_index["<START>"] = 1   # Starting point
word_index["<UNK>"] = 2     # Unknown characters
word_index["<UNUSED>"] = 3  # Unused

# Swap values & keys, so that the INT value points to the word
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

# Pad every line to equal length
train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding="post", maxlen=250)
test_data = keras.preprocessing.sequence.pad_sequences(test_data, value=word_index["<PAD>"], padding="post", maxlen=250)

def decode_review(text):
    return " ".join([reverse_word_index.get(i, "?") for i in text])

# Train and save a model, if no other is found 
if keras.models.load_model("model.h5") == None:
    model = keras.Sequential()
    model.add(keras.layers.Embedding(88000, 16))
    model.add(keras.layers.GlobalAveragePooling1D())
    model.add(keras.layers.Dense(16, activation="relu"))    # Amount of neurons, and 
    model.add(keras.layers.Dense(1, activation="sigmoid"))
    model.summary()
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

    x_value = train_data[:10000]
    x_train = train_data[10000:]
    y_value = train_labels[:10000]
    y_train = train_labels[10000:]

    fit_model = model.fit(x_train, y_train, epochs=40, batch_size=512, 
                          validation_data=(x_value, y_value), verbose=1)
    result = model.evaluate(test_data, test_labels)

    print(result)
    model.save("model.h5")


def review_encode(string):
    encoded = [1]
    for word in string:
        if word.lower() in word_index:
            encoded.append(word_index[word.lower()])
        else:
            encoded.append(2)
    return encoded

# Load previously saved model
model = keras.models.load_model("model.h5")

# Open and format a text
with open("analyse_me", encoding="utf-8") as f:
    for line in f.readlines():
        new_line = line.replace(",", "").replace(".", "").replace("(",
                                     "").replace(")", "").replace(":", 
                                    "").replace("\"", "").strip().split(" ")
        encode = review_encode(new_line)
        encode = keras.preprocessing.sequence.pad_sequences([encode], 
                        value=word_index["<PAD>"], padding="post", maxlen=30)
        # Analyse the text for known words
        predict = model.predict(encode)
        # print(line)
        # print(encode)
        # print(f"{predict[0]}\n")
        for i in encode:
            for x in i:
                word_id = {value:key for key, value in word_index.items()}
                print(word_id)
        