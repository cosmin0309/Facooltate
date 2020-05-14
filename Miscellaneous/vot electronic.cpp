#include <iostream>
#include <fstream>
#include <string.h>
#include <ctime>

using namespace std;
struct candidat
{
    char nume[100];
    float nr_voturi;
};
ifstream f("evidenta.csv");
int incercari_frauda;
candidat candidati[100];
int nr_candidati, nr_cnp;
char nume[100][100], cnp[100][100], adresa[100][100], serie_nr_ci[100][100], cnp_adaugat[100][100];
int i;
float nr_total_voturi;
void parcurgere()
{
    while(!f.eof())
    {
        i++;
        char linie[200];
        f.getline(linie, 200);
        char *p = strtok(linie, ",");
        int choice = 1;
        while(p!=NULL)
        {
            switch(choice)
            {
            case 1:
                strcpy(nume[i], p);
                break;
            case 2:
                strcpy(adresa[i], p);
                break;
            case 3:
                strcpy(cnp[i], p);
                break;
            case 4:
                strcpy(serie_nr_ci[i], p);
                break;

            }
            choice++;
            p = strtok(NULL, ",");
        }
    }

}
int gasesc_cnp(char cnpp[])
{
    for(int j = 1; j <= i; j++)
    {
        if(strcmp(cnp[j], cnpp) == 0)
            return j;
    }
    return 0;

}
void add_cnp(char cnpp[])
{
    strcpy(cnp_adaugat[++nr_cnp], cnpp);
}
int votat_deja(char cnpp[])
{
    for(int j = 1; j <= i; j++)
    {
        if(strcmp(cnp_adaugat[j], cnpp) == 0)
            return j;
    }
    return 0;

}
int minora(char cnpp[])
{
    time_t now = time(NULL);
    struct tm * currentDate = localtime(&now);
    if(cnpp[0]!='5'&&cnpp[0]!='6'){
    int an = (cnpp[1]-'0')*10+cnpp[2]-'0';
    int luna = (cnpp[3]-'0')*10+cnpp[4]-'0';
    if(currentDate->tm_year - an > 18)
    {
        return 1;
    }
    if(currentDate->tm_year - an == 18&&currentDate->tm_mon + 1 - luna>=0)
    {
        return 1;
    }
    return 0;
    }
    else
    {
        int an = (cnpp[1]-'0')*10+cnpp[2]-'0';
        int luna = (cnpp[3]-'0')*10+cnpp[4]-'0';
    if(currentDate->tm_year - an-100 > 18)
    {
        return 1;
    }
    if(currentDate->tm_year - an == 18&&currentDate->tm_mon + 1 - luna>=0)
    {
        return 1;
    }
    return 0;
    }

}
int gasesc_candidat(candidat c)
{
    for(int j = 1; j <= nr_candidati; j++)
        if(strcmp(c.nume, candidati[j].nume) == 0){
            candidati[j].nr_voturi++;
            return j;
        }
    return 0;
}
void add_candidat(candidat c)
{
    strcpy(candidati[++nr_candidati].nume, c.nume);
    candidati[nr_candidati].nr_voturi = 1;
}

void add()
{
    candidat c;
    char cnpp[100];
    cin.get(cnpp, 100);
    cin.get();
    cin.get(c.nume, 100);
    cin.get();
    if(votat_deja(cnpp)!=0)
    {
        cout<<"\nVot deja inregistrat\n";
        incercari_frauda++;
        return;
    }

    if(gasesc_cnp(cnpp)==0)
    {
        cout<<"\nCNP invalid\n";
        incercari_frauda++;
        return;
    }
    if(minora(cnpp) == 0)
    {
        cout<<"\nPersoana minora\n";
        return;
    }
    if(gasesc_candidat(c)!= 0)
    {
        nr_total_voturi++;
    }
    else
    {
        add_candidat(c);
        nr_total_voturi++;
    }
    add_cnp(cnpp);
}
void sorteaza()
{
    int sem;
    do
    {
     //   cout<<"crap";
        sem = 1;
        for(int j = 1; j <= nr_candidati-1; j++)
            if(candidati[j].nr_voturi < candidati[j+1].nr_voturi)
            {
                //cout<<"\nCompar "<<candidati[j].nume<<" cu "<<candidati[j+1].nume<<"\n";
                candidat temp;
                temp = candidati[j];
                candidati[j] = candidati[j+1];
                candidati[j+1] = temp;
                sem = 0;
            }
    }
    while(sem == 0);
}
void statistica()
{
    cout<<"Statistici\n==========\n";
    if(nr_candidati!=0)
    {
        sorteaza();
        for(int j = 1; j <= nr_candidati; j++)
        {
            float procent;
            procent =( float)((candidati[j].nr_voturi*100)/nr_total_voturi);
            cout<<candidati[j].nume<<": "<<candidati[j].nr_voturi<<" voturi ("<<(float)(procent)<<"%)"<<'\n';
        }
    }
    cout<<"Incercari de frauda : "<<incercari_frauda<<'\n';
}

void incheie()
{
    statistica();
}

int main()
{

    char choice;
    parcurgere();
    do
    {
        cin>>choice;
        cin.get();
        switch(choice)
        {
        case '+':
            add();
            break;
        case '?':
            statistica();
            break;
        case '*':
            incheie();
            break;
        }
    }
    while(choice!='*');

}
