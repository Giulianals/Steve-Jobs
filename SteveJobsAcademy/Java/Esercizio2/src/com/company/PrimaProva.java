package com.company;

import java.util.Scanner;

public class PrimaProva {
    private String nome;
    private int popolazione;
    private double tassoCrescita;

    public void leggiInput() {
        Scanner tastiera = new Scanner(System.in);
        System.out.println("Qual è il nome della specie?");
        nome = tastiera.nextLine();
        System.out.println("A quanto ammonta la popolazione?");
        popolazione = tastiera.nextInt();
        System.out.println("Inserisci il tasso di crescita " + "(%crescita per anno): ");
        tassoCrescita= tastiera.nextDouble();
    }
    public void scriviOutput(){
        System.out.println("Nome = " + nome);
        System.out.println("Popolazione = " +popolazione);
        System.out.println("Tasso di crescita = " + tassoCrescita);
    }
    public int prediciPopolazione (int anni) {
        int risultato = 0;
        double totalePopolazione = popolazione;
        int contatore = anni;
        while ((contatore>0) & (totalePopolazione>0)){
            totalePopolazione= (totalePopolazione + (tassoCrescita/100) * totalePopolazione);
            contatore --;
        }
        if (totalePopolazione > 0) {
            risultato = (int) totalePopolazione;
        }
        return risultato;
    }
}
