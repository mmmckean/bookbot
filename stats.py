def wordcount(file_contents):
    words = file_contents.split()
    return len(words)

def charcount(file_contents):
    freq = {}
    for char in file_contents.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return(freq)

def sort_on(freq):
    return freq["num"]

def sort_chars(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
