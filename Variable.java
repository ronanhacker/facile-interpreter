public class Variable{
    int val_int;

    Helper.Type type;

    public Variable() {
    type = Helper.Type.UNINITIALIZED;
    }
    
    public Helper.Type getType(){
        return type;
    }
    
    public int getInt(){
        if(type == Helper.Type.UNINITIALIZED) Helper.error();
        return val_int;
    }
    
    public void set(String x){
        if(Helper.stringIsInt(x))
        {
            type = Helper.Type.INT;
            val_int = Integer.parseInt(x);
        }
        else {
            Helper.error();
        }
    }

}