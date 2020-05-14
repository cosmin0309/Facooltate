#include <iostream>
#include <string.h>
using namespace std;
class Oven
{
    char functii[8][15];
    bool are[7];
public:
    Oven()
    {
        strcpy(functii[1],"microwave");
        strcpy(functii[2], "convection");
        strcpy(functii[3], "ventilator");
        strcpy(functii[4], "grill");
        strcpy(functii[5], "crisp");
        strcpy(functii[6], "rotisserie");
        strcpy(functii[7], "steam");
        for(int i = 1; i<= 7; i++)
            are[i] = false;
    }
    void set_are(char *functie)
    {
        for(int i = 1; i <= 7; i++)
            if(strcmp(functii[i], functie) == 0)
                are[i] = true;
    }
    char * get_functii(int i)
    {
        return functii[i];
    }
    bool get_are(int i)
    {
        return are[i];
    }
};
class P0001M:public Oven
{
    char model[9];
public:
    P0001M()
    {
        strcpy(model, "P0001M");
        set_are("microwave");
    }
};

class P0001MG : public P0001M
{
    char model[9];
public:
    P0001MG()
    {
        strcpy(model, "P0001MG");
        P0001M();
        set_are("grill");
    }
};

class P0002M : public Oven
{
    char model[9];
public:
    P0002M()
    {
        strcpy(model, "P0002M");
        set_are("microwave");
        set_are("grill");
        set_are("ventilator");
    }
};

class P0003 : public Oven
{
    char model[9];
public:
    P0003()
    {
        strcpy(model, "P0003");
        set_are("microwave");
        set_are("grill");
        set_are("ventilator");
        set_are("steam");
    }
};

class P0004 : public Oven
{
    char model[9];
public:
    P0004()
    {
        strcpy(model, "P0004");
        set_are("grill");
        set_are("crisp");
        set_are("rotisserie");
    }
};

class P0004M : public P0004
{
    char model[9];
public:
    P0004M()
    {
        strcpy(model, "P0004M");
        P0004();
        set_are("microwave");
    }
};

class P0003X : public P0003
{
    char model[9];

public:
    P0003X()
    {
        strcpy(model, "P0003X");
        P0003();
        set_are("convection");
        set_are("ventilator");
    }
};

class P00034X : public P0003, P0004
{
    char model[9];
public:
    P00034X()
    {
        strcpy(model, "P00034X");
        P0003();
        P0004();
        P0003::set_are("convection");
    }
};
class Subsisteme
{
    char lipsa[100];
    int nr_reteta;
public:
    Subsisteme()
    {
        //     nr_reteta = n;
        strcpy(lipsa," ");
    }
    void set_nr_reteta(int n)
    {
        this->nr_reteta = n;
    }
    char *get_lipsa(){
        return this->lipsa;
    }
    int get_nr_reteta()
    {
        return this->nr_reteta;
    }
    void add_lipsa(char *to_add)
    {
        //cout<<"\nAdaug "<<to_add<<"\n";
        if(strlen(this->lipsa) > 2)
            strcat(this->lipsa, " ");
        strcat(this->lipsa,to_add );
    }
    bool nu_este_in_lista(char *s)
    {
        if(strstr(this->lipsa, s) == 0)
            return true;
        return false;
    }
    void sortt(){
        char cs[strlen(this->lipsa)];
        strcpy(cs, this->lipsa);
        char cuvinte[20][20];
        char *pch;
        pch = strtok(cs, " ");
        int i = 0;
        while(pch != NULL){
           // cout<<pch<<endl;
            strcpy(cuvinte[i++], pch);
            pch = strtok(NULL, " ");
        }
        bool sorted;
        //cout<<"\nNot SORTED\n";
        //for(int j = 0 ; j < i; j++)
         //   cout<<cuvinte[j]<<endl;

        do{
            sorted = true;
            for(int j = 0; j < i-1; j++)
            if(strcmp(cuvinte[j], cuvinte[j+1]) > 0){
                char x[15];
                strcpy(x, cuvinte[j]);
                strcpy(cuvinte[j], cuvinte[j+1]);
                strcpy(cuvinte[j+1], x);
                sorted = false;
            }
        }while(sorted == false);
       // cout<<"\nSORTED\n";
        //for(int j = 0 ; j < i; j++)
          //  cout<<cuvinte[j]<<endl;
        strcpy(this->lipsa, cuvinte[0]);
        for(int j = 1; j < i; j++){
            strcat(this->lipsa, " ");
            strcat(this->lipsa, cuvinte[j]);
        }
    }
};
class My_Oven
{
    char model[15];
    int n;
    Subsisteme subst_lipsa[100];
    char subsisteme[100];
public:
    void set_My_Oven()
    {
        strcpy(subsisteme," ");
        cin>>model;
        cin>>n;
    }
    Subsisteme get_subsisteme(int i){
        return subst_lipsa[i];
    }
    char *get_subsisteme(){
        return this->subsisteme;
    }
    int get_n()
    {
        return n;
    }
    int cin_reteta(int indice)
    {
        /*  if(strcmp(model, "P0001MG"))
          {
              P0001MG my_oven;
          }
          if(strcmp(model, "P0002M"))
          {
              P0002M my_oven;
          }
          if(strcmp(model, "P0003"))
          {
              P0003 my_oven;
          }
          if(strcmp(model, "P0004"))
          {
              P0004 my_oven;
          }
          if(strcmp(model, "P0004M"))
          {
              P0004M my_oven;
          }
          if(strcmp(model, "P0003X"))
          {
              P0003X my_oven;
          }
          if(strcmp(model, "P00034X"))
          {
              P00034X my_oven;
          }
        */
        unsigned int nr_randuri;
        //  cout<<"\nNumarul de randuri: ";
        cin>>nr_randuri;
        bool se_poate = true;
        cin.get();
        for(int i = 1; i <= nr_randuri; i++)
        {
            char reteta[50];
            //   cout<<"\nRandul "<<i<<" : ";
            cin.getline(reteta, 50, '\n');
            char functie[10];
            int nr_randuri2;
            if(strchr(reteta, '['))
            {
                int poz1 = strchr(reteta, '[') - reteta;
                int poz2 = strchr(reteta, ']') - reteta;
                int k = 0;
                int j;
                //   cout<<"###"<<nr_randuri<<"###\n";

                for( j = poz1+1; j < poz2; j++)
                {
                    //  cout<<"###"<<nr_randuri<<"###\n";

                    functie[k++] = reteta[j];
                }
                nr_randuri2 = nr_randuri;

                //  cout<<"###"<<nr_randuri<<"###\n";

                functie[k] = '\0';
                strcat(subsisteme, " ");
                strcat(subsisteme, functie);
                // cout<<"###"<<nr_randuri<<"###\n";

                if(strcmp(model, "P0001M")==0)
                {
                    P0001M my_oven;
                    for(int ii = 1; ii <= 7; ii++)
                        if(strcmp(my_oven.get_functii(ii), functie) == 0 && my_oven.get_are(ii) != true)
                        {
                            subst_lipsa[indice].set_nr_reteta(indice);
                            if(subst_lipsa[indice].nu_este_in_lista(functie))
                                subst_lipsa[indice].add_lipsa(functie);
                            se_poate = false;
                            // cout<<"aici1";
                        }
                }
                if(strcmp(model, "P0001MG")==0)
                {
                    P0001MG  my_oven;
                    for(int ii = 1; ii <= 7; ii++)
                        if(strcmp(my_oven.get_functii(ii), functie) == 0 && my_oven.get_are(ii) != true)
                        {
                            subst_lipsa[indice].set_nr_reteta(indice);
                            if(subst_lipsa[indice].nu_este_in_lista(functie))
                                subst_lipsa[indice].add_lipsa(functie);

                            se_poate = false;
                            //   cout<<"aici2";
                        }
                }
                if(strcmp(model, "P0002M")==0)
                {
                    P0002M my_oven;
                    for(int ii = 1; ii <= 7; ii++)
                        if(strcmp(my_oven.get_functii(ii), functie) == 0 && my_oven.get_are(ii) != true)
                        {
                            subst_lipsa[indice].set_nr_reteta(indice);
                            if(subst_lipsa[indice].nu_este_in_lista(functie))
                                subst_lipsa[indice].add_lipsa(functie);

                            se_poate = false;
                            //  cout<<"aici2";
                        }
                }
                if(strcmp(model, "P0003")==0)
                {
                    P0003 my_oven;
                    for(int ii = 1; ii <= 7; ii++)
                        if(strcmp(my_oven.get_functii(ii), functie) == 0 && my_oven.get_are(ii) != true)
                        {
                            subst_lipsa[indice].set_nr_reteta(indice);
                            if(subst_lipsa[indice].nu_este_in_lista(functie))
                                subst_lipsa[indice].add_lipsa(functie);

                            //cout<<"aici2.2";
                            se_poate = false;
                        }
                }
                if(strcmp(model, "P0004")==0)
                {
                    P0004 my_oven;
                    for(int ii = 1; ii <= 7; ii++)
                        if(strcmp(my_oven.get_functii(ii), functie) == 0 && my_oven.get_are(ii) != true)
                        {
                            subst_lipsa[indice].set_nr_reteta(indice);
                            if(subst_lipsa[indice].nu_este_in_lista(functie))
                                subst_lipsa[indice].add_lipsa(functie);

                            se_poate = false;
                            //  cout<<"aici3";
                        }
                }

                if(strcmp(model, "P0004M")==0)
                {

                    P0004M my_oven;
                    for(int ii = 1; ii <= 7; ii++)
                    {

                        if(strcmp(my_oven.get_functii(ii), functie) == 0 && my_oven.get_are(ii) != true)
                        {
                            subst_lipsa[indice].set_nr_reteta(indice);
                            if(subst_lipsa[indice].nu_este_in_lista(functie))
                                subst_lipsa[indice].add_lipsa(functie);

                            se_poate = false;
                            // cout<<"\nNu se poate ptc nu exista "<<functie<<" in cuptor\n";
                        }
                    }
                }
                if(strcmp(model, "P0003X")==0)
                {
                    P0003X my_oven;
                    for(int ii = 1; ii <= 7; ii++)
                        if(strcmp(my_oven.get_functii(ii), functie) == 0 && my_oven.get_are(ii) != true)
                        {
                            subst_lipsa[indice].set_nr_reteta(indice);
                            if(subst_lipsa[indice].nu_este_in_lista(functie))
                                subst_lipsa[indice].add_lipsa(functie);

                            //cout<<"aici4";
                            se_poate = false;
                        }
                }
                if(strcmp(model, "P00034X")==0)
                {
                    P00034X my_oven;
                    for(int ii = 1; ii <= 7; ii++)
                        if(strcmp(my_oven.P0003::get_functii(ii), functie) == 0 && my_oven.P0003::get_are(ii) != true)
                        {
                            subst_lipsa[indice].set_nr_reteta(indice);
                            if(subst_lipsa[indice].nu_este_in_lista(functie))
                                subst_lipsa[indice].add_lipsa(functie);

                            se_poate = false;
                            //  cout<<"aici5";
                        }

                }
            }
            // cout<<"\nurmeaza "<<i+1<<" care e <= "<<nr_randuri;
            nr_randuri = nr_randuri2;
        }
        this->subst_lipsa[indice].sortt();

        //  cout<<"am iesit si n am trecut prin i";
        if(se_poate == true)
        {
            //  cout<<"Se poate";
            return 1;

        }
        else
        {
            //cout<<"Nu se poate";
            return 0;
        }
    }
    void retete_folosite(){
         char cs[strlen(this->subsisteme)];
        strcpy(cs, this->subsisteme);
        char cuvinte[20][20];
        char *pch;
        pch = strtok(cs, " ");
        int i = 0;
        while(pch != NULL){
           // cout<<pch<<endl;
            strcpy(cuvinte[i++], pch);
            pch = strtok(NULL, " ");
        }
        bool sorted;
        //cout<<"\nNot SORTED\n";
        //for(int j = 0 ; j < i; j++)
         //   cout<<cuvinte[j]<<endl;

        do{
            sorted = true;
            for(int j = 0; j < i-1; j++)
            if(strcmp(cuvinte[j], cuvinte[j+1]) > 0){
                char x[15];
                strcpy(x, cuvinte[j]);
                strcpy(cuvinte[j], cuvinte[j+1]);
                strcpy(cuvinte[j+1], x);
                sorted = false;
            }
        }while(sorted == false);
        cout<<"\nSORTED\n";
        int counter = 1;
        for(int j = 0 ; j <= i-1; j++){

            if(strcmp(cuvinte[j], cuvinte[j+1]) == 0){
               counter++;
            }
            else{
            cout<<cuvinte[j]<<" "<<counter<<endl;
            counter = 1;
            }
        }
       /* strcpy(this->lipsa, cuvinte[0]);
        for(int j = 1; j < i; j++){
            strcat(this->lipsa, " ");
            strcat(this->lipsa, cuvinte[j]);
        }
    }*/

}
};
int main()
{
    My_Oven ovi;
    ovi.set_My_Oven();
    int s = 0;
    for(int i = 1 ; i <= ovi.get_n(); i++)
        s+=ovi.cin_reteta(i);
    char x;
    cin>>x;
    if(x=='a')
        cout<<s;
    if(x == 'b'){
        for(int i = 0; i <= ovi.get_n(); i++){
            if(strlen(ovi.get_subsisteme(i).get_lipsa()) > 2){
                cout<<ovi.get_subsisteme(i).get_nr_reteta()<<": ";
                    cout<<ovi.get_subsisteme(i).get_lipsa()<<" ";
                cout<<endl;
            }
    }
    }
    if(x == 'c'){
        ovi.retete_folosite();
       // cout<<ovi.get_subsisteme();
    }

}
