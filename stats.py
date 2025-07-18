def count_words(book_text):
    word_count = len(book_text.split())
    return word_count

def count_chars(book_text):
    chars = book_text.lower()
    freq = {}
    for i in chars:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def sort_on(items):
    return items["num"]

def sort_chars(char_count):
    sorted_list = []
    for char, num in char_count.items():
        if char.isalpha() == True:
            sorted_list.append({"char": char,"num": num})
        else:
            pass      
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

