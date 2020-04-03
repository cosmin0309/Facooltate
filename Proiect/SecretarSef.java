import java.util.ArrayList;

public class SecretarSef extends Secretar {
    ArrayList<Adeverinta> adeverinteRespinse = new ArrayList<Adeverinta>();

    public SecretarSef(String numeSecretar, String anSecretar, String specializareSecretar) {
        super(numeSecretar, anSecretar, specializareSecretar);
    }

    public ArrayList<Adeverinta> getAdeverinteRespinse() {
        return adeverinteRespinse;
    }

    public void setAdeverinteRespinse(Adeverinta adeverintaRespinsa) {
        this.adeverinteRespinse.add(adeverintaRespinsa);
    }

    @Override
    public void sortAdeverinte() {
            boolean sem = true;

            do{
                sem = true;
                for(int i = 0; i<this.adeverinteRespinse.size()-1; i++)
                    if(this.adeverinteRespinse.get(i).getData().after(this.adeverinteRespinse.get(i+1).getData())){
                        Adeverinta temp = new Adeverinta();
                        temp = this.getAdeverinteRespinse().get(i);
                        this.adeverinteRespinse.set(i, this.adeverinteRespinse.get(i + 1));
                        this.adeverinteRespinse.set(i + 1, temp);
                        sem = false;
                    }

            }while (sem!=true);
        }
}
