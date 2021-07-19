def rename(s):
    s = s.split()
    emj = []
    for i in s:
        if i[0] == emj[0]:
            i = i.replace(emj[0]*len(i), '=' + ')'*len(i))
        if i[0] == emj[1]:
            i = i.replace(emj[1]*len(i), '=' + '('*len(i))
        if i[0] == emj[2]:
            i = i.replace(emj[2]*len(i), '=' + '/'*len(i))
        if i[0] == emj[3]:
            i = i.replace(emj[3]*len(i), ';' + ')'*len(i))
        if i[0] == emj[4]:
            i = i.replace(emj[4]*len(i), 'X' + 'D'*len(i))
        if i[0] == emj[5]:
            i = i.replace(emj[5]*len(i), '-'*len(i) + '_' + '-'*len(i))
        if i[0] == emj[6]:
            i = i.replace(emj[6]*len(i), 'o'*len(i) + '_' + 'O'*len(i))
        if i[0] == emj[7]:
            i = i.replace(emj[7]*len(i), '$'*len(i) + '_' + '$'*len(i))
        if i[0] == emj[8]:
            i = i.replace(emj[8]*len(i), 'rofl')
    return s

