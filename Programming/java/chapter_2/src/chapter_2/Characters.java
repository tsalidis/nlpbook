package chapter_2;

public class Characters
{
	private static final int UNICODDE_GREEK_COPTIC_BLOCK_START = 0x0370;
	private static final int UNICODE_GREEK_COPTIC_BLOCK_END    = 0x03FF;

	private static final int UNICODDE_GREEK_EXTENDED_BLOCK_START = 0x1F00;
	private static final int UNICODE_GREEK_EXTENDED_BLOCK_END    = 0x1FFF;

	private static final int UNICODDE_ANSII_BLOCK_START = 0x0000;
	private static final int UNICODE_ANSII_BLOCK_END    = 0x007F;

	private static String getCategoryName(int type)
	{
		String catName = null;
		
		switch(type)
		{
			case Character.UPPERCASE_LETTER: catName = "UPPERCASE"; break;
		  case Character.LOWERCASE_LETTER: catName = "LOWERCASE"; break;
		  case Character.TITLECASE_LETTER: catName = "TITLECASE"; break;
		  case Character.MODIFIER_LETTER:  catName = "MODIFIER";  break;
		  case Character.OTHER_LETTER:     catName = "OTHER";     break;
		
		  // Mark
		  case Character.NON_SPACING_MARK:       
		  	catName =  "NON_SPACING_MARK";       
		  	break;
		  case Character.COMBINING_SPACING_MARK: 
		  	catName =  "COMBINING_SPACING_MARK"; 
		  	break;
		  case Character.ENCLOSING_MARK:         
		  	catName =  "ENCLOSING_MARK";         
		  	break;
		
		  // Number
		  case Character.DECIMAL_DIGIT_NUMBER: 
		  	catName =  "DECIMAL_DIGIT_NUMBER";    
		  	break;
		  case Character.LETTER_NUMBER:        
		  	catName =  "LETTER_NUMBER";           
		  	break;
		  case Character.OTHER_NUMBER: 
		  	catName =  "OTHER_NUMBER";    
		  	break;
		
		  // Punctuation
		  case Character.CONNECTOR_PUNCTUATION:     
		  	catName =  "CONNECTOR_PUNCTUATION";     
		  	break;
		  case Character.DASH_PUNCTUATION:          
		  	catName =  "DASH_PUNCTUATION";         
		  	break;
		  case Character.START_PUNCTUATION:         
		  	catName =  "START_PUNCTUATION";         
		  	break;
		  case Character.END_PUNCTUATION:           
		  	catName =  "END_PUNCTUATION";           
		  	break;
		  case Character.INITIAL_QUOTE_PUNCTUATION: 
		  	catName =  "INITIAL_QUOTE_PUNCTUATION"; 
		  	break;
		  case Character.FINAL_QUOTE_PUNCTUATION:   
		  	catName =  "FINAL_QUOTE_PUNCTUATION";   
		  	break;
		  case Character.OTHER_PUNCTUATION:         
		  	catName =  "OTHER_PUNCTUATION";         
		  	break;
		
		  // Symbol
		  case Character.MATH_SYMBOL:     
		  	catName =  "MATH_SYMBOL";     
		  	break;
		  case Character.CURRENCY_SYMBOL: 
		  	catName =  "CURRENCY_SYMBOL"; 
		  	break;
		  case Character.MODIFIER_SYMBOL: 
		  	catName =  "MODIFIER_SYMBOL"; 
		  	break;
		  case Character.OTHER_SYMBOL:    
		  	catName =  "OTHER_SYMBOL";   
		  	break;
		
		  // Separator
		  case Character.SPACE_SEPARATOR:     
		  	catName =  "SPACE_SEPARATOR";     
		  	break;
		  case Character.LINE_SEPARATOR:      
		  	catName =  "LINE_SEPARATOR";      
		  	break;
		  case Character.PARAGRAPH_SEPARATOR: 
		  	catName =  "PARAGRAPH_SEPARATOR"; 
		  	break;
		
		  // Other
		  case Character.CONTROL:     catName =  "CONTROL";     break;
		  case Character.FORMAT:      catName =  "FORMAT";      break;
		  case Character.SURROGATE:   catName =  "SURROGATE";   break;
		  case Character.PRIVATE_USE: catName =  "PRIVATE_USE"; break;
		  case Character.UNASSIGNED:  catName =  "UNASSIGNED";  break;
		
		  default: 
		  	catName =  "ERROR - Unknown Category type: " + type + ".";
		  	break;
		}
		
		return catName;
	}
	
	private static void printUnicodeBlock (	String header, 
			                                    int start_block, 
			                                    int end_block    )
	{
		System.out.println("Unicode Block: "+header);
		for (int i=start_block; i < end_block; i++)
		{
			System.out.printf("Code Point: %s, Character: %c, Name: %s, Type: %s\n",
					String.format("0x%04X", i),
					(char)i,
					Character.getName(i), 
					getCategoryName(Character.getType(i)));
		}		
	}
	
	public static void main(String[] args)
	{
		printUnicodeBlock("ANSII",
				UNICODDE_ANSII_BLOCK_START,
				UNICODE_ANSII_BLOCK_END);
		
		System.out.println();
		
		printUnicodeBlock("GREEK COPTIC",
				UNICODDE_GREEK_COPTIC_BLOCK_START,
				UNICODE_GREEK_COPTIC_BLOCK_END);
		
		System.out.println();
		
		printUnicodeBlock("GREEK EXTENDED",
				UNICODDE_GREEK_EXTENDED_BLOCK_START,
				UNICODE_GREEK_EXTENDED_BLOCK_END);
	}
}
