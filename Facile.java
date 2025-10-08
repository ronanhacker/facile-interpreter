import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;

/*
Group:
Target audience:

What unique needs did your group identify in your audience?




What choices did you make while writing your error messages to meet these needs?




Pick three error messages and add an in-line comment next to each one justifying the way you wrote it.
*/


public class Facile {
    
    static ArrayList<String> validOperators =  new ArrayList<>(Arrays.asList("=", "<>", "<", ">", "<=", ">="));
    static Variable[] variables = new Variable[26];
    public static void main(String[] args) {

            for(int i = 0; i < 26; i++){
                variables[i] = new Variable();
            }

            File input = new File(args[0]);
        
            try(Scanner s = new Scanner(input)){
                
                ArrayList<String> code = new ArrayList<>();
                while(s.hasNextLine()){
                    code.add(s.nextLine());
                }
                
                interpret(code, variables, 0);

                Helper.error();
            } catch(FileNotFoundException e){
                Helper.error();
            }
        }
        
    static void interpret(ArrayList<String> lines, Variable[] variables, int startline){
        for(int i = startline; i < lines.size(); i++){

            if(!lines.getLast().equals(".")) Helper.error();
            if(lines.get(i).toUpperCase() != lines.get(i)) Helper.error();
            String[] args = lines.get(i).split(" ");
            if(args.length == 0) Helper.error();
            
            Variable v1;
            Variable v2;
            switch(args[0]){
                case "LET":
                    if (args.length != 3) Helper.error();
                    
                    variables[Helper.getLetter(args[1])].set(args[2]);
                    break;
                case "PRINT":
                    if (args.length != 2) Helper.error();
            
                    v1 = variables[Helper.getLetter(args[1])];
                    if (v1.getType() == Helper.Type.INT) {
                        System.out.println(v1.getInt());
                    }
                    else if (v1.getType() == Helper.Type.UNINITIALIZED) {
                        Helper.error();
                    }
                    break;
                case "ADD":
                    if (args.length != 3) Helper.error();

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
                    if (args.length != 3) Helper.error();
                    
                    v1 = variables[Helper.getLetter(args[1])];
                    
                    if(Helper.stringIsInt(args[2])){
                        v1.set(Integer.toString(v1.getInt() - Integer.parseInt(args[2])));
                    }
                    else{
                        v2 = variables[Helper.getLetter(args[2])];
                        v1.set(Integer.toString(v1.getInt() - v2.getInt()));
                    }
                
                    break;
                case "MULT":
                    if (args.length != 3) Helper.error();

                    v1 = variables[Helper.getLetter(args[1])];
                    
                    if(Helper.stringIsInt(args[2])){
                        v1.set(Integer.toString(v1.getInt() * Integer.parseInt(args[2])));
                    }
                    else{
                        v2 = variables[Helper.getLetter(args[2])];
                        v1.set(Integer.toString(v1.getInt() * v2.getInt()));
                    }

                    break;
                case "DIV":
                    if (args.length != 3) Helper.error();

                    v1 = variables[Helper.getLetter(args[1])];
                    
                    if(Helper.stringIsInt(args[2])){
                        v1.set(Integer.toString(v1.getInt() / Integer.parseInt(args[2])));
                    }
                    else{
                        v2 = variables[Helper.getLetter(args[2])];
                        v1.set(Integer.toString(v1.getInt() / v2.getInt()));
                    }

                    break;
                case "GOTO":
                    if(args.length != 2) Helper.error();

                    if(Integer.parseInt(args[1]) -1 < 0 || Integer.parseInt(args[1]) >= lines.size()) Helper.error();

                    i = Integer.parseInt(args[1]) - 2;

                    break;
                case "IF":
                    if(args.length != 6) Helper.error();
                    
                    if(!args[4].equals("THEN")) Helper.error();
                
                    if(!validOperators.contains(args[2])) Helper.error();
                    
                    if(!Helper.stringIsInt(args[5])) Helper.error();

                    int toJump = Integer.parseInt(args[5]);
                    if(toJump <= 0 || toJump >= lines.size()) Helper.error();
        
                    if(Helper.stringIsInt(args[1])){
                        v1 = new Variable();
                        v1.set(args[1]);
                    }
                    else{
                        v1 = variables[Helper.getLetter(args[1])];
                    }
                    
                    if(Helper.stringIsInt(args[3])){
                        v2 = new Variable();
                        v2.set(args[3]);
                    }
                    else{
                        v2 = variables[Helper.getLetter(args[3])];
                    }

                    boolean output = false;
                    switch(args[2]){
                        case "=":
                            output = v1.getInt() == v2.getInt();
                        break;
                        case "<>":
                            output = v1.getInt() != v2.getInt();
                        break;
                        case  "<":
                            output = v1.getInt() < v2.getInt();
                        break;
                        case ">":
                            output = v1.getInt() > v2.getInt();
                        break;
                        case "<=":
                            output = v1.getInt() <= v2.getInt();
                        break; 
                        case ">=":
                            output = v1.getInt() >= v2.getInt();
                        break;
                        default:
                            Helper.error();
                        break;
                    }
                    if(output) i = toJump -2;
                    break;
                case "GOSUB":
                    if(args.length != 2) Helper.error();

                    if(Integer.parseInt(args[1]) -1 < 0 || Integer.parseInt(args[1]) >= lines.size()) Helper.error();
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
