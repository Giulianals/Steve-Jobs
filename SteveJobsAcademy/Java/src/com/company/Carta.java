package com.company;
import java.util.Scanner;
    public class Carta {

        private String nome;
        private String cognome;
        private int codice;
        private int numerocarta;
        private int scadenzamese;
        private int scadenzaanno;
        private int soldiresidui;




        public void setNome(String N){ //metodo set
            this.nome=N;
        }
        public void setCognome(String C){
            this.cognome=C;
        }
        public void setsoldiresidui(int S){
            this.soldiresidui=S;
        }
        public void setcodice(int P){
            this.codice=P;
        }
        public void setscadenza(int R){
            this.scadenzamese=R;
        }
        public void setscadenzaanno(int Q){
            this.scadenzaanno=Q;
        }
        public void setnumerocarta(int num){
            this.numerocarta=num;
        }

        public String getNome() {
            return nome;
        }

        public String getCognome() {
            return cognome;
        }

        public int getNumerocarta() {
            return numerocarta;
        }

        public int getCodice() {
            return codice;
        }

        public int getScadenzaanno() {
            return scadenzaanno;
        }

        public int getScadenzamese() {
            return scadenzamese;
        }

        public int getSoldiresidui() {
            return soldiresidui;
        }
    }