package com.company;

public class Cane {
    public String name;
    public String breed;
    public int age;


    public void printOutput () {
        System.out.println("Nome" + name);
        System.out.println("Razza" + breed);
        System.out.println("Anni" + age);
    }

    public int getAgeInUmanAge () {
        int umanAge = 0;
        if (age <= 2 ) {
            umanAge = age * 11;
        }
        else{
            umanAge = 22 + ((age - 2) * 5);
        }
        return umanAge;
    }



}
