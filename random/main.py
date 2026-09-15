def reverse_list(items):
    if len(items) == 0:
        return []
    
    reversed_items = []

    for i in range(len(items) - 1, -1, -1):
        print(f"{i}", items[i])
        

    return reversed_items
        
# items = [1, 2 , 3, 4]        
# reverse_list(items)

# profanity function

messages1 = ["darn it", "this dang thing won't work", "lets fight one on one"]
messages2 = ["darn it", "this thing won't work", "lets fight one on one"]

def filter_bad_word(words_string, bad_word):
    words = words_string.split(' ')
    result = []
    bad_words_count = 0
    for word_item in words:
        if word_item != bad_word:
            result.append(word_item)
        else:
            bad_words_count += 1
            
    return " ".join(result), bad_words_count

def filter_messages(messages):
    bad_word = 'dang'
    messages_len = len(messages)
    
    filtered_messages = []
    count_in_messages = []

    for i in range(0, messages_len):
        message = messages[i]
        new_message, bad_words_count = filter_bad_word(message, bad_word)
        filtered_messages.append(new_message)
        count_in_messages.append(bad_words_count)
        
    return filtered_messages, count_in_messages

print(filter_messages(messages1))


    

