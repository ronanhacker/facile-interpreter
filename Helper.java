public class Helper {
    
    public static enum Type{
        INT,
        UNINITIALIZED
    }

    public static void error(){
        System.out.println("ERROR.");
        System.exit(-1);
    }

    public static boolean stringIsInt(String s){
        try{
            int y = Integer.parseInt(s);
            return true;
        }  catch(NumberFormatException e){
            return false;
        }
    }

    public static int getLetter(String s) {
        if(s.length() != 1 ) Helper.error();
        char c = s.toCharArray()[0];
        return c - 'A';
    }
    

}
