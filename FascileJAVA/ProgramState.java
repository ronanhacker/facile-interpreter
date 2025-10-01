// ProgramState.java
//
// ICS 22 / CSE 22 Fall 2012
// Project #3: What's Simple Is True
//
// The ProgramState class encapsulates the state of an executing Facile
// program.  The state of a Facile program consists of three parts:
//
//    * The program counter, which specifies the line number of the
//      statement that will execute next.
//    * An array of 26 integers, holding the current values of the 26
//      variables.
//    * A stack of integers, which is used to hold return lines for GOSUB
//      statements.
//
// I've provided you a start on this class, but you'll need to add methods
// to it as you go along.  In particular, you'll need methods to access and
// modify the state; these methods will be called primarily by the various
// execute() methods in the Statement subclasses, to allow the execution of
// a statement to change the state of a program.  For example, executing a
// GOTO statement will cause the program counter to be changed.



public class ProgramState
{
	private int programCounter;
	private int[] variables;
	private Stack<Integer> stack;


	public ProgramState()
	{
		programCounter = 1;
		variables = new int[26];
		stack = new Stack<Integer>();
	}


	// You'll need to add a variety of methods here.  Rather than trying to
	// think of what you'll need to add ahead of time, add them as you find
	// that you need them.


}
