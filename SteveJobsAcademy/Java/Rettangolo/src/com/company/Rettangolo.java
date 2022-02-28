package com.company;

public class Rettangolo {
    private  int larghezza;
    private  int altezza;


    public void setDimensioni (int larghezza, int altezza) {
        this.larghezza = larghezza;
        this.altezza = altezza;

    }

    public int getArea () {
        return larghezza * altezza;
    }
}
