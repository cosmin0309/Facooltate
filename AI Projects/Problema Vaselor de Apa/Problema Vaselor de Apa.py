#LAB 6 PB 5
import copy
import time

"""ENUNT:
Consideram ca avem niste vase cu apa colorata. Despre fiecare vas stim capacitatea maxima si cat
lichid contine. Pot exista si vase vide. De asemenea pentru combinatia a doua culori de lichide stim ce
culoare rezulta din combinatia lor. Pentru combinatiile de culori neprecizate, inseamna ca nu ne
intereseaza rezultatul si desi le putem amesteca (uneori e nevoie sa depozitam apa intr-un vas, ca sa
facem loc pentru alte mutari) culoarea rezultata nu va aparea in starea solutie niciodata (puteti
considera un identificator special pentru acea culoare, de exemplu "nedefinit"). Evident, apa cu culoare
nedefinita nu poate fi folosita pentru a obtine alte culori (apa cu culoare nedefinita, amestecata cu orice
rezulta in culoare nedefinita).
Lichidul dintr-un vas nu poate fi varsat decat in alt vas (nu dorim sa pierdem din lichid; nu se varsa in
exterior).
Formatul fisierului de intrare:
Primele randuri se vor referi la combinatiile de culori. Vor fi cate 3 pe rand, de exemplu:
c1 c2 c3
cu semnificatia ca din combinarea culorii c1 cu c2 rezulta c3 (nu conteaza cantitatea apei amestecate
ci doar culoarea ei). Combinatiile sunt simetrice, adica, daca din c1 combinat cu c2 rezulta c3, atunci si
din c2 combinat cu c1 rezulta c3.
Sub randurile cu culorile avem un rand cu textul "stare_initiala", dupa care urmeaza starea initiala a
vaselor. Pentru fiecare vas se precizeaza cantitatea maxima a acestuia, cata apa are si ce culoare are
apa. Toate cantitatile sunt date in litri. In cazul in care cantitatea de apa este 0, lipseste si culoarea.
Dupa precizarea starii, initiale, avem textul "stare_finala". Sub acest text pe cate un rand, se specifica
o cantitate si o culoare, cu sensul ca in starea finala, pentru fiecare astfel de cantitate (si culoare)
precizata trebuie sa existe un vas care sa o contina. Tranzitia consta din turnarea apei dintr-un vas in
altul. Se considera ca nu stim sa masuram litrii altfel decat folosind vasele. Cand turnam lichid putem
turna ori pana se termina lichidul din vasul din care turnam, ori pana se umple vasul in care
turnam.. Nu se varsa lichid in exterior, lichidul nu da pe afara. Asfel daca, de exemplu, am un vas
cu capacitate 6 si cantitate 3 si unul cu capacitate 4 si cantitate 2, nu putem turna din primul doar un
litru, ci doar 2 litri (fiindca sunt 4-2=2 litri liberi in vasul al doilea). In felul asta ramanem cu un litru in
primul.
Ne oprim din cautat cand reusim sa ajungem in starea finala: cu alte cuvinte, cand fiecare cantitate de
apa colorata specificata in stare se gaseste in cate un vas (nu ne intereseaza cantitatile de apa din
restul vaselor)
Exemplu de fisier de intrare:
rosu albastru mov
albastru galben verde
mov verde maro
stare_initiala
5 4 rosu
2 2 galben
3 0
7 3 albastru
1 0
4 3 rosu
stare_finala
3 mov
2 verde
In fisierul de output se vor afisa starile intermediare, pornind de la starea initiala la starea finala.
Pentru fiecare vase se aloca un id (poate fi numarul de ordine din fisier - de exemplu, vasul cu id-ul 0
este cel cu capacitate 5 si 4 litri de apa rosie)

- 4 -

O stare se va afisa, afisand intai (daca nu e vorba de prima stare) ce miscare s-a facut, in formatul:
Din vasul X s-au turnat L litri de apa de culoare C in vasul Y.
Apoi se va afisa starea vaselor astfel:
id_vas: capacitate_maxima cantitate_apa culoare_apa
De exemplu, pentru un succesor al starii initiale de mai sus am avea:
Din vasul 0 s-au turnat 1 litri de apa de culoare rosu in vasul 4.
0: 5 3 rosu
1: 2 2 galben
2: 3 0
3: 7 3 albastru
4: 1 1 rosu
5: 4 3 rosu
Insa starea initiala s-ar fi afisat in drum fara randul cu mutarea:
0: 5 4 rosu
1: 2 2 galben
2: 3 0
3: 7 3 albastru
4: 1 0
5: 4 3 rosu

Nu ne preocupam de corectitudine gramaticala ("culoare rosie" in loc de "culoare rosu").
Cand se afiseaza "drumul" de stari, se afiseaza si prima stare in formatul de mai sus (cu id-urile vaselor),
dar fara mesajul mutarii.
Un exemplu de distributie a apei intr-o stare finala este (observam ca nu am precizat culoarea pentru
cantitate 0):
0: 5 5 rosu
1: 2 1 galben
2: 3 1 albastru
3: 7 2 verde
4: 1 0
5: 4 3 mov
Indicatie: nu precizati toate starile finale posibile, ci faceti o functie care testeaza daca o stare
indeplineste conditia ceruta.
Alte precizari:
• Pentru fisierele de input nu e obligatoriu sa folositi nume reale de culori
• Nu e obligatoriu sa se foloseasca toate culorile in starea finala.
"""

"""definirea problemei"""
fisiere_input = ["input_1.txt", "input_2.txt", "input_3.txt"]
fisiere_output = ["output_1.txt", "output_2.txt", "output_3.txt"]

class Vas:
    def __init__(self, id, capacitate, continut, culoare=None):
        self.id = id
        self.capacitate = capacitate
        self.continut = continut
        self.culoare = culoare

    def __str__(self):
        return "{} : {} {} {}\n".format(self.id, self.capacitate, self.continut, self.culoare)

    def __repr__(self):
        return f"({self.id} : {self.capacitate} {self.continut} {self.culoare})"


class Amestec:
    def __init__(self, c1, c2, c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def __str__(self):
        return "({} + {} = {})".format(self.c1, self.c2, self.c3)

    def __repr__(self):
        return f"({self.c1} + {self.c2} = {self.c3} )"


class StareFinala:
    def __init__(self, cantitate, culoare):
        self.cantitate = cantitate
        self.culoare = culoare


class Nod:
    def __init__(self, info, h=1):
        self.info = info  # info este o configuratie a vaselor,
        self.h = h  # practic fiecare nod reprezinta o configuratie

    miscare = ""

    def __str__(self):
        return "{}\n".format(self.info)

    def __repr__(self):
        return f"{self.info}"


class Arc:
    def __init__(self, capat, varf, cost=1):
        self.capat = capat
        self.varf = varf
        self.cost = cost


class Problema:
    def __init__(self, noduri=[], nod_start=None):
        self.noduri = noduri
        self.nod_scop = []  # de tip StareFinala
        self.arce = []
        self.nod_start = nod_start

    amestecuri = []

    def cauta_nod_nume(self, info):
        for nod in self.noduri:
            if nod.info == info:
                return nod
        return None


""" Sfarsit definire problema """

""" Clase folosite in algoritmul A* """


class NodParcurgere:
    """O clasa care cuprinde informatiile asociate unui nod din listele open/closed
    	Cuprinde o referinta catre nodul in sine (din graf)
    	dar are ca proprietati si valorile specifice algoritmului A* (f si g).
    	Se presupune ca h este proprietate a nodului din graf

    """

    problema = Problema()  # atribut al clasei
    amestecuri = []

    def __init__(self, nod_graf, parinte=None, g=0, f=None):
        self.nod_graf = nod_graf  # obiect de tip Nod
        self.parinte = parinte  # obiect de tip Nod
        self.g = g  # costul drumului de la radacina pana la nodul curent(vom calcula costul ca fiind inaltimea
        # subarborelui determinat de radacina si de nodul curent  )
        if f is None:
            self.f = self.g + self.nod_graf.h
        else:
            self.f = f

    def __str__(self):
        parinte = self.parinte if self.parinte is None else self.parinte.nod_graf.info
        return "({})".format(self.nod_graf)

    def amesteca(self, c1, c2):
        if c1 == c2:
            return c1
        if c1 == None:
            return c2
        if c2 == None:
            return c1
        for amestec in self.amestecuri:
            if amestec.c1 == c1 and amestec.c2 == c2 or amestec.c2 == c1 and amestec.c1 == c2:
                return amestec.c3
        return "undef"

    def drum_arbore(self, fisier_output):
        """
        	Functie care calculeaza drumul asociat unui nod din arborele de cautare.
        	Functia merge din parinte in parinte pana ajunge la radacina
        """
        nod_c = self
        drum = [nod_c]
        while nod_c.parinte is not None:
            drum = [nod_c.parinte] + drum
            nod_c = nod_c.parinte
            # print(nod_c.parinte.miscare)
        fisier_output.write("Stare initiala :")

        for miscare in drum:
            fisier_output.write(miscare.nod_graf.miscare)
            fisier_output.write("\n\n")
            for nod in miscare.nod_graf.info:
                fisier_output.write(str(nod) + "\n\n")
        return drum

    def contine_in_drum(self, nod):
        """
        	Functie care verifica daca nodul "nod" se afla in drumul dintre radacina si nodul curent (self).
        	Verificarea se face mergand din parinte in parinte pana la radacina
        	Se compara doar informatiile nodurilor (proprietatea info)
        	Returnati True sau False.

        	"nod" este obiect de tip Nod (are atributul "nod.info")
        	"self" este obiect de tip NodParcurgere (are "self.nod_graf.info")
        """
        ### TO DO ... DONE
        nod_c = self
        while nod_c.parinte is not None:
            if nod.info == nod_c.nod_graf.info:
                return True
            nod_c = nod_c.parinte
        return False

    def expandeaza(self):
        """
        Creez un nou nod modificand nodul self prin efectuarea unei singure miscari
        (adica o varsare dintr-un vas care este echivalenta cu o turnare in alt vas)
        execut pe rand toate combinatiile posibile: iau vasul cu indicele 0 din
         self.nod_graf.info, parcurg lista cu toate vasele iar daca pot turna intr-un vas
         si acel vas este diferit de vasul curent(indicele vasului din care torn este
        diferit de indicele vasului in care torn) aplic miscarea"""

        de_varsat = 0
        l_succesori = []
        for ivas in self.nod_graf.info:

            if ivas.continut != 0:
                """Iau fiecare vas in parte si ii creez o noua configuratie astfel: 
                daca din vasul i pot sa vars apa in oricare alt vas,o cantitate apa din i
                 se adauga in vasul respectiv, aceasta reprezentand o noua configuratie"""
                for ivas_curent in self.nod_graf.info:
                    if ivas_curent.continut < ivas_curent.capacitate and ivas_curent.id != ivas.id:  # adica nu e plin si nu este vasul curent
                        vas_temp = Vas(ivas_curent.id, ivas_curent.capacitate, ivas_curent.continut,
                                       ivas_curent.culoare)
                        if ivas.continut + ivas_curent.continut <= ivas_curent.capacitate:#daca il vars
                                                                                            # pe tot nu da pe afara
                            de_varsat = ivas.continut
                        else:  # trebuie sa vars doar o parte
                            de_varsat = ivas_curent.capacitate - ivas_curent.continut
                        vas_temp2 = Vas(ivas.id, ivas.capacitate, ivas.continut, ivas.culoare)
                        vas_temp2.continut = vas_temp2.continut - de_varsat
                        # print(ivas)
                        vas_temp.continut = vas_temp.continut + de_varsat
                        vas_temp.culoare = self.amesteca(ivas.culoare, ivas_curent.culoare)
                        nod_temp = copy.deepcopy(self.nod_graf)
                        # print("nod temp " + str(nod_temp))
                        nod_temp.info[ivas_curent.id] = vas_temp
                        nod_temp.info[ivas.id] = vas_temp2
                        if nod_temp.info[ivas.id].continut == 0:
                            nod_temp.info[ivas.id].culoare = None

                        if de_varsat > 0:

                            #print("----------------------------------------------")
                            nod_temp.miscare = ("Din vasul " + str(ivas.id) + " s-au turnat " + str(de_varsat) +
                                                " litri de apa de culoare " + str(ivas.culoare) + " in vasul " + str(
                                        ivas_curent.id))
                            l_succesori.append((nod_temp, 1))

        return l_succesori

    def test_scop(self):
        """ Caut elementele date in lista starilor finale (salvate in nod_scop) in elementele din self
         daca am parcurs toata lista si nu am gasit ce cautam, returnez false, altfel returnez true"""

        sem = True
        #print("De cautat " + str(self.problema.nod_scop))
        for i in self.problema.nod_scop:
            for j in self.nod_graf.info:
                #print("compar " + str(j.culoare) + " cu " + str(i.culoare) + " si " + str(j.continut) + " cu " + str(
                 #   i.continut))
                if j.culoare == i.culoare and \
                        j.continut == i.continut:
                  #  print("Contine " + i.culoare)
                    break
                if j.id == len(self.nod_graf.info) - 1:
                    sem = False
        # print("sem == " + str(sem))
        return sem


""" Algoritmul A* """


def str_info_noduri(l):
    "O functie folosita strict in afisari"
    sir = "["
    for x in l:
        sir += str(x) + " "
    sir += "]"
    return sir


def afis_succesori_cost(l):
    """
        o functie folosita strict in afisari
    """
    sir = ""
    for (x, cost) in l:
        sir += "\nnod: " + str(x) + ", cost arc:" + str(cost)
    return sir


def in_lista(l, nod):
    """
    		lista "l" contine obiecte de tip NodParcurgere
    		"nod" este de tip Nod
    	"""
    for i in range(len(l)):
        if l[i].nod_graf.info == nod.info:
            # print("Am gasit!!!")
            return l[i]
    return None


def a_star(fisier_output):
    rad_arbore = NodParcurgere(NodParcurgere.problema.nod_start)
    # rad_arbore.problema = nod.problema
    open = [rad_arbore]  # open va contine elemente de tip NodParcurgere
    # print(rad_arbore.problema.nod_scop)
    if rad_arbore.test_scop():
        str_info_noduri(rad_arbore.drum_arbore(fisier_output))
        fisier_output.write("\n Stara initiala este si starea finala ")
        fisier_output.close()
        return
    closed = []  # closed va contine elemente de tip NodParcurgere
    while len(open) > 0:
        nod_curent = open.pop(0)  # scoatem primul element din lista open
        closed.append(nod_curent)  # si il adaugam la finalul listei closed
        # testez daca nodul extras din lista open este nod scop (si daca da, ies din bucla while)
        if nod_curent.test_scop():
            break

        l_succesori = nod_curent.expandeaza()  # contine tupluri de tip (Nod, numar)
        for (nod_succesor, cost_succesor) in l_succesori:
            # "nod_curent" este tatal, "nod_succesor" este fiul curent

            # daca fiul nu e in drumul dintre radacina si tatal sau (adica nu se creeaza un circuit)
            if (not nod_curent.contine_in_drum(nod_succesor)):

                # calculez valorile g si f pentru "nod_succesor" (fiul)
                g_succesor = nod_curent.g + cost_succesor  # g-ul tatalui + cost muchie(tata, fiu)
                f_succesor = g_succesor + nod_succesor.h  # g-ul fiului + h-ul fiului
                # verific daca "nod_succesor" se afla in closed
                # (si il si sterg, returnand nodul sters in nod_parcg_vechi
                nod_parcg_vechi = in_lista(closed, nod_succesor)
                if nod_parcg_vechi is not None:  # "nod_succesor" e in closed
                    # daca f-ul calculat pentru drumul actual este mai bun (mai mic) decat
                    # 	   f-ul pentru drumul gasit anterior (f-ul nodului aflat in lista closed)
                    # atunci actualizez parintele, g si f
                    # si apoi voi adauga "nod_nou" in lista open

                    if (f_succesor < nod_parcg_vechi.f):
                        closed.remove(nod_parcg_vechi)  # scot nodul din lista closed
                        nod_parcg_vechi.parinte = nod_curent  # actualizez parintele
                        nod_parcg_vechi.g = g_succesor  # actualizez g
                        nod_parcg_vechi.f = f_succesor  # actualizez f
                        nod_nou = nod_parcg_vechi  # setez "nod_nou", care va fi adaugat apoi in open

                else:
                    # daca nu e in closed, verific daca "nod_succesor" se afla in open
                    nod_parcg_vechi = in_lista(open, nod_succesor)

                    if nod_parcg_vechi is not None:  # "nod_succesor" e in open
                        # daca f-ul calculat pentru drumul actual este mai bun (mai mic) decat
                        # 	   f-ul pentru drumul gasit anterior (f-ul nodului aflat in lista open)
                        # atunci scot nodul din lista open
                        # 		(pentru ca modificarea valorilor f si g imi va strica sortarea listei open)
                        # actualizez parintele, g si f
                        # si apoi voi adauga "nod_nou" in lista open (la noua pozitie corecta in sortare)
                        if (f_succesor < nod_parcg_vechi.f):
                            open.remove(nod_parcg_vechi)
                            nod_parcg_vechi.parinte = nod_curent
                            nod_parcg_vechi.g = g_succesor
                            nod_parcg_vechi.f = f_succesor
                            nod_nou = nod_parcg_vechi

                    else:  # cand "nod_succesor" nu e nici in closed, nici in open
                        nod_nou = NodParcurgere(nod_graf=nod_succesor, parinte=nod_curent, g=g_succesor)
                    # se calculeaza f automat in constructor

                if nod_nou:
                    # inserare in lista sortata crescator dupa f
                    # (si pentru f-uri egale descrescator dupa g)
                    i = 0
                    while i < len(open):
                        if open[i].f < nod_nou.f:
                            i += 1
                        else:
                            while i < len(open) and open[i].f == nod_nou.f and open[i].g > nod_nou.g:
                                i += 1
                            break

                    open.insert(i, nod_nou)

    print("\n------------------ Concluzie -----------------------")

    if len(open) == 0:
        fisier_output.write("Lista open e vida, nu avem drum de la nodul start la nodul scop")
        print("Lista open e vida, nu avem drum de la nodul start la nodul scop")
    else:
        str_info_noduri(nod_curent.drum_arbore(fisier_output))
        fisier_output.close()


if __name__ == "__main__":

    i = 0
    for file_name in fisiere_input:
        start_time = time.time()
        problema = Problema()
        print(file_name)
        File_object = open(file_name, "r")
        amestecuri = File_object.readline()
        # citesc amestecurile
        while str(amestecuri).strip() != str("stare_initiala").strip():
            amestecuri_list = amestecuri.split()
            problema.amestecuri.append(Amestec(amestecuri_list[0], amestecuri_list[1], amestecuri_list[2]))
            amestecuri = File_object.readline()
        # citesc vasele
        vase = File_object.readline()
        index = 0
        vase_de_adaugat = []
        while str(vase).strip() != str("stare_finala").strip():
            vase_list = vase.split()
            if len(vase_list) == 2:
                vas = Vas(int(index), int(vase_list[0]), int(vase_list[1]))
            else:
                vas = Vas(int(index), int(vase_list[0]), int(vase_list[1]), vase_list[2])
            vase_de_adaugat.append(vas)
            index = index + 1
            vase = File_object.readline()
        problema.noduri.append(Nod(vase_de_adaugat, 1))

        problema.nod_start = problema.noduri[0]

        # citesc starea finala
        stare_finala = File_object.readline()
        while str(stare_finala).strip() != None:
            stare_finala_list = stare_finala.split()
            if not stare_finala_list:
                break
            problema.nod_scop.append(Vas(None, None, int(stare_finala_list[0]), stare_finala_list[1]))
            stare_finala = File_object.readline()
        NodParcurgere.amestecuri = problema.amestecuri
        NodParcurgere.problema = problema
        File_object.close()
        File_object2 = open(fisiere_output[i], "w+")
        i = i + 1
        a_star(File_object2)

        NodParcurgere.amestecuri.clear()
        NodParcurgere.problema.noduri.clear()

        del problema
        del File_object
        del File_object2
        del amestecuri
        del amestecuri_list
        del vas
        del vase
        del vase_list
        del vase_de_adaugat
        del index
        del stare_finala
        del stare_finala_list
        print("-----% s Seconds-----" % (time.time() - start_time))