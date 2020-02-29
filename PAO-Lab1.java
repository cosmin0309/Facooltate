import java.util.Scanner;

class Problema1{
    void rezolvare() {
        for (int i = 1; i <= 99; i++)
            if(i%2 == 1)
                System.out.println(i);
    }

}
class Problema2{
    void rezolvare(){
        int first;
        int second;
        System.out.println("Input Data: \n Input first integer: ");
        Scanner scanner = new Scanner(System.in);
        first = scanner.nextInt();
        System.out.println("Input second integer: ");
        second = scanner.nextInt();

        if(second > first) {
            System.out.println(first + " < " + second);
            System.out.println(first + " <= " + second);
            System.out.println(first + " != " + second);

        }
        if(second < first) {
            System.out.println(first + " > " + second);
            System.out.println(first + " >= " + second);
            System.out.println(first + " != " + second);

        }
        if(second == first) {
            System.out.println(first + " == " + second);


        }
    }
}
class Problema3{
    void rezolvare(int n){
        int suma = 0;
        for(int i = 3; i <= n; i++)
            if(i % 3 == 0 || i % 5 == 0)
                suma += i;
            System.out.print(suma);
    }
}
class Problema4{
    void rezolvare(int n){
        int factorial = 1;
        if(n == 0 || n == 1){
            System.out.println(factorial);
            return;
        }
        for(int i = 2; i <= n; i++)
            factorial *= i;
        System.out.println(factorial);
    }
}
class Problema5 {
    void rezolvare(int n){
        boolean e_prim = true;
        for(int i = 2; i <= n/2; i++)
            if(n%i == 0){
                e_prim = false;
                break;
            }
        if(e_prim == true)
            System.out.println("E prim");
        else
            System.out.println("Nu e prim");
    }
}
class Problema6{
    void rezolvare(int n){
        if(n == 1 || n == 2)
            System.out.println(1);
            else{int a = 1;
            int b = 1;
            int c = 0;
            while(n > 2) {
                    c = a + b;
                    a = b;
                    b = c;
                    n--;
                }
                System.out.println(c);
            }
    }
}
class Problema7{
    boolean isPrime(int n){
        boolean e_prim = true;
        for(int i = 2; i <= n/2; i++)
            if(n%i == 0){
                e_prim = false;
                break;
            }
        return e_prim;
    }
    void rezolvare(int n){
        for (int i = n/2; i>=0; i--)
            if(n % i == 0 && isPrime(i) == true){
                System.out.println(i);
                break;
            }
    }
}
class Scratch {
    public static void main(String[] args) {
        Problema1 p1 = new Problema1();
        //p1.rezolvare();
        Problema2 p2 = new Problema2();
        //p2.rezolvare();

        Problema3 p3 = new Problema3();
        //p3.rezolvare(30);
        Problema4 p4 = new Problema4();
        //p4.rezolvare(7);

        Problema5 p5 = new Problema5();
        //p5.rezolvare(13);

        Problema6 p6 = new Problema6();
       // p6.rezolvare(8);
        Problema7 p7 = new Problema7();
        p7.rezolvare(20);
    }
}
//1
