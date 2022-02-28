package academy.stevejobs.cestiniuova;

import java.util.Scanner;

public class Main {

    public static final int MAX_VALUE = 20;

    public static void main(String[] args) {
        int numeroDiCestini, uovaPerCestino, totaleUova, uovaDaRimuovere;

        try (Scanner keyboard = new Scanner(System.in)) {
            System.out.println("Inserisci il numero di uova per ciascun cestino:");
            uovaPerCestino = keyboard.nextInt();

            System.out.println("Inserisci il numero di cestini:");
            numeroDiCestini = keyboard.nextInt();

            totaleUova = numeroDiCestini * uovaPerCestino;

            System.out.println("Se hai");
            System.out.println(uovaPerCestino + " uova per cestino e");
            System.out.println(numeroDiCestini + " cestini");
            System.out.println("il numero totale di uova e' " + totaleUova);

            System.out.println("Inserisci il numero di uova da rimuovere da ciascun cestino.");
            uovaDaRimuovere = keyboard.nextInt();
        }

        uovaPerCestino -= uovaDaRimuovere;
        totaleUova = numeroDiCestini * uovaPerCestino;

        System.out.println("Ora hai");
        System.out.println(uovaPerCestino + " uova per cestino e");
        System.out.println(numeroDiCestini + " cestini.");
        System.out.println("Il nuovo numero totale di uova e' " + totaleUova);

        /*double distanza = 9.9;
        System.out.println("valore in double: " + distanza);
        int punti = (int)distanza;
        System.out.println("valore in int: " + punti);
        double distanza2 = punti;
        System.out.println("valore in double dopo cast: " + distanza2);

        char simbolo = '7';
        int charToInt = (int)simbolo;

        System.out.println("valore in int dopo cast: " + charToInt);*/
    }


}