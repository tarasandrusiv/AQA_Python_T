"""
Homework #4.

In this task need to count each vowel occurrence in text below '
(total sum of lower and capital cases).'
Then need to modify poem text by replacing letters in it.

Flow:
 - counting each vowel occurrence in text
 - write output as table
 - modify text where each vowel replaced with
# A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
"""

poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze. 

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

number_a = poem_text.count('a') + poem_text.count('A')
number_e = poem_text.count('e') + poem_text.count('E')
number_i = poem_text.count('i') + poem_text.count('I')
number_o = poem_text.count('o') + poem_text.count('O')
number_u = poem_text.count('u') + poem_text.count('U')

sep_num = 21
print("See poem text below")
print("-" * sep_num)
print(poem_text)
print("-" * sep_num)
print("See table with vowel letters count below")
print("-" * sep_num)
print(f"| {'vowel':^7} | {'count':^7} |")
print("-" * sep_num)
vowel_count = {
    "a": number_a,
    "e": number_e,
    "i": number_i,
    "o": number_o,
    "u": number_u,
}

for letter, number in vowel_count.items():
    print(f"| {letter:^8}| {number:^7} |")

print("-" * sep_num)
print("See modified poem text below")
print("-" * sep_num)

rep_table = str.maketrans('aAeEiIoOuU', 'àÀéÉíÍóÓúÚ')
modified_poem = poem_text.translate(rep_table)
print(modified_poem)

# 2nd method
# rep_table = poem_text.replace(f'a', 'à').replace('A', 'À').replace('e', 'é').replace('E', 'É').replace('E', 'É')....
