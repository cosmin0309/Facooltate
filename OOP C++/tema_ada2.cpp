/*În noua aplicație web pe care ați dezvoltat-o este necesară introducerea unor elemente suplimentare de securitate. Pentru asta veți dezvolta o bibliotecă de Password Policies. Aceste politici de parolă sunt configurate de fiecare client care folosește biblioteca voastră și apoi fiecare parola setată de utilizatori este verificată contra acestor reguli. Ele sunt:
Length - restricția poate specifica lungimea minimă sau lungimea minimă și maximă a unei parole.
Class - restricția spune câte clase diferite de caractere trebuie să aibă minim parola; clasele sunt: literă mică, literă mare, cifră și alte caractere
Must Include - parola trebuie obligatoriu să includă cel puțin un caracter din clasa specificată.
Must Not Include - parola trebuie obligatoriu să NU includă niciun caracter din clasa respectivă.
Repetition - restricția impune de câte ori se poate repeta consecutiv același caracter în parolă
Consecutive - restricția impune un număr maxim de caractere consecutive (ex: abc sau 123)
Cerință
Dându-se un set de politici de parolă sigură și apoi o listă de parole, să se afișeze pentru fiecare din ele OK sau NOK, în funcție de respectarea sau nu a tuturor acestor politici.

Date de intrare
Pe prima linie se află un număr întreg pozitiv n, necunoscut de mare, reprezentând numărul de reguli care trebuie respectate. Pe următoarele n linii se află definiția unei reguli, în următoarele formate posibile:

length <min_length> - parola trebuie să aibă min_length caractere (inclusiv); 0 < min_length
length <min_length> <max_length> - parola trebuie să aibă între min_length și max_length caractere (inclusiv); 0 < min_length <= max_length
class <min_class_count> - parola trebuie să aibă minim min_class_count tipuri de caractere diferite (literă mică, literă mare, cifră și alte caractere); 0 < min_class_count < 5
include <class> - parola trebuie obligatoriu să includă cel puțin un caracter din clasa specificată; class poate fi a, A, 0 sau $, caractere ce denotă clasa dorită
ninclude <class> - parola trebuie obligatoriu să nu includă niciun caracter din clasa specificată; class urmează aceleași reguli de mai sus
repetition <max_count> - același caracter se poate repeta pe poziții consecutive de maxim max_count ori; 0 < max_count
consecutive <max_count> - parola poate avea max_count caractere consecutive în secvență; 0 < max_count
Pe următoarele linii, până la EOF, se află câte o parolă pe linie, ce vor fi verificate cu regulile specificate.

Date de ieșire
Pentru fiecare parolă verificată, se va afișa OK dacă parola respectă TOATE regulile specificate, sau NOK dacă există măcar o regulă care nu este respectată.
*/
#include <iostream>
#include <string.h>

using namespace std;
struct length{
    int min, max;

};

class Password{
    /*length lungime;
    int class_count;
    string must_include;
    string must_not_include;
    int repetition;
    int consecutive;*/
    string parola;

public:
    void set_parola(string parola){
        this->parola = parola;
    }
    bool respecta_must_include(string must_include_dat){
            bool sem = false;
            int i;
            if(must_include_dat.find('a')){
                for(i = 0; i <= this->parola.length()-1; i++)
                    if(this->parola[i] >= 'a' && this->parola[i] <= 'z'){
                        sem = true;
                        break;
                    }
                if(i == this->parola.length() + 1)
                    return false;
            }
            if(must_include_dat.find('A')){
                for(i = 0; i <= this->parola.length()-1; i++)
                    if(this->parola[i] >= 'A' && this->parola[i] <= 'z'){
                        sem = true;
                        break;
                    }
                if(i == this->parola.length())
                    return false;
            }
            if(must_include_dat.find('0')){
                for(i = 0; i <= this->parola.length()-1; i++)
                    if(this->parola[i] >= '0' && this->parola[i] <= '9'){
                        sem = true;
                        break;
                    }
                if(i == this->parola.length())
                    return false;
            }
            if(must_include_dat.find('$')){
                for(i = 0; i <= this->parola.length() - 1; i++)
                    if(!(this->parola[i] >= '0' && this->parola[i] <= '9')&&
                    !(this->parola[i] >= 'A' && this->parola[i] <= 'z')&&
                    !(this->parola[i] >= 'a' && this->parola[i] <= 'z')){
                        sem = true;
                        break;
                    }
                if(i == this->parola.length())
                    return false;
            }    
            return sem;

    }
    bool respecta_must_not_include(string must_not_include_dat){
            return !respecta_must_include(must_not_include_dat);
    }
    bool respecta_repetitia(int repetition_dat){
            for(int i = 0; i < this->parola.length()-repetition_dat; i++){
                int k;
                for(k = i+1; k < repetition_dat; k++)
                    if(parola[i] != parola[k])
                        break;
                if(k == repetition_dat)
                    return false;
            }
            return true;
    }

    bool respecta_consecutive(int consecutive_dat){
            for(int i = 0; i <= this->parola.length()-1; i+=consecutive_dat){
                int k;
                for(k = i; k < i+consecutive_dat; k++)
                    if(parola[k] - parola[k+1] != -1)
                        break;
                if(k == i+consecutive_dat)
                    return false;
            }
            return true;
    }

    bool respecta_class_count(int class_count_dat, string must_include_dat){
        if(must_include_dat.length() < class_count_dat)
            return false;
        return true;
    }
    bool verify(length lungime_dat,
                string must_include_dat,string must_not_include_dat,
                int repetition_dat, int consecutive_dat, int class_count_dat){
                    cout<<"verific "<<parola;
                    if(!(this->parola.length() > lungime_dat.min || this->parola.length() < lungime_dat.max ||
                        this->respecta_must_include(must_include_dat)||
                        this->respecta_must_not_include(must_not_include_dat)||
                        this->respecta_repetitia(repetition_dat)||
                        this->respecta_consecutive(consecutive_dat)||
                        this->respecta_class_count(class_count_dat, must_include_dat)))
                            return true;
                        else
                            return false;
    }

};
int main(){
    Password parola;
    int n;
    cin>>n;
    length lungime_dat;
    lungime_dat.min = -1;
    lungime_dat.max = 9999;
    string must_include_dat ="";
    string must_not_include_dat ="";
    int repetition_dat = 999;
    int consecutive_dat = 999;
    int class_count_dat = 999;
    string deCitit;
    int i = 0;
    while(i < n){
        cin>>deCitit;
        //cout<<deCitit<<endl;
        if(deCitit.find("length")){
            cin>>lungime_dat.min;
            cin>>deCitit;
            cout<<deCitit<<endl;
            if(deCitit.length() == 1)
                lungime_dat.min = deCitit;
            i++;
            cin>>deCitit;
            cout<<deCitit<<endl;
        }
        if(deCitit.find("class")){
            cin>>class_count_dat;
            i++;
            cin>>deCitit;
            cout<<deCitit<<endl;
        }
        if(deCitit.find("include")){
            cin>>must_include_dat;
            i++;
            cin>>deCitit;
        }
        if(deCitit.find("ninclude")){
               cin>> must_not_include_dat;
               i++;
               cin>>deCitit;
        }
        if(deCitit.find("repetition")){
           cin>> repetition_dat;
           i++;
           cin>>deCitit;
        }
        
        if(deCitit.find("consecutive")){
           cin>> consecutive_dat;
        }
    }
    string pass;
    i = 0;
    while(i++<n){
        cin>>pass;
        cout<<pass<<endl;
        parola.set_parola(pass);
        if(parola.verify(lungime_dat, must_include_dat, must_not_include_dat, 
                        repetition_dat, consecutive_dat,class_count_dat) == true)
                            cout<<"OK"<<endl;
            else
                cout<<"NOK"<<endl;
    }
}
