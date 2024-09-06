def capitalize_alternative_words(input_string):
    words = input_string.split()
    capitalized_words = []
    
    for i in range(len(words)):
        if i % 2 == 0:
            capitalized_words.append(words[i].capitalize())
        else:
            capitalized_words.append(words[i])
    
    return ' '.join(capitalized_words)

input_string = "array is a linear datastructure"
output_string = capitalize_alternative_words(input_string)
print(input_string)
print(output_string)
