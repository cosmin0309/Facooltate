
#include <iostream>
#include <math.h>
using namespace std;
class Complex
{
private:
    float re, im;
    friend istream &operator >>(istream&, Complex&);
    friend ostream &operator <<(ostream&, const Complex&);

public:
    friend class Vector_Complecsi;
    friend float modul(Complex X);
    Complex operator +(const Complex&) const;
    Complex operator *(const Complex&) const;
    friend class Vector_Complecsi;
};

class Vector_Complecsi
{
public:
    Complex V[100];
    int n;
public:
    /* friend ostream &operator <<(ostream&, const Vector_Complecsi&);
     friend istream &operator >>(ostream&, Vector_Complecsi&);
     */
    void citire()
    {
        cin>>n;
        for(int i=0; i<n; i++)
            cin>>V[i];
    }
    void afisare()
    {
        for(int i=0; i<n; i++)
            cout<<V[i]<<endl;

    }
    void vector_module()
    {
        float VM[100];

        cout<<"Vectorul modulelor este:\n";
        for(int i=0; i<n; i++)
            VM[i]=modul(V[i]);
        cout<<endl;
        for(int i=0; i<n; i++)
            cout<<VM[i]<<" ";
        cout<<"\nVectorul modulelor SORTAT CRESCATOR este:\n";
        int sem;
           do {
                sem=1;
                for(int i=0; i<n-1; i++)
                    for(int j=i+1; j<n; j++)
                        if(VM[i]>VM[j]){
                            sem=0;
                            swap(VM[i], VM[j]);
                        }
            }while(sem!=1);
        cout<<endl;
        for(int i=0; i<n; i++)
            cout<<VM[i]<<" ";
        cout<<endl;
    }

    Complex suma_complecsi()
    {
        Complex Suma;
        Suma.re=0;
        Suma.im=0;
        for(int i=0; i<n; i++)
            Suma=Suma+V[i];
        return Suma;
    }
    Complex produs_complecsi()
    {

        Vector_Complecsi V2;
        cout<<"Dati al doilea vector: \n";
        V2.citire();
        V2.afisare();
        Complex produs;
        produs.re=0;
        produs.im=0;
        for(int i=0; i<n; i++)
            produs=produs+V[i]*V2.V[i];
        return produs;
    }

};
istream &operator>> (istream&is, Complex &c)
{
    is>> c.re>> c.im;
    return is;
}
ostream &operator <<(ostream &os, const Complex &c)
{
    os<<c.re<<" + "<<c.im<<"i";
    return os;
}
float modul (Complex X)
{
    return sqrt(X.re*X.re+X.im*X.im);
}
Complex Complex::operator+(const Complex &operand)const
{
    Complex S;
    S.re=(*this).re+operand.re;
    S.im=(*this).im+operand.im;
    return S;
}
Complex Complex::operator*(const Complex &operand)const //in loc de complex complex puteam sa pun friend complex ca sa pot sa apelez membrii clasei complex
{
    Complex P;
    P.re=(*this).re*operand.re-(*this).im*operand.im;
    P.im=(*this).im*operand.re+(*this).re*operand.im;
    return P;
}

int main()
{
    /*
        Complex A, B;
        cin>>A>>B;
        cout<<A<<endl<<B;
        cout<<endl<<A+B<<endl<<A*B<<endl<<modul(A);

    Vector_Complecsi A;
    A.citire();
    A.afisare();
    A.vector_module();
    cout<<"\n Suma lor: "<<A.suma_complecsi();
    cout<<"\n Produsul lor: "<<A.produs_complecsi();
    */char c;
    do
    {
        cout<<"Meniu:\n";
        cout<<"Operatii pentru doua numere complexe: 1\n";
        cout<<"Operatii pentru vector de complecsi: 2\n";
        cin>>c;
        if(c=='1')
        {
            do
            {
                Complex A, B;
                cout<<endl;
                cout<<"Citirea a doua numere complexe ( partile reale si imaginare ): 1\n";
                cout<<"Afisarea a doua numere complexe: 2\n";
                cout<<"Suma a doua numere complexe: 3\n";
                cout<<"Produsul a doua numere complexe: 4\n";
                cout<<"Modulul primului numar complex: 5\n";
                cout<<"Iesire: 0\n";
                cin>>c;
                switch(c)
                {
                case'1':
                    cout<<"Dati numerele:\n";
                    cin>>A>>B;
                    break;
                case'2':
                    cout<<"Cele doua numere sunt :\n"<<A<<endl<<B<<endl;
                    break;
                case'3':
                    cout<<"Suma celor doua nr complexe este: "<<A+B<<endl;
                    break;
                case'4':
                    cout<<"Produsul celor doua numere complexe este: "<<A*B<<endl;
                    break;
                case'5':
                    cout<<"Modulul primului numar este: "<<modul(A)<<endl;
                case'0':
                    break;
                }
            }
            while(c!='0');

        }else
        {
             do
            {
                Vector_Complecsi A;
                cout<<endl;
                cout<<"Citirea unui vector de complecsi( partile reale si imaginare ): 1\n";
                cout<<"Afisarea unui vector de complecsi: 2\n";
                cout<<"Suma elementelor vectorului: 3\n";
                cout<<"Produsul scalar a doi vectori: 4\n";
                cout<<"Vectorul modulelor: 5\n";
                cout<<"Iesire: 0\n";
                cin>>c;
                switch(c)
                {
                case'1':
                    cout<<"Dati vectorul\n";
                    A.citire();
                    break;
                case'2':
                    cout<<"Vectorul este :\n";
                    A.afisare();
                    cout<<endl;
                    break;
                case'3':
                    cout<<"Suma elementelor vectorului este: "<<A.suma_complecsi()<<endl;
                    break;
                case'4':
                    cout<<"Produsul scalar al vectorilor este "<<A.produs_complecsi()<<endl;
                    break;
                case'5':
                    A.vector_module();
                case'0':
                    break;
                }
            }
            while(c!='0');
        }

    }
    while(c!='0');
}

