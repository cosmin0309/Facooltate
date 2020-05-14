#LAB9 PB 6
import math
import copy
import time

""" CHECKERS """
class Joc:
    DIMENSIUNE = 8
    SIMBOLURI_JUC = ['a', 'n']
    JMIN = SIMBOLURI_JUC[0]
    JMAX = SIMBOLURI_JUC[1]
    GOL = "#"
    MISCARE = ""

    def __init__(self, tabla=None):
        self.matr = tabla or [
            Joc.GOL] * self.DIMENSIUNE * self.DIMENSIUNE  # pentru a accesa un element:
                                                          # a[linie][coloana] = lista[linie * dimensiune + coloana]

    def populeaza_tabla(self):
        for i in range(int(self.DIMENSIUNE / 2) - 1):
            for j in range(self.DIMENSIUNE):
                if i % 2 == 0:
                    if j % 2 == 1:
                        self.matr[i * self.DIMENSIUNE + j] = "a"
                else:
                    if j % 2 == 0:
                        self.matr[i * self.DIMENSIUNE + j] = "a"

        for i in range(int(self.DIMENSIUNE / 2) + 1, self.DIMENSIUNE):
            for j in range(self.DIMENSIUNE):
                if i % 2 == 0:
                    if j % 2 == 1:
                        self.matr[i * self.DIMENSIUNE + j] = "n"
                else:
                    if j % 2 == 0:
                        self.matr[i * self.DIMENSIUNE + j] = "n"

    def final(self):  # pentru a distinge spatiile negre de cele albe : daca linia este para
        if 'a' not in self.matr and 'A' not in self.matr:  # atunci spatiile negre se afla pe coloanele impare
            return 'n'  # altfel, daca linia este impara, spatiile negre se afla pe coloanele pare
        if 'n' not in self.matr and 'N' not in self.matr:  # pentru a accesa elementul care se gaseste pe
            return 'a'  # a[i DIMENSIUNE +/- 1]# diagonala elementului curent
        sem = False

        for linie1 in range(self.DIMENSIUNE):
            for coloana1 in range(self.DIMENSIUNE):
                for linie2 in range(self.DIMENSIUNE):
                    for coloana2 in range(self.DIMENSIUNE):
                        if self.matr[linie1 * self.DIMENSIUNE + coloana1] == 'a' or \
                                self.matr[linie1 * self.DIMENSIUNE + coloana1] == 'A':
                            if self.se_poate_muta(linie1, coloana1, linie2, coloana2,
                                                  self.matr[linie1 * self.DIMENSIUNE + coloana1], self.matr):
                                sem = True

            if linie1 == self.DIMENSIUNE - 1 and sem == False:
                return 'n'

        sem = False

        for linie1 in range(self.DIMENSIUNE):
            for coloana1 in range(self.DIMENSIUNE):
                for linie2 in range(self.DIMENSIUNE):
                    for coloana2 in range(self.DIMENSIUNE):
                        if self.matr[linie1 * self.DIMENSIUNE + coloana1] == 'n' or \
                                self.matr[linie1 * self.DIMENSIUNE + coloana1] == 'N':

                            if self.se_poate_muta(linie1, coloana1, linie2, coloana2,
                                                  self.matr[linie1 * self.DIMENSIUNE + coloana1], self.matr):
                                sem = True
            if linie1 == self.DIMENSIUNE - 1 and sem == False:
                return 'a'

        return False

    def e_neagra(self, pozitie):
        for i in range(self.DIMENSIUNE):
            for j in range(self.DIMENSIUNE):
                if pozitie == i * self.DIMENSIUNE + j:
                    if (i % 2) == (j % 2):
                        return True
                    break
                return False

    def se_poate_muta(self, linie1, coloana1, linie2, coloana2, piesa, matr):
        """O functie pentru a verifica daca o piesa de pe pozitia 1 se poate muta pe pozitia 2
        Mai intai verificam daca pozitia pe care se doreste sa se faca mutarea se afla pe diagonala fata de pozitia
        de pe care se vrea sa se execute miscarea
        Mai intai pentru piesele care nu sunt regi"""
        if piesa == 'a':  # elementul de pe pozitia curenta
            # print(
            #   "pt " + str(linie1) + " " + str(coloana1) + " pe " + str(linie2) + " " + str(coloana2))
            if linie1 != (self.DIMENSIUNE - 1) and (linie2 != self.DIMENSIUNE - 1):

                if matr[linie2 * self.DIMENSIUNE + coloana2] == self.GOL:
                    return True
                else:
                    if matr[linie2 * self.DIMENSIUNE + coloana2] != piesa and coloana2 == 7 and (
                            matr[linie2 * self.DIMENSIUNE + coloana2 + self.DIMENSIUNE - 1] == self.GOL):
                        return True
                    if matr[linie2 * self.DIMENSIUNE + coloana2] != piesa and coloana2 == 0 and (
                            matr[linie2 * self.DIMENSIUNE + coloana2 + self.DIMENSIUNE + 1] == self.GOL):
                        return True
                    if matr[linie2 * self.DIMENSIUNE + coloana2] != piesa and (coloana2 == 7 and \
                                                                               matr[
                                                                                   linie2 * self.DIMENSIUNE + coloana2 + self.DIMENSIUNE - 1] == self.GOL):
                        return True
                    if matr[linie2 * self.DIMENSIUNE + coloana2] != piesa and (coloana2 == 0 and \
                                                                               matr[
                                                                                   linie2 * self.DIMENSIUNE + coloana2 + self.DIMENSIUNE + 1] == self.GOL):
                        return True
                    if matr[linie2 * self.DIMENSIUNE + coloana2] != piesa and (
                            coloana2 != 7 and coloana2 != 1 and \
                            matr[linie2 * self.DIMENSIUNE + coloana2 + self.DIMENSIUNE + 1] == self.GOL or
                            matr[linie2 * self.DIMENSIUNE + coloana2 + self.DIMENSIUNE - 1] == self.GOL):
                        return True
            return False
        else:
            """Apoi pentru regi"""
            if piesa == 'A':  # elementul de pe pozitia curenta
                if matr[linie2 * self.DIMENSIUNE + coloana2] == self.GOL:
                    return True
                else:
                    if linie2 * self.DIMENSIUNE + coloana2 > linie1 * self.DIMENSIUNE + coloana1:  # Daca merg in jos
                        if matr[linie2 * self.DIMENSIUNE + coloana2 + self.DIMENSIUNE + 1] == self.GOL or \
                                matr[linie2 * self.DIMENSIUNE + coloana2 + self.DIMENSIUNE - 1] == self.GOL:
                            return True
                        if linie2 * self.DIMENSIUNE + coloana2 < linie1 * self.DIMENSIUNE + coloana1:  # Daca merg in sus
                            if matr[linie2 * self.DIMENSIUNE + coloana2 - self.DIMENSIUNE + 1] == self.GOL or \
                                    matr[linie2 * self.DIMENSIUNE + coloana2 - self.DIMENSIUNE - 1] == self.GOL:
                                return True

        if piesa == 'n':  # elementul de pe pozitia curenta
            # print(
            #   "pt " + str(linie1) + " " + str(coloana1) + " pe " + str(linie2) + " " + str(coloana2))
            if linie1 != 0 and (linie2 != 0):

                if matr[linie2 * self.DIMENSIUNE + coloana2] == self.GOL:
                    return True
                else:
                    if matr[linie2 * self.DIMENSIUNE + coloana2] != piesa and coloana2 == 7 and (
                            matr[linie2 * self.DIMENSIUNE + coloana2 - self.DIMENSIUNE - 1] == self.GOL):
                        return True
                    if matr[linie2 * self.DIMENSIUNE + coloana2] != piesa and coloana2 == 0 and (
                            matr[linie2 * self.DIMENSIUNE + coloana2 - self.DIMENSIUNE + 1] == self.GOL):
                        return True
                    if matr[linie2 * self.DIMENSIUNE + coloana2] != piesa and (coloana2 == 7 and \
                                                                               matr[
                                                                                   linie2 * self.DIMENSIUNE + coloana2 - self.DIMENSIUNE - 1] == self.GOL):
                        return True
                    if matr[linie2 * self.DIMENSIUNE + coloana2] != piesa and (coloana2 == 0 and \
                                                                               matr[
                                                                                   linie2 * self.DIMENSIUNE + coloana2 - self.DIMENSIUNE + 1] == self.GOL):
                        return True
                    if matr[linie2 * self.DIMENSIUNE + coloana2] != piesa and (
                            coloana2 != 7 and coloana2 != 1 and \
                            matr[linie2 * self.DIMENSIUNE + coloana2 - self.DIMENSIUNE + 1] == self.GOL or
                            matr[linie2 * self.DIMENSIUNE + coloana2 - self.DIMENSIUNE - 1] == self.GOL):
                        return True
            return False
        else:
            """Apoi pentru regi"""
            if piesa == 'N':  # elementul de pe pozitia curenta
                if matr[linie2 * self.DIMENSIUNE + coloana2] == self.GOL:
                    return True
                else:
                    if linie2 * self.DIMENSIUNE + coloana2 > linie1 * self.DIMENSIUNE + coloana1:  # Daca merg in jos
                        if matr[linie2 * self.DIMENSIUNE + coloana2 + self.DIMENSIUNE + 1] == self.GOL or \
                                matr[linie2 * self.DIMENSIUNE + coloana2 + self.DIMENSIUNE - 1] == self.GOL:
                            return True
                        if linie2 * self.DIMENSIUNE + coloana2 < linie1 * self.DIMENSIUNE + coloana1:  # Daca merg in sus
                            if matr[linie2 * self.DIMENSIUNE + coloana2 - self.DIMENSIUNE + 1] == self.GOL or \
                                    matr[linie2 * self.DIMENSIUNE + coloana2 - self.DIMENSIUNE - 1] == self.GOL:
                                return True
        return False

    def mutari_joc(self):  # vom genera toate mutarile doar pentru jmax deoarece acela este calculatorul
        lista_mutari = []
        # print("in mutari pt : \n " + str(self))
        for linie in range(self.DIMENSIUNE):
            for coloana in range(self.DIMENSIUNE):
                matr_temp = copy.deepcopy(self.matr)
                if matr_temp[linie * self.DIMENSIUNE + coloana] == 'a':
                    linie_noua = linie + 1
                    coloana_noua = coloana - 1
                    # print(str(linie) + " " + str(coloana))
                    if self.se_poate_muta(linie, coloana, linie_noua, coloana_noua, 'a', matr_temp) \
                            and 0 <= coloana_noua < 8:
                        matr_temp[linie * self.DIMENSIUNE + coloana] = self.GOL
                        matr_temp[linie_noua * self.DIMENSIUNE + coloana_noua] = 'a'
                        if linie_noua == 7:
                            matr_temp[linie_noua * self.DIMENSIUNE + coloana_noua] = 'A'
                        joc_de_adaugat = Joc(matr_temp)
                        joc_de_adaugat.MISCARE = "Am mutat de pe pozitia [" + str(linie) + "][" + str(coloana) + \
                                                 "] pe pozitia [" + str(linie_noua) + "][" + str(coloana_noua) + "]\n"
                        lista_mutari.append(joc_de_adaugat)
                        # print(joc_de_adaugat.MISCARE)
                        # print(joc_de_adaugat)
                        matr_temp = copy.deepcopy(self.matr)

                    linie_noua = linie + 1
                    coloana_noua = coloana + 1
                    if self.se_poate_muta(linie, coloana, linie_noua, coloana_noua, 'a', matr_temp) and \
                            0 <= coloana_noua < 8:
                        matr_temp[linie * self.DIMENSIUNE + coloana] = self.GOL
                        matr_temp[linie_noua * self.DIMENSIUNE + coloana_noua] = 'a'
                        if linie_noua == 7:
                            matr_temp[linie_noua * self.DIMENSIUNE + coloana_noua] = 'A'
                        joc_de_adaugat = Joc(matr_temp)
                        joc_de_adaugat.MISCARE = "Am mutat de pe pozitia [" + str(linie) + "][" + str(coloana) + \
                                                 "] pe pozitia [" + str(linie_noua) + "][" + str(coloana_noua) + "]\n"
                        lista_mutari.append(joc_de_adaugat)
                        # print(joc_de_adaugat)

                        # print(joc_de_adaugat.MISCARE)

                coloana_noua = coloana + 1
                if matr_temp[linie * self.DIMENSIUNE + coloana] == 'A' and \
                        0 <= coloana_noua < 8:  # or self.matr[i * self.DIMENSIUNE + j] == 'A':
                    linie_noua = linie + 1
                    coloana_noua = coloana + 1
                    if self.se_poate_muta(linie, coloana, linie_noua, coloana_noua, 'A', matr_temp):
                        matr_temp[linie * self.DIMENSIUNE + coloana] = self.GOL
                        matr_temp[linie_noua * self.DIMENSIUNE + coloana_noua] = 'n'
                        if linie_noua == 7:
                            matr_temp[linie_noua * self.DIMENSIUNE + coloana_noua] = 'N'
                        joc_de_adaugat = Joc(matr_temp)
                        joc_de_adaugat.MISCARE = "Am mutat de pe pozitia [" + str(linie) + "][" + str(coloana) + \
                                                 "] pe pozitia " + str(linie_noua) + "][" + str(coloana_noua) + "]\n"
                        lista_mutari.append(joc_de_adaugat)
                        # print(joc_de_adaugat)
                        # print(joc_de_adaugat.MISCARE)

                    linie_noua = linie + 1
                    coloana_noua = coloana - 1
                    if self.se_poate_muta(linie, coloana, linie_noua, coloana_noua, 'A', matr_temp) and \
                            0 <= coloana_noua < 8:
                        matr_temp[linie * self.DIMENSIUNE + coloana] = self.GOL
                        matr_temp[linie_noua * self.DIMENSIUNE + coloana_noua] = 'n'
                        if linie_noua == 7:
                            matr_temp[linie_noua * self.DIMENSIUNE + coloana_noua] = 'N'
                        joc_de_adaugat = Joc(matr_temp)
                        joc_de_adaugat.MISCARE = "Am mutat de pe pozitia [" + str(linie) + "][" + str(coloana) + \
                                                 "] pe pozitia " + str(linie_noua) + "][" + str(coloana_noua) + "]\n"
                        lista_mutari.append(joc_de_adaugat)
                        # print(joc_de_adaugat)
                        # print(joc_de_adaugat.MISCARE)

        return lista_mutari

    def estimeaza_scor(self, adancime):

        if self.final() != False:
            if self.final() == 'a':
                return 1
            if self.final() == 'n':
                return -1
        else:
            albe = 0
            negre = 0
            for element in self.matr:
                if element == 'a':
                    albe = albe + 1
                if element == 'n':
                    negre = negre + 1
                if element == 'A':
                    albe = albe + 2
                if element == 'N':
                    negre = negre + 2

            return negre - albe

    def __str__(self):
        to_print = "    a   b   c   d   e   f   g   h\n__________________________________\n"
        print(self.matr[2])
        for i in range(len(self.matr)):
            if i % 8 == 0:
                to_print = to_print + str(int(i / 8)) + "  |" + str(self.matr[i]) + "   "
                continue
            if (i + 1) % 8 == 0:
                to_print = to_print + str(self.matr[i]) + "\n"
                continue
            to_print = to_print + str(self.matr[i]) + "   "
        return to_print


class Stare:
    ADANCIME_MAX = 0

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = Joc(tabla_joc)
        self.j_curent = j_curent

        self.adancime = adancime
        self.scor = scor
        self.mutari_posibile = []
        self.stare_aleasa = None

    def jucator_opus(self):
        if self.j_curent == 'a':
            return 'n'
        else:
            return 'a'

    def mutari_stare(self):
        #print("in mutari stare")
        list_stari = []
        stare_temp = copy.deepcopy(self)
        list_stari_mutari = []
        list_stari_mutari = stare_temp.tabla_joc.mutari_joc()
        # print(list_stari_mutari[0])
        # print(list_stari_mutari[1])
        for mutare in list_stari_mutari:
            list_stari.append(Stare(mutare.matr, stare_temp.j_curent,
                                    stare_temp.adancime - 1, stare_temp, mutare.estimeaza_scor))
        return list_stari

    def input_corect(self, l1, c1, l2, c2):
        # Mai intai verific daca [l2][c2] data este pe diagonala fata de [l1][c1]
        if (l1 * self.tabla_joc.DIMENSIUNE + c1 - self.tabla_joc.DIMENSIUNE + 1) == \
                (l2 * self.tabla_joc.DIMENSIUNE + c2) or \
                (l1 * self.tabla_joc.DIMENSIUNE + c1 - self.tabla_joc.DIMENSIUNE - 1) == \
                (l2 * self.tabla_joc.DIMENSIUNE + c2):
            if self.tabla_joc.matr[
                l1 * self.tabla_joc.DIMENSIUNE + c1] == 'n':  # elementul de pe pozitia curenta nu este rege
                if self.tabla_joc.matr[l2 * self.tabla_joc.DIMENSIUNE + c2] == self.tabla_joc.GOL:  # daca spatiul
                    # de pe pozitia pe care vreau sa mut este gol
                    return True
                else:
                    if self.tabla_joc.matr[l2 * self.tabla_joc.DIMENSIUNE + c2] != 'n' and \
                            self.tabla_joc.matr[l2 * self.tabla_joc.DIMENSIUNE + c2] != 'N' and (
                            self.tabla_joc.matr[l2 * self.tabla_joc.DIMENSIUNE + c2 -
                                                self.tabla_joc.DIMENSIUNE + 1] == self.tabla_joc.GOL or
                            self.tabla_joc.matr[l2 * self.tabla_joc.DIMENSIUNE + c2 -
                                                self.tabla_joc.DIMENSIUNE - 1] == self.tabla_joc.GOL):
                        return True
        """Apoi pentru regi"""
        if (l1 * self.tabla_joc.DIMENSIUNE + c1 - self.tabla_joc.DIMENSIUNE + 1) == \
                (l2 * self.tabla_joc.DIMENSIUNE + c2) or \
                (l1 * self.tabla_joc.DIMENSIUNE + c1 - self.tabla_joc.DIMENSIUNE - 1) == \
                (l2 * self.tabla_joc.DIMENSIUNE + c2) or \
                (l1 * self.tabla_joc.DIMENSIUNE + c1 + self.tabla_joc.DIMENSIUNE + 1) == \
                (l2 * self.tabla_joc.DIMENSIUNE + c2) or \
                (l1 * self.tabla_joc.DIMENSIUNE + c1 + self.tabla_joc.DIMENSIUNE - 1) == \
                (l2 * self.tabla_joc.DIMENSIUNE + c2):  # daca e pe diagonala
            if self.tabla_joc.matr[l1 * self.tabla_joc.DIMENSIUNE + c1] == 'N':  # elementul de pe pozitia curenta
                if self.tabla_joc.matr[l2 * self.tabla_joc.DIMENSIUNE + c2] == self.tabla_joc.GOL:  # daca spatiu e gol
                    return True
                else:
                    if (l2 * self.tabla_joc.DIMENSIUNE + c2) > (l1 * self.tabla_joc.DIMENSIUNE + c1):  # Daca merg jos
                        if self.tabla_joc.matr[l2 * self.tabla_joc.DIMENSIUNE + c2 + self.tabla_joc.DIMENSIUNE + 1] \
                                == self.tabla_joc.GOL or self.tabla_joc.matr[l2 * self.tabla_joc.DIMENSIUNE +
                                                                             c2 + self.tabla_joc.DIMENSIUNE - 1] == self.tabla_joc.GOL:
                            return True
                    if (l2 * self.tabla_joc.DIMENSIUNE + c2) < (l1 * self.tabla_joc.DIMENSIUNE + c1):  # Daca merg sus
                        if self.tabla_joc.matr[l2 * self.tabla_joc.DIMENSIUNE + c2 -
                                               self.tabla_joc.DIMENSIUNE + 1] == self.tabla_joc.GOL or \
                                self.tabla_joc.matr[l2 * self.tabla_joc.DIMENSIUNE +
                                                    c2 - self.tabla_joc.DIMENSIUNE - 1] == self.tabla_joc.GOL:
                            return True

        print("MISCARE INCORECTA")
        return False

    def executa_miscare(self):
        sem = False
        while sem == False:
            print("Dati pozitia piesei pe care doriti sa o mutati : \n")
            print("De pe Linia : ")
            linie = int(input())
            print("si Coloana : ")
            coloana = input()
            print("Dati pozitia unde vreti sa mutati piesa : ")
            print("Pe linia : ")
            linie_noua = int(input())
            print("si coloana : ")
            coloana_noua = input()
            coloana = ord(
                coloana) - 97  # convertesc literele in cifre pentru a imi fi mai usor sa ma deplasez in memorie
            coloana_noua = ord(coloana_noua) - 97
            if self.input_corect(linie, coloana, linie_noua, coloana_noua) == True:
                self.tabla_joc.matr[linie * self.tabla_joc.DIMENSIUNE + coloana] = self.tabla_joc.GOL
                self.tabla_joc.matr[linie_noua * self.tabla_joc.DIMENSIUNE + coloana_noua] = 'n'
                if linie_noua == 0:
                    self.tabla_joc.matr[linie_noua * self.tabla_joc.DIMENSIUNE + coloana_noua] = 'N'
                # print(self.tabla_joc)
                sem = True

    def __str__(self):
        return "Tabla joc :\n {} \nSimbolul jucatorului curent : {} \n".format(self.tabla_joc, self.j_curent)


def min_max(stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    # print(type(stare.tabla_joc))
    #print("In minmax starea curenta : ")
    #print(stare.tabla_joc)
    if stare.adancime == 0 or stare.tabla_joc.final():
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        stare.stare_aleasa = stare
        #print("AJA")
        return stare

    # Altfel, calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari_stare()
    #print("AAAAAAAAAAAAAAAAA")
    #for mutare in stare.mutari_posibile:
     #   print(mutare)
    #print("AAAAAAAAAAAAAAAAA")
    # aplic algoritmul minimax pe toate mutarile posibile
    # (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]
    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)

    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor
    # print("Sex" + str(stare.tabla_joc))
    return stare


def alpha_beta(alpha, beta, stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    if stare.adancime == 0 or stare.tabla_joc.final() :
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare
    # Conditia de retezare:
    if alpha >= beta:
        return stare # este intr-un interval invalid, deci nu o mai procesez
    # Calculez toate mutarile posibile din starea curenta (toti „fiii”)
    stare.mutari_posibile = stare.mutari_stare()
    if stare.j_curent == Joc.JMAX :
        scor_curent = float('-inf') # scorul „tatalui” de tip MAX
        # pentru fiecare „fiu” de tip MIN:
        for mutare in stare.mutari_posibile:
            # calculeaza scorul fiului curent
            stare_noua = alpha_beta(alpha, beta, mutare)
            # incerc sa imbunatatesc (cresc) scorul si alfa
            # „tatalui” de tip MAX, folosind scorul fiului curent
            if scor_curent < stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor
            if alpha < stare_noua.scor:
                alpha = stare_noua.scor
                if alpha >= beta: # verific conditia de retezare
                    break # NU se mai extind ceilalti fii de tip MIN
    elif stare.j_curent == Joc.JMIN :
        scor_curent = float('inf') # scorul „tatalui” de tip MIN
        # pentru fiecare „fiu” de tip MAX:
        for mutare in stare.mutari_posibile:
            stare_noua = alpha_beta(alpha, beta, mutare)
            # incerc sa imbunatatesc (scad) scorul si beta
            # „tatalui” de tip MIN, folosind scorul fiului curent
            if scor_curent > stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor
            if beta > stare_noua.scor:
                beta = stare_noua.scor
                if alpha >= beta: # verific conditia de retezare
                    break # NU se mai extind ceilalti fii de tip MAX
    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor
    return stare


if __name__ == "__main__":

    joc = Joc()
    joc.populeaza_tabla()
    # print(joc)
    stare = Stare(joc.matr, joc.JMIN, 2)
    # print(stare.adancime)
    stare.ADANCIME_MAX = 2
    # adancime
    # print(min_max(stare))
    # print(joc)

    sem = False
    while sem == False:
        print("Ce algoritm doriti sa se foloseasca ? (minimax/alpha-beta)")
        algortim = input()

        if algortim == "minimax":
            sem = True
            sem2 = False
            while sem2 == False:

                """Jucatorul va fi cu negre(jmin) iar calculatorul va fi cu albe(jmax)"""
                print("Care sa fie nivelul de dificultate?: \n-usor\n-mediu\n-greu")
                dif = input()
                if dif == "usor":
                    stare.ADANCIME_MAX = 2
                    sem2 = True
                if dif == "mediu":
                    stare.ADANCIME_MAX = 4
                    sem2 = True
                if dif == "greu":
                    stare.ADANCIME_MAX = 8
                    sem2 = True
            print("The Game is on : \n")
            print(joc)
            while stare.tabla_joc.final() == False or stare.ADANCIME_MAX != 0:
                print("Continuati?(yes/no)")
                if(input() == "no"):
                    if stare.scor > 0:
                        print("Castigator: Jucatorul")
                    else:
                        if stare.scor < 0:
                            print("Castigator: Calculatorul")
                        else:
                            print("EGALITATE")

                    break
                # cat timp nu sunt intr-o stare finala si cat timp nu am atins maximul
                stare.j_curent = joc.JMIN
                start_time = time.time()
                stare.executa_miscare()
                print("-----% s Seconds-----" % (time.time() - start_time))

                stare.j_curent = joc.JMAX
                start_time = time.time()

                stare = min_max(stare).stare_aleasa
                print("-----% s Seconds-----" % (time.time() - start_time))

                # print("Miscarea:" + str(stare.stare_aleasa.tabla_joc.MISCARE))
                print(stare.tabla_joc)

        if algortim == "alpha-beta":
            sem = True
            sem3 = False
            while sem3 == False:

                """Jucatorul va fi cu negre(jmin) iar calculatorul va fi cu albe(jmax)"""
                print("Care sa fie nivelul de dificultate?: \n-usor\n-mediu\n-greu")
                dif = input()
                if dif == "usor":
                    stare.ADANCIME_MAX = 2
                    sem3 = True
                if dif == "mediu":
                    stare.ADANCIME_MAX = 4
                    sem3 = True
                if dif == "greu":
                    stare.ADANCIME_MAX = 8
                    sem3 = True
            print("The Game is on : \n")
            print(joc)
            while stare.tabla_joc.final() == False or stare.ADANCIME_MAX != 0:
                print("Continuati?(yes/no)")
                if (input() == "no"):
                    if stare.scor > 0:
                        print("Castigator: Jucatorul")
                    else:
                        if stare.scor < 0:
                            print("Castigator: Calculatorul")
                        else:
                            print("EGALITATE")

                    break
                # cat timp nu sunt intr-o stare finala si cat timp nu am atins maximul
                stare.j_curent = joc.JMIN
                start_time = time.time()
                stare.executa_miscare()
                print("-----% s Seconds-----" % (time.time() - start_time))

                stare.j_curent = joc.JMAX
                start_time = time.time()

                stare = alpha_beta(float('-inf'), float('+inf'), stare).stare_aleasa
                print("-----% s Seconds-----" % (time.time() - start_time))

                # print("Miscarea:" + str(stare.stare_aleasa.tabla_joc.MISCARE))
                print(stare.tabla_joc)
