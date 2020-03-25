import unittest
import pile_file


class TestPile(unittest.TestCase):
    """
    Test des fonctions de la classe Pile
    """

    def test_init(self):
        """
        Test si une pile que l'on vient de créer est vide
        """
        stack = pile_file.Pile()
        self.assertEqual(0, stack.size())

    def test_non_vide(self):
        """
        Test si une pile sur laquelle on vient d’empiler un élément est non vide
        """
        stack = pile_file.Pile()
        stack.empiler(5)
        self.assertEqual(False, stack.pileVide())

    def test_empiler_depiler(self):
        """
        Test si une pile qui subit un empilement suivi d’un dépilement est inchangée
        """
        stack = pile_file.Pile()
        stack.empiler(5)
        stack.depiler()
        self.assertEqual(True, stack.pileVide())

    def test_sommet(self):
        """
        Test que le sommet d’une pile sur laquelle on vient d’empiler un élément e est e.
        """
        stack = pile_file.Pile()
        stack.empiler(5)
        self.assertEqual(5, stack.sommet())

    def test_depiler_vide(self):
        """
        Lever une exception si on veut depiler une pile vide
        """
        stack = pile_file.Pile()
        self.assertRaises(IndexError, stack.depiler())

    def test_sommet_vide(self):
        """
        lever une exception si on veut lire le sommet d'une pile vide
        """
        stack = pile_file.Pile()
        self.assertRaises(IndexError, stack.sommet())


class TestFile(unittest.TestCase):
    """
    Test des fonctions de la classe file
    """

    def test_init(self):
        """
        Une file que l'on vient de créer est vide
        """
        queue = pile_file.File()
        self.assertEqual(0, queue.size())

    def test_tete_enfilee(self):
        """
        Si une file est vide, alors la tête d’une file sur laquelle on enfile un élément e est e.
        """
        queue = pile_file.File()
        queue.enfiler(5)
        self.assertEqual(5, queue.tete())

    def test_tete(self):
        """
        la tête d’une file sur laquelle on enfile un élément e est identique à la
        tête de la file avant  d’enfilement
        """
        queue = pile_file.File()
        queue.enfiler(5)
        queue.enfiler(8)
        head = queue.tete()
        queue.enfiler(6)
        self.assertEqual(head, queue.tete())

    def test_enfiler1_defiler1(self):
        """
        Une file vide qui subit un enfilement suivi d’un défilement est toujours une file vide
        """
        queue = pile_file.File()
        queue.enfiler(5)
        queue.defiler()
        self.assertEqual(True, queue.fileVide())

    def test_operations_equivalentes(self):
        """
        un enfilement suivi d’un défilement est identique à un défilement suivi d’un
        enfilement.
        """
        queue1 = pile_file.File()
        queue1.enfiler(1)
        queue1.enfiler(2)
        queue2 = queue1
        queue1.enfiler(3)
        queue1.defiler()
        queue2.defiler()
        queue2.enfiler(3)
        self.assertEqual(queue1, queue2)

    def test_defiler_vide(self):
        """
        defiler une file vide leve une exception
        """
        queue = pile_file.File()
        self.assertRaises(IndexError, queue.defiler())

    def test_tete_file_vide(self):
        """
        lire la tete d'une dile vide leve une exception
        """
        queue = pile_file.File()
        self.assertRaises(IndexError, queue.tete())


if __name__ == '__main__':
    unittest.main()
