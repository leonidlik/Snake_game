def data_record():
    # Функция для записи ника и рекорда в общие рекорды и удаления худших результатов 
    file = open('table_of_records.txt').read().split('\n')
    tf = open('last_name_score.txt').read().split()
    if len(tf) > 2:
        name, sc = ' '.join(tf[:-1]), tf[-1]
    else:
        name, sc = tf
    score = {}
    score[sc] = [name]

    for i in file:
        if '...............' not in i:
            tf = i.split()
            if len(tf) > 2:
                name, sc = ' '.join(tf[:-1]), tf[-1]
            else:
                name, sc = tf
            if sc not in score:
                score[sc] = [name]
            else:
                score[sc].append(name)
            score[sc].sort

    key = list(score.keys())
    for i in range(len(key)):
        key[i] = int(key[i])
    key = sorted(key)[::-1]

    record = ''
    c = 0
    for i in key:
        for j in range(len(score[str(i)])):
            if c < 5:
                record += score[str(i)][j] + ' ' + str(i) + '\n'
            else:
                record += score[str(i)][j] + ' ' + str(i)
            c += 1
            if c == 5:
                break
    while c != 5:
        if c < 4:
            record += '...............' + '\n'
        else:
            record += '...............'
        c += 1

    with open('last_name_score.txt','w'): pass
    with open('table_of_records.txt','w'): pass
    file = open('table_of_records.txt', 'w')
    file.write(record)
    file.close()
    return 0

def score_record(count):
    # Функция для записи результата
    name_score = open('last_name_score.txt').read()
    if name_score == '':
        name_score = 'unknown'
    file = open('last_name_score.txt', 'w')
    name_score += ' ' + str(count)
    file.write(name_score)
    file.close()
    return 0

def name_record(text):
    # Функция для записи ника
    with open('last_name_score.txt', 'w') as f:
        f.write(text)
        f.close()
    return 0

def binding(text):
    # Функция для замены кнопок и размера экрана
    file = open('data.txt', 'w')
    file.write(text)
    file.close()
    return 0