package com.company;

public class Main {

    public static void main(String[] args) {
	    Rettangolo rettangolo = new Rettangolo();
        rettangolo.setDimensioni(10, 15);
        System.out.println("L'area del rettangolo è: " + rettangolo.getArea());
    }
}
