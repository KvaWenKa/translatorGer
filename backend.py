from tkinter import messagebox

dict_special = {"eins": 1,"sechs": 6, "sieben": 7, "zenh": 10, "elf": 11, "zwolf": 12, "sechzehn": 16, "siebzehn": 17, "dreibig": 30}
dict_endings = {"zig": 10, "zehn": 10, "hundert": 100}
dict_prefixes = {"ein": 1, "zwei": 2, "zwan": 2, "drei": 3, "vier": 4, "funf": 5, "sech": 6, "sieb": 7, "acht": 8, "neun": 9}
dict_oldrus_numbers = {500: "Ф", 100: "Р", 30: "Л", 8: "И", 2: "В", 1: "А"}

def search_number(str_number):
    for spec in dict_special:
        if str_number == spec:
            return dict_special[spec]
    else:
        for prefix in dict_prefixes:
            if str_number.startswith(prefix):
                if str_number.startswith(prefix + "und"):
                    return dict_prefixes[prefix] + search_number(str_number[len(prefix + "und"):])
                for ending in dict_endings:
                    if str_number.endswith(ending):
                        if prefix + ending != str_number:
                            messagebox.showwarning("Внимание",
                                                   f"Ошибка в написании числа {prefix + ending} ({str_number}) ")
                            return 0
                        elif ending == "zehn":
                            return 10 + dict_prefixes[prefix]
                        else:
                            return dict_prefixes[prefix] * dict_endings[ending]
                else:
                    if prefix != str_number:
                        messagebox.showwarning("Внимание",
                                               f"Ошибка в написании числа {prefix} ({str_number}) ")
                    else:
                        return dict_prefixes[prefix]
        else:
            messagebox.showerror("Number not found", f"{str_number} - неизвестное число")
            return 0

def to_oldRus_numbers(numbers):
    oldRus = ""
    for old_num in dict_oldrus_numbers:
        while old_num <= numbers:
            numbers -= old_num
            oldRus += dict_oldrus_numbers[old_num]
    return oldRus