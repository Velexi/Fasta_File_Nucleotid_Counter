import threading


def decoupe(file):
    empty_string = ''
    for line in file:
        string = line.rstrip('\n')
        if not string.startswith('>'):
            empty_string = empty_string + line

    string_as_list = list(empty_string)
    return string_as_list


def calc_a(nucleotid_list):
    a_count = 0
    for char in nucleotid_list:
        if str(char) == 'A':
            a_count = a_count + 1
    print('Nombre de A dans le fichier FASTA: ' + str(a_count))


def calc_c(nucleotid_list):
    c_count = 0
    for char in nucleotid_list:
        if str(char) == 'C':
            c_count = c_count + 1
    print('Nombre de C dans le fichier FASTA: ' + str(c_count))


def calc_g(nucleotid_list):
    g_count = 0
    for char in nucleotid_list:
        if str(char) == 'G':
            g_count = g_count + 1
    print('Nombre de G dans le fichier FASTA: ' + str(g_count))


def calc_t(nucleotid_list):
    t_count = 0
    for char in nucleotid_list:
        if str(char) == 'T':
            t_count = t_count + 1
    print('Nombre de T dans le fichier FASTA: ' + str(t_count))


if __name__ == '__main__':
    with open('test.fa', 'r') as f:
        NUCLEOTIDLIST = decoupe(f)
        THREAD1 = threading.Thread(target=calc_a, args=(NUCLEOTIDLIST,))
        THREAD1.start()
        THREAD2 = threading.Thread(target=calc_c, args=(NUCLEOTIDLIST,))
        THREAD2.start()
        THREAD3 = threading.Thread(target=calc_g, args=(NUCLEOTIDLIST,))
        THREAD3.start()
        THREAD4 = threading.Thread(target=calc_t, args=(NUCLEOTIDLIST,))
        THREAD4.start()
