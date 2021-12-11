package chapter_3;

public class GreekHyphenator
{
	private static final int MAX_PHONE_CHARS = 4;
	
	private static final char HYPHEN_CHAR    = '-';

	private static final int  NO_HYPH_POS    = -1;
	
//	private static final char VOWEL_TYPE     = 'v';
//	private static final char CONSONANT_TYPE = 'c';
//	private static final char HYPHEN_TYPE    = HYPHEN_CHAR;
	
	private static boolean isVowel(char ch)
	{
		boolean isv = false;

		switch (ch)
		{
			case 'Α': case 'Ά': case 'α': case 'ά':
			case 'Ε': case 'Έ': case 'ε': case 'έ':
			case 'Η': case 'Ή': case 'η': case 'ή':
			case 'Ι': case 'Ί': case 'ι': case 'ί': case 'ϊ': case 'ΐ':  
			case 'Ο': case 'Ό': case 'ο': case 'ό':
			case 'Υ': case 'Ύ': case 'υ': case 'ύ': case 'ϋ': case 'ΰ':  
			case 'Ω': case 'Ώ': case 'ω': case 'ώ':  
				isv = true;
				break;
		}

		return isv;
	}

	private static boolean isAccentVowel(char ch)
	{
		boolean isv = false;

		switch (ch)
		{
			case 'Ά': case 'ά': case 'Έ': case 'έ':
			case 'Ή': case 'ή': case 'Ί': case 'ί': case 'ϊ': case 'ΐ':  
			case 'Ό': case 'ό': case 'Ύ': case 'ύ': case 'ϋ': case 'ΰ':  
			case 'Ώ': case 'ώ':  
				isv = true;
				break;
		}

		return isv;
	}
	
	private static boolean isConsonant(char ch)
	{
		return !isVowel(ch);
	}

	private static boolean isValidVowelBigram(char chVowel1, char chVowel2)
	{
		boolean  val = false;

		switch (chVowel1)
		{
			case 'α': 
				switch (chVowel2)
				{
					case 'η': case 'ή': case 'ι': 
					case 'ί': case 'ϊ':	case 'υ': 
					case 'ύ': 
						val = true;
				}
				break;
			case 'ε': 
				switch (chVowel2)
				{
					case 'ι': case 'ί': case 'υ': 
					case 'ύ': 
						val = true;
				}
				break;
			case 'ι': 
				switch (chVowel2)
				{
					case 'α': case 'ά': case 'ε': 
					case 'έ': case 'ο': case 'ό': 
					case 'ω': case 'ώ': 
						val = true;
				}
				break;
			case 'ο': 
				switch (chVowel2)
				{
					case 'ι': case 'ί': case 'υ': 
					case 'ύ': case 'η':	case 'ή': 
						val = true;
				}
				break;
			case 'υ': 
				switch (chVowel2)
				{
					case 'α': case 'ά': case 'ι': 
					case 'ί': case 'ο':	case 'ό': 
					case 'ω': case 'ώ': 
						val = true;
				}
				break;
		}

		return val;
	}

	private static boolean isValidVowelTrigram(char chVowel1, char chVowel2, char chVowel3)
	{
		boolean  val = false;

		switch (chVowel1)
		{
			case 'ε':  // εια ειε ειο ειω
				if ( chVowel2 == 'ι')
					switch (chVowel3)
					{
						case 'α': case 'ά': case 'ε':
						case 'έ':	case 'ω': case 'ώ':
							val = true;
					}
				break;
			case 'ο':  // οια οιε οιο
				if ( chVowel2 == 'ι')
					switch (chVowel3)
					{
						case 'α': case 'ά': case 'ε':
						case 'έ': case 'ο':	case 'ό':
							val = true;
					}
		} 
		
		return val;
	}
	
	private static boolean isValidVowelFourgram(char chVowel1, char chVowel2, char chVowel3, char chVowel4)
	{
		boolean  val = false;

		switch (chVowel1)
		{
			case 'ε':  // ειου, ειού
				if ( (chVowel2 == 'ι') && (chVowel3 == 'ο') && ( (chVowel4 == 'υ') || (chVowel4 == 'ύ') ) )
					val = true;
				break;
			case 'ο':  // οιου, οιού
				if ( chVowel2 == 'ι')
					if ( (chVowel2 == 'ι') && (chVowel3 == 'ο') && ( (chVowel4 == 'υ') || (chVowel4 == 'ύ') ) )
						val = true;
					break;
		} 
		
		return val;
	}
	
	private static boolean isValidConsonantBigram(char chConsonant1, char chConsonant2)
	{
		boolean valid = false;

		switch (chConsonant1)
		{
			case 'β':      //βγ, βδ, βλ, βρ
				switch (chConsonant2)
				{
					case 'γ': case 'δ': case 'λ':
					case 'ρ':
						valid = true;
				}
				break;
			case 'γ':      // γδ, γκ, γλ, γν, γρ
				switch (chConsonant2)
				{
					case 'δ': case 'κ': case 'λ':
					case 'ν': case 'ρ':
						valid = true;
				}
				break;
			case 'δ':      // δρ
				switch (chConsonant2)
				{
					case 'ρ':
						valid = true;
				}
				break;
			case 'θ':      // θλ, θν, θρ
				switch (chConsonant2)
				{
					case 'λ': case 'ν': case 'ρ':
						valid = true;
				}
				break;
			case 'κ':      // κβ, κλ, κν, κρ, κτ
				switch (chConsonant2)
				{
					case 'β': case 'λ': case 'ν':
					case 'ρ':	case 'τ':
						valid = true;
				}
				break;
				
			case 'μ':      // μν, μπ
				switch (chConsonant2)
				{
					case 'ν': case 'π':
						valid = true;
				}
				break;
			case 'ν':      //  ντ
				switch (chConsonant2)
				{
					case 'τ':
						valid = true;
				}
				break;
			case 'π':      //  πλ, πν, πρ, πτ
				switch (chConsonant2)
				{
					case 'λ': case 'ν': case 'ρ':
					case 'τ':
						valid = true;
				}
				break;
			case 'σ':      // σβ, σγ, σθ, σκ, σλ, σμ, σν, σπ, στ, σφ, σχ
				switch (chConsonant2)
				{
					case 'β': case 'γ': case 'θ':
					case 'κ': case 'λ': case 'μ':
					case 'ν': case 'π': case 'τ':
					case 'φ': case 'χ':
						valid = true;
				}
				break;				
			case 'τ':      // τζ, τμ, τρ, τσ
				switch (chConsonant2)
				{
					case 'ζ': case 'μ': case 'ρ':
					case 'σ':
						valid = true;
				}
				break;
				
			case 'φ':      // φθ, φκ, φλ, φρ, φτ, φχ
				switch (chConsonant2)
				{
					case 'θ': case 'κ': case 'λ':
					case 'ρ':	case 'τ': case 'χ':
						valid = true;
				}
				break;
			case 'χ':      // χθ, χλ, χν, χρ, χτ
				switch (chConsonant2)
				{
					case 'θ': case 'λ': case 'ν':
					case 'ρ':	case 'τ':
						valid = true;
				}
				break;
		}

		return valid;
	}
	
	private static int getPhoneme(String word, int wpos, boolean fVowel, char[] phoneme)
	{
		final int WORD_LEN  = word.length();

		int count = 0;
		
		while (wpos < WORD_LEN)
		{
			char  ch = word.charAt(wpos++);
			
			if ( (fVowel && isVowel(ch)) || (!fVowel && isConsonant(ch)) )
				phoneme[count++] = ch;
			else
				break;
		}
		
		return count;
	}

	private static int FindHyphenInVowelsPhoneme(char[] vowelPhoneme, int phoneLen)
	{
		int hpos = NO_HYPH_POS;
		
		switch (phoneLen)
		{
			case 1:
				break;
			case 2:
				if (!isValidVowelBigram(vowelPhoneme[0],vowelPhoneme[1]))
					hpos = 1;
				break;
			case 3:
				if (!isValidVowelTrigram(vowelPhoneme[0],vowelPhoneme[1],vowelPhoneme[2]))
				{
					if (!isValidVowelBigram(vowelPhoneme[0],vowelPhoneme[1]))
						hpos = 1;
					else if (!isAccentVowel(vowelPhoneme[2]))
						hpos = 2;
				}
				break;
			case 4:
				if (!isValidVowelFourgram(vowelPhoneme[0],vowelPhoneme[1],vowelPhoneme[2],vowelPhoneme[3]))
				{
					if (!isValidVowelTrigram(vowelPhoneme[0],vowelPhoneme[1],vowelPhoneme[2]))
					{
						if (!isValidVowelBigram(vowelPhoneme[0],vowelPhoneme[1]))
							hpos = 1;
						else if (!isAccentVowel(vowelPhoneme[2]))
							hpos = 2;
					}
					else
						hpos = 3;
				}
				break;
		}
		
		return hpos;
	}
	
	private static int FindHyphenInConsonantsPhoneme(char[] vowelPhoneme, int phoneLen, boolean fLastPhoneme)
	{
		int hpos = NO_HYPH_POS;
		
		if (!fLastPhoneme)
		{
			switch (phoneLen)
			{
				case 1:
					hpos = 0;
					break;
				case 2:	case 3:	case 4:
					if (!isValidConsonantBigram(vowelPhoneme[0],vowelPhoneme[1]))
						hpos = 1;
					break;
			}			
		}
		
		return hpos;
	}
	
	static private String  AppendPhoneme(String hyphWord, char[] phoneme, int phonelen)
	{
		for (int i=0; i < phonelen; i++)
			hyphWord += phoneme[i];

		return hyphWord;
	}
	
	/**
	 * Hyphenate a word.
	 * @param word
	 * @return the hyphenated word  
	 */
	public static String hyphenate(String word)
	{
		String  hyphWord  = "";

		// 3 consecutive phonemes cvc
		char[][]  phonemes  = new char[3][MAX_PHONE_CHARS];
		int []    phonelens = new int[3];
		
		final int WORD_LEN  = word.length();
		int       hyph_pos  = 0;
		
		for (int i=0; i < WORD_LEN; i = hyph_pos)
		{
			// fill the phonemes
			
			int  widx = i;
			int  count;
			
			phonelens[1] = phonelens[2] = 0;
			
			// read the first phoneme with consonants
			count = phonelens[0] = getPhoneme(word,widx,false,phonemes[0]);			
			widx += count;
			if (widx != WORD_LEN)
			{
				// read the second phoneme with vowels
				count = phonelens[1] = getPhoneme(word,widx,true,phonemes[1]);
				widx += count;
				if (widx != WORD_LEN)
				{
					// read the third phoneme with consonants
					count = phonelens[2] = getPhoneme(word,widx,false,phonemes[2]);
					widx += count;
				}
			}
			
			// process the phonemes
			// Step 1 Append the first phoneme with consonants
			hyphWord = AppendPhoneme(hyphWord,phonemes[0],phonelens[0]);
			hyph_pos += phonelens[0];  
			
			// Step 2 Find the hyphen in second phoneme with vowels. 
			int hpos = FindHyphenInVowelsPhoneme(phonemes[1],phonelens[1]);
			
			if (hpos >= 0)
			{
				// append the first part of phoneme
				hyphWord = AppendPhoneme(hyphWord,phonemes[1],hpos);
				
				// append hyphen
				hyphWord += HYPHEN_CHAR;
				hyph_pos += hpos;
			}
			else // vowels cannot be hyphenated
			{
				// append vowels to word
				hyphWord = AppendPhoneme(hyphWord,phonemes[1],phonelens[1]);
				hyph_pos += phonelens[1];

				boolean  fLastPhoneme = hyph_pos+phonelens[2] == WORD_LEN;
				
				hpos = FindHyphenInConsonantsPhoneme(phonemes[2],phonelens[2],fLastPhoneme );
				
				if (hpos >= 0)
				{
					hyphWord = AppendPhoneme(hyphWord,phonemes[2],hpos);
					hyphWord += HYPHEN_CHAR;
					
					hyph_pos += hpos;
				}
				else if (!fLastPhoneme)
					hyphWord += HYPHEN_CHAR;					
			}
		}
				
		return hyphWord;
	}

	public static void main(String[] args)
	{
		String[] testWords = { "οσφυοκάμπτης",
				"καλά", "έχω", "αηδόνι", "ουρανός", "ναύτης", "ατμός", "έρχομαι", "αστράφτω", "σφυρίχτρα", "άνθρωπος", "φεγγάρι", "σύννεφο",
				"δουλειά", "άδειες", "άδειος", "αργαλειού", "άδειων", "λειώνω", "ίδιες", "ίδιος", "καινούργιου", "παιδιού", "ματιών", "κάποια", "οποιεσδήποτε",
				"ποιος", "τέτοιους", "μυαλό", "δυο", "σταχυού", "Καρυωτάκης", "σταχυών", "εχθρός", "αργαλειού", "σπρωγμένος", "οσφυοκάμπτης", "γκραβούρα", "άστρο",
				"έξαψη", "ταψιού", "απέκκριση"};

		for (String word : testWords)
		{
			String hyphWord = hyphenate(word);

			System.out.printf("Word: <%s>, Hyphenated Word: <%s>\n",word,hyphWord);
		}
	}
}
