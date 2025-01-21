
def main():
    file_contents = None
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    def count_string(string):
        list_of_all_letters = string.split()
        print(len(list_of_all_letters))      
    
    count_string(file_contents)
    
    def count_string_frequency(string):
        dict_of_str_count = {}
        for letter in string:
            if letter.isalpha():  
                letter = letter.lower()
                if letter in dict_of_str_count:
                    dict_of_str_count[letter] += 1
                else:
                    dict_of_str_count[letter] = 1
        return dict_of_str_count
    
    count_string_frequency(file_contents)
    
    
    def print_report():
        count_of_words = file_contents.split()
        count_of_letter = count_string_frequency(file_contents)
        
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{len(count_of_words)} words found in the document")
        
        sorted_items = sorted(count_of_letter.items(), key=lambda item: item[1], reverse=True)
        
        for key,value in sorted_items:
            print(f"The '{key}' character was found {value} times")
            
        print("--- End report ---")
        
    print_report()
    
main()