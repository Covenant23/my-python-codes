def item_lengths(items, length):
    result = []
    for word in items:
        if len(word) == length: 
           result.append(word)
    return result
print(item_lengths(["hello", "bye", "today", "great"], 5))