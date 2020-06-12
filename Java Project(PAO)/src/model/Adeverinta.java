package model;

import java.util.Calendar;

public class Adeverinta {
   Student stud;
   Calendar data;
   Secretar secr;
   public boolean valida;
   String feedBack;

    public boolean isValida() {
        return valida;
    }

    public String getFeedBack() {
        return feedBack;
    }

    public void setFeedBack(String feedBack) {
        this.feedBack = feedBack;
    }

    public Adeverinta(Student stud, Calendar data, Secretar secr) {
        this.stud = stud;
        this.data = data;
        this.secr = secr;
    }

    public Adeverinta() {
    }

    public void setValida(boolean valida) {
        this.valida = valida;
    }

    public Student getStud() {
        return stud;
    }

    public void setStud(Student stud) {
        this.stud = stud;
    }

    public Calendar getData() {
        return data;
    }

    public void setData(Calendar data) {
        this.data = data;
    }

    public Secretar getSecr() {
        return secr;
    }

    public void setSecr(Secretar secr) {
        this.secr = secr;
    }

}
