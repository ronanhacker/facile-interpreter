// Parser.java
//
// ICS 22 / CSE 22 Fall 2012
// Project #3: What's Simple Is True
//
// The Parser class implements one static method that reads the contents of
// an input file, which is assumed to contain a syntactically legal Facile
// program, and returns an ArrayList of Statement objects of the appropriate
// types.  I've provided some code to get you started.

import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;



public class Parser
{
	// parseProgram() takes a filename as a parameter, opens and reads the
	// contents of the file, and returns an ArrayList of Statement objects.
	// If the file does not exist, an IOException should be thrown.
	public static ArrayList<Statement> parseProgram(String filename)
	throws IOException
	{

	}


	// parseLine() takes a line from the input file and returns a Statement
	// object of the appropriate type.  This will be a handy method to call
	// within your parseProgram() method.
	private static Statement parseLine(String line)
	{
		// Scanners can be used to break Strings into pieces, too!
		Scanner scanner = new Scanner(line);
		
		// The next() method returns the next word out of the String.  We'll
		// use the first word to decide on a statement type.
		String statementType = scanner.next();
		
		Statement statement = null;
		
		if (statementType.equals("LET"))
		{
			char variable = scanner.next().charAt(0);
			int value = scanner.nextInt();

			statement = new LetStatement(variable, value);
		}
		else if (statementType.equals("PRINT"))
		{
			// ...
		}
		
		// You'll need to add more "else if"s above for the other kinds of
		// statements.

		// Once you've created the appropriate kind of statement, it can be
		// returned.
		return statement;
	}
}
