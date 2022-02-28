package com.company;

public class SecondaProva {
    private String nome;
    private int popolazione;
    private double tassoCrescita;

    public void setSpercie (String nome, int popolazione, double tassoCrescita) {
        this.nome = nome;
        if (popolazione >=0) {
            this.popolazione = popolazione;
        }
        else {
            System.out.println("ERRORE: si sta usando un numero negativo " + popolazione);
            System.exit(0);
        }
        this.tassoCrescita = tassoCrescita;
    }

    public String getNome() {
        return nome;
    }

    public int getPopolazione() {
        return popolazione;
    }

    public double getTassoCrescita() {
        return tassoCrescita;
    }
}
