import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class Facile {
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
                Helper.error();
            } catch(FileNotFoundException e){
                Helper.error();
            }
        }
        
    static void interpret(ArrayList<String> lines, Variable[] variables, int startline){
        for(int i = startline; i < lines.size(); i++){

            if(lines.get(i).toUpperCase() != lines.get(i)) Helper.error();

            String[] args = lines.get(i).split(" +");
            
            if(args.length == 0) Helper.error();
            
            Variable v1;
            Variable v2;
            
            switch(args[0]){
                case "LET":
                    if (args.length != 3) {
                        Helper.error();
                    }
                    variables[Helper.getLetter(args[1])].set(args[2]);
                    break;
                case "PRINT":
                    if (args.length != 2) {
                        Helper.error();
                    }
                    v1 = variables[Helper.getLetter(args[1])];
                    if (v1.getType() == Helper.Type.STRING) {
                        System.out.println(v1.getString());
                    }
                    else if (v1.getType() == Helper.Type.INT) {
                        System.out.println(v1.getInt());
                    }
                    else if (v1.getType() == Helper.Type.UNINITIALIZED) {
                        Helper.error();
                    }
                    break;
                case "ADD":
                    if (args.length != 3) {
                        Helper.error();
                    }

                    v1 = variables[Helper.getLetter(args[1])];
                    
                    if(Helper.stringIsInt(args[2])){
                        v1.set(Integer.toString(v1.getInt() + Integer.parseInt(args[2])));
                    }
                    else{
                        v2 = variables[Helper.getLetter(args[2])];
                        v1.set(Integer.toString(v1.getInt() + v2.getInt()));
                    }
                    break;
                case "SUB":
                    if (args.length != 3) {
                        Helper.error();
                    }

                    v1 = variables[Helper.getLetter(args[1])];
                    
                    if(Helper.stringIsInt(args[2])){
                        v1.set(Integer.toString(v1.getInt() + Integer.parseInt(args[2])));
                    }
                    else{
                        v2 = variables[Helper.getLetter(args[2])];
                        v1.set(Integer.toString(v1.getInt() + v2.getInt()));
                    }
                    if (args.length != 3) {
                        Helper.error();
                    }
                
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
                    if(args.length != 2) Helper.error();
                    interpret(lines, variables, Integer.parseInt(args[1]) -1);
                    break;
                case "RETURN":
                    return;
                case "END":
                case ".":
                    System.exit(0);
                    break;
                default:
                    Helper.error();
                    break;              
            }
        }
    }
}
