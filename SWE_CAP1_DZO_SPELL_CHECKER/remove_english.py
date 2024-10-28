import re

def only_dzongkha_word (word):
    return re.match (r"^[\u0F00-\u0FFF]+$",word)

def filter_dzongkha_words (input_file,output_file):
    with open (input_file,"r",encoding="utf-8") as file:
        lines=file.readlines ()

        with open (output_file,"w",encoding="utf-8") as output:
            for line in lines:
                words=line.split ()

                dzongkha_words= [word for word in words if only_dzongkha_word(word)]

                if dzongkha_words:
                    output.write (" ".join(dzongkha_words)+"\n")

input_file="dzo_dict.txt"
output_file="only_dzongkha.txt"

filter_dzongkha_words (input_file, output_file)