// Solution to challenge Jaden Case from Codewars

public class JadenCase
{
    public String toJadenCase(String phrase) {
		
        // If the string is null or empty return null
        if (phrase == null || phrase.isEmpty())
        {
            return null;
        }

        // Make a String builder object
        // It will be used to capitalize every new word
        StringBuilder jadenString = new StringBuilder();

        boolean titleNext = true;

        // Loop through all characters of the given string
        for (char jadenChar : phrase.toCharArray())
        {
            // If the character is a whitespace, set
            // title Next to true
            if (Character.isSpaceChar(jadenChar))
            {
                titleNext = true;
            }

            // If title next is true, convert that letter
            // into uppercase
            else if (titleNext)
            {
                jadenChar = Character.toTitleCase(jadenChar);
                titleNext = false;
            }

            // Convert any string to lowercase by default
            else
            {
                // Append every letter to the string builder
                jadenChar = Character.toLowerCase(jadenChar);
            }
        
            // Append the characters to the string builder
            jadenString.append(jadenChar);
        }

        // return the Jaden String
		return jadenString.toString();
	}
}