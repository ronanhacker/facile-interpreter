import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class Facile {

    public static boolean stringIsInt(String s){
        try{
            int y = Integer.parseInt(s);
            return true;
        }  catch(NumberFormatException e){
            return false;
        }
    }

    public static int getLetter(String s) {
        if(s.length() != 1 ) error();
        char c = s.toCharArray()[0];
        return c - 'A' + 1;
    }

    enum Type{
        STRING,
        INT,
        UNINITIALIZED
    }

    public class Variable {
        String val_string;
        int val_int;

        Type type;

        public Variable() {
           type = Type.UNINITIALIZED;
        }

        public String getString(){
            if(type != Type.STRING) error();
            return val_string;
        }
        
        public int getInt(){
            if(type != Type.INT) error();
            return val_int;
        }
        
        public void set(String x){
            if(stringIsInt(x))
            {
                type = Type.INT;
                val_int = Integer.parseInt(x);
            }
            else {
                type = Type.STRING;
                val_string = x;
            }
        }
    }
    

    public static void main(String[] args) {
        File input = new File(args[0]);
        ArrayList<String> code = new ArrayList<>();
        try(Scanner s = new Scanner(input)){
            while(s.hasNextLine()){
                code.add(s.nextLine());
            }
            Variable[] variables = new Variable[26];
            for(int i = 0; i < 26; i++){
                variables[i] = new Variable();
            }
            interpret(code, variables, 0);
            error();
        } catch(FileNotFoundException e){
            System.out.println("Error.");
        }
    }

    static void interpret(ArrayList<String> lines, Variable[] variables, int startline){
        for(int i = startline; i < lines.size(); i++){

            if(lines.get(i).toUpperCase() != lines.get(i)) error();

            String[] args = lines.get(i).split(" ");

            if(args.length == 0) error();
            
            for(String arg: args){
                System.out.print(arg);
            }
            
            Variable v1;
            Variable v2;
            
            switch(args[0].toUpperCase()){
                case "LET":
                    if (args.length != 3) {
                        error();
                    }
                    variables[getLetter(args[1])].set(args[2]);
                    break;
                case "PRINT":
                    if (args.length != 2) {
                        error();
                    }
                    v1 = variables[getLetter(args[1])];
                    if (v1.type == Type.STRING) {
                        System.out.println(v1.val_string);
                    }
                    else if (v1.type == Type.INT) {
                        System.out.println(v1.val_int);
                    }
                    else if (v1.type == Type.UNINITIALIZED) {
                        error();
                    }
                    break;
                case "ADD":
                    if (args.length != 3) {
                        error();
                    }

                    v1 = variables[getLetter(args[1])];
                    
                    if(stringIsInt(args[2])){
                        v1.set(Integer.toString(v1.getInt() + Integer.parseInt(args[2])));
                    }
                    else{
                        v2 = variables[getLetter(args[2])];
                        v1.set(Integer.toString(v1.getInt() + v2.getInt()));
                    }
                    break;
                case "SUB":
                    if(stringIsInt(args[2])){
                        v1.set(Integer.toString(v1.getInt() + Integer.parseInt(args[2])));
                    }
                    else{
                        v2 = variables[getLetter(args[2])];
                        v1.set(Integer.toString(v1.getInt() + v2.getInt()));
                    }
                    if (args.length != 3) {
                        error();
                    }
                    Variable sub_v1 = variables[getLetter(args[1])];
                    Variable sub_v2 = variables[getLetter(args[2])];
                    
                    break;
                case "MULT":
                    break;
                case "DIV":
                    break;
                case "GOTO":
                    i = Integer.parseInt(args[1]);
                    break;
                case "IF":
                    break;
                case "GOSUB":
                    if(args.length != 2) error();
                    interpret(lines, variables, Integer.parseInt(args[1]));
                    break;
                case "RETURN":
                    return;
                case "END":
                case ".":
                    System.exit(0);
                    break;
                default:
                    error();
                    break;              
            }
            System.out.println("");
        }
    }
}

static void error(){
    System.out.println("ERROR.");
    System.exit(-1);
}