#include <stdio.h>
#include <stdlib.h>
typedef struct
{
    int nr_crt;
    char nume_marca[20];
    int nr_masini;
    int pret;

} masina;

int nrcrt(FILE *f, int dim)
{
    /*Functie pentru a returna pozitia elementului din fisier fata de celalalte elemente*/

    int nr;
    long p = ftell(f);
    fseek(f, 0, 2);
    nr = ftell(f)/dim;
    fseek(f, p, 0);
    return nr;
}
FILE *creeaza_fisierb(char *nume_fisier)
{
    FILE *f;
    int i;
    f = fopen(nume_fisier,"wb");
    if(f == NULL)
    {
        printf("Eroare la creearea fisierului!\n");
        return NULL;
    }
    else
        printf("Am creat fisierul %s\n", nume_fisier);
    printf("\nDati numarul de obiecte ale caror informatii doriti sa le adaugati in fisier:\n");
    int nr;
    scanf("%d", &nr);
    printf("Introduceti informatiile :\n", nr);

    for(i = 1; i <= nr; i++)
    {

        masina m;
        m.nr_crt = i;
        printf("Informatiile pentru inregistrarea %d\n", m.nr_crt);
        printf("Dati numele marcii: \n");
        scanf("%s", m.nume_marca);
        printf("Dati numarul de masini disponibile: \n");
        scanf("%d", &m.nr_masini);
        printf("Dati pretul:\n");
        scanf("%d", &m.pret);
        fwrite(&m, sizeof(masina), 1, f);
    }
    fclose(f);
    return f;
}
void stergere_cheieUnica(char *nume_fisier)
{
    //Mut doar obiectele care doresc sa fie pastrate intr-un alt fisier temporar apoi le mut inapoi peste cele din fisierul original
    FILE *f;
    FILE *g;
    int cheie;
    f = fopen(nume_fisier, "rb+");
    g = fopen("masiniBinarDupaStergere.in", "wb");
    if(!f)
        printf("eroare la deschiderea fisierului binar");
    printf("Dati cheia unica din dreptul careia doriti sa stergeti inregistrarea : ");
    scanf("%d", &cheie);
    masina m;
    fread(&m, sizeof(masina), 1, f);
    do
    {
        printf("Am citit din f intrarea %d : %s %d %d\n", m.nr_crt, m.nume_marca, m.nr_masini, m.pret);
        if(m.nr_crt != cheie){
            fwrite(&m, sizeof(masina), 1, g);
        printf("Am scris in g intrarea %d : %s %d %d\n", m.nr_crt, m.nume_marca, m.nr_masini, m.pret);
        }
        fread(&m, sizeof(masina), 1, f);

    }
    while(!feof(f));

    fclose(f);
    fclose(g);
    g = fopen("masiniBinarDupaStergere.in", "rb+");
    f = fopen(nume_fisier, "wb");
    fread(&m, sizeof(masina), 1, g);
    int i=1;
    m.nr_crt=i++;
    do
    {
        printf("Am citit din g intrarea %d : %s %d %d\n", m.nr_crt, m.nume_marca, m.nr_masini, m.pret);
        fwrite(&m, sizeof(masina), 1, f);
        printf("Am scris in f intrarea %d : %s %d %d\n", m.nr_crt, m.nume_marca, m.nr_masini, m.pret);
        fread(&m, sizeof(masina), 1, g);
        m.nr_crt=i++;

    }
    while(!feof(g));


    printf("Am efectuat stergerea dupa cheia %d si am actualizat valorile cheilor pentru restul elementelor", cheie);
    fclose(f);
    fclose(g);
    remove(g);

}
void modifcare_grup_articole(char *nume_fisier)
{
    FILE *f;
    masina m;
    f = fopen(nume_fisier, "rb+");
    if(!f)
        printf("Eroare la deschiderea fisierului!");
    int nr_maxim;
    printf("\nDati numarul maxim de masini care trebuie sa fie disponibile pentru a indeplini criteriul:\n");
    scanf("%d", &nr_maxim);
    //printf("%s", nume_produs);

    fread(&m, sizeof(masina), 1, f);
    while(!feof(f))
    {
        if(m.nr_masini<nr_maxim)
        {
            printf("\n Pretul actual de masini %s este %d", m.nume_marca, m.pret );
            m.pret/=2;
            fseek(f, -sizeof(masina), 1);
            fwrite(&m, sizeof(masina), 1, f);
            printf("\nAm modificat pretul pentru %s la %d\n", m.nume_marca, m.pret);

        }
        fseek(f, 0, 1);
        fread(&m, sizeof(masina), 1, f);
    }
    fclose(f);

}
FILE *creeaza_fisiert(char *nume_fisierText, char *nume_fisierBinar)
{
    //Mut elementele din fisierul binar in cel text
    FILE *ftext;
    ftext = fopen(nume_fisierText, "w");
    if(ftext == NULL)
        printf("Eroare la deschiderea fisierului!");
    FILE *fbinar;
    fbinar = fopen(nume_fisierBinar, "rb");
    if(ftext == NULL)
        printf("Eroare la deschiderea fisierului!");
    masina m;
    fread(&m, sizeof(masina), 1, fbinar);

    int n = nrcrt(fbinar, sizeof(masina)), i;
    for(i = 1; i <= n; i++)
    {
        fprintf(ftext, "%d).%s|%d|%d\n", m.nr_crt, m.nume_marca, m.nr_masini, m.pret);
        fread(&m, sizeof(masina), 1, fbinar);

    }
    fclose(ftext);
    fclose(fbinar);
    printf("Am mutat elementele din fisierul binar in cel text.");
    return ftext;
}

int main()
{
    printf("Meniu:\n");
    FILE* fisier;
    int choice;
    FILE* fisier_text;
    char *nume_fisier = "masiniBinar.in";
    do
    {

        printf("\n\nCreati si populati un fisier binar pentru a stoca datele despre masinile aflate intr-un anumit showroom : 1\n");
        printf("\nStergeti o anumita inregistrare data de cheia unica : 2\n");
        printf("\nInjumatati pretul masinilor disponibile intr-un anumit numar maxim dat : 3\n");
        printf("\nCreati un raport care sa contina toate articolele din fisierul binar sub forma de fisier text : 4\n");
        printf("\nExit : 0\n");
        printf("\nDati comanda : \n");
        scanf("%d", &choice);
        switch(choice)
        {
        case 1:
            fisier = creeaza_fisierb(nume_fisier);
            break;
        case 2:
            stergere_cheieUnica(nume_fisier);
            break;
        case 3:
            modifcare_grup_articole(nume_fisier);
            break;
        case 4:
            fisier_text=creeaza_fisiert("masini.txt", nume_fisier);
            break;
        }
    }
    while(choice!=0);
}
