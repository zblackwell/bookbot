def get_num_words (words):
    words_array = words.split()
    total_words = len(words_array)
    return total_words

def character_count (words):
    character_count = {}
    words_array = words.split()
    for word in words_array:
        for letter in word:
            if letter.lower() in character_count:
                character_count[letter.lower()] += 1
            else:
                character_count[letter.lower()] = 1
    return character_count

def sort_on(dict):
    return dict["num"]

def book_report (wordcount,char_dictionary,path):
    #report_dictionary = {char,num}
    ordered_list = []
    for character in char_dictionary:
        if character.isalpha():
            letter_dict = {}
            num_total = char_dictionary[character]
            letter_dict["char"] = character
            letter_dict["num"] = num_total
            #print(letter_dict)
            ordered_list.append(letter_dict)
    ordered_list.sort(reverse=True, key=sort_on)
    #print(ordered_list)
    #return 0
    #"""
    report = []
    report.append("============ BOOKBOT ============")
    report.append(f"Analyzing book found at {path}...")
    report.append("----------- Word Count ----------")
    report.append(f"Found {wordcount} total words")
    report.append("--------- Character Count -------")
    for item in ordered_list:
        report.append(f"{item["char"]}: {item["num"]}")
    report.append("============= END ===============")
    return report