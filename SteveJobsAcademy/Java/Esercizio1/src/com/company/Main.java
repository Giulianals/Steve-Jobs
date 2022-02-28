package com.company;

public class Main {

    public static void main(String[] args) {
	    Cane Balto = new Cane();
        Balto.name ="Balto";
        Balto.breed="Siberian Husky";
        Balto.age= 8;

        Balto.printOutput();

        Cane scooby = new Cane();
        scooby.name = "Scooby";
        scooby.breed= "Alano";
        scooby.age= 9;

        System.out.println(scooby.name + " è un " + scooby.breed);
        System.out.println("Ha " + scooby.age + " anni, oppure");
        int umanAge = scooby.getAgeInUmanAge(); //salviamo in una variabile
        System.out.println(umanAge + " in anni umani");

    }
}
