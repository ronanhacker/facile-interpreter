public class Variable{
    String val_string;
    int val_int;

    Helper.Type type;

    public Variable() {
    type = Helper.Type.UNINITIALIZED;
    }
    
    public Helper.Type getType(){
        return type;
    }

    public String getString(){
        if(type != Helper.Type.STRING) Helper.error();
        return val_string;
    }
    
    public int getInt(){
        if(type != Helper.Type.INT) Helper.error();
        return val_int;
    }
    
    public void set(String x){
        if(Helper.stringIsInt(x))
        {
            type = Helper.Type.INT;
            val_int = Integer.parseInt(x);
        }
        else {
            type = Helper.Type.STRING;
            val_string = x;
        }
    }

}