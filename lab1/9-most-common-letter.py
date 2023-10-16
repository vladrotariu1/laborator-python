def most_frequent_letter(text):
    freq = {}

    for char in text.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return max(freq, key=freq.get)


input_string = str(input('Enter your text: '))
most_frequent_letter = most_frequent_letter(input_string)

print(most_frequent_letter)
