import re
import concurrent.futures


def count_nucleotid_occurences(character: str, nucleotids: str) -> int:
    """ Compte le nombre d'occurence d'un nucléotique """
    character_occurence = 0

    for nucleotid in nucleotids:
        if character == nucleotid:
            character_occurence += 1

    return character_occurence


def retrieve_sequences(buffer: str) -> list:
    """ Récupère séparémment les deux séquences de nucléotides du fichier """
    regexp = re.compile('^>.*$', re.MULTILINE)
    sequences = regexp.split(buffer)

    sequences.pop(0)
    sequences[0] = sequences[0].replace('\n', '')
    sequences[1] = sequences[1].replace('\n', '')

    return sequences


def start_threads(sequences, occurences):
    """
        Utilise le module executor pour lancer des threads et stocker le résultat
        des fonctions parralélisés dans un dictionnaire
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for character in list(occurences.keys()):
            # Lance la fonction
            futur = executor.submit(count_nucleotid_occurences, character, sequences)
            # Récupère le  résultat
            occurences[character] = futur.result()


def main():
    with open('data/test.fa', 'r') as file:
        buffer = file.read()

    sequences = retrieve_sequences(buffer)

    occurences_seq1 = {'A' : 0, 'T' : 0, 'C' : 0, 'G' : 0}
    occurences_seq2 = {'A' : 0, 'T' : 0, 'C' : 0, 'G' : 0}

    start_threads(sequences[0], occurences_seq1)
    print(occurences_seq1)
    start_threads(sequences[1], occurences_seq2)
    print(occurences_seq2)


if __name__ == '__main__':
    main()
