# Pavel Tinyakov

with open('task_4_out.txt.', encoding='utf-8') as data_r:
    lines = data_r.readlines()

dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('task_4_in.txt.', 'w', encoding='utf-8') as data_w:
    for i in lines:
        line = i.split()
        line[0] = dictionary[line[0]]
        data_w.write(' '.join(line) + '\n')
