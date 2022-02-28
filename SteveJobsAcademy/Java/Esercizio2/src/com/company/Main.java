package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner tastiera = new Scanner(System.in);
        PrimaProva primaProva = new PrimaProva();

        System.out.println("Inserisci i dati della specie del mese: ");
        primaProva.leggiInput();
        primaProva.scriviOutput();

        System.out.println("Inserisci il numero degli anni della previsione: ");
        int anni = tastiera.nextInt();
        int popolazioneFutura = primaProva.prediciPopolazione(10);
        System.out.println("Tra 10 anni la popolazione sarà di "+ popolazioneFutura + " individui");

        //primaProva.nome = "Pantera"; se metto private nome non è più valida
        //primaProva.popolazione = 325;     non può esserci un accesso diretto con private
        //primaProva.tassoCrescita = 30;

        primaProva.scriviOutput();

    }
}
