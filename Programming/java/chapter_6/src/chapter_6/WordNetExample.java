package chapter_6;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import net.didion.jwnl.JWNL;
import net.didion.jwnl.JWNLException;
import net.didion.jwnl.data.IndexWord;
import net.didion.jwnl.data.POS;
import net.didion.jwnl.data.Synset;
import net.didion.jwnl.dictionary.Dictionary;

import net.didion.jwnl.data.PointerType;
import net.didion.jwnl.data.PointerUtils;
import net.didion.jwnl.data.list.PointerTargetNodeList;
import net.didion.jwnl.data.list.PointerTargetTree;
import net.didion.jwnl.data.relationship.AsymmetricRelationship;
import net.didion.jwnl.data.relationship.Relationship;
import net.didion.jwnl.data.relationship.RelationshipFinder;
import net.didion.jwnl.data.relationship.RelationshipList;

import java.util.Iterator;

public class WordNetExample 
{
  final Dictionary          dictionary;
  final PointerUtils        pointerUtils;
  final RelationshipFinder  relationshipFinder;
  
  private WordNetExample() throws FileNotFoundException, JWNLException
  {
    JWNL.initialize(new FileInputStream("properties.xml")); 
    
    dictionary         = Dictionary.getInstance();
    pointerUtils       = PointerUtils.getInstance();
    relationshipFinder = RelationshipFinder.getInstance();
  }
  
  public static void main(String[] args) 
      throws FileNotFoundException, JWNLException 
  {
    WordNetExample wnex = new WordNetExample();
    
    wnex.SimpleExample();
    wnex.FullExample();
  }

  private void SimpleExample() throws JWNLException
  {
    IndexWord indexWord = dictionary.getIndexWord(POS.NOUN, "cat");
    
    Synset[] senses = indexWord.getSenses();

    System.out.println();
    System.out.println("Simple Example. Synsets for word 'cat' as noun");
     
    for (Synset set : senses) 
    {
      System.out.println(indexWord + ": " + set.getGloss());
    }

    indexWord = dictionary.getIndexWord(POS.VERB, "cat");
    if (indexWord != null)
    {
      System.out.println("Simple Example. Synsets for word 'cat' as verb");
      
      for (Synset set : senses) 
      {
        System.out.println(indexWord + ": " + set.getGloss());
      }
    }
  }
  
  private IndexWord ACCOMPLISH;
  private IndexWord DOG;
  private IndexWord CAT;
  private IndexWord FUNNY;
  private IndexWord DROLL;
  private IndexWord MEN;
  private IndexWord WOMAN;
  private IndexWord DRAW;
  private IndexWord BE;

  public void FullExample() throws JWNLException 
  {
    ACCOMPLISH = dictionary.getIndexWord(POS.VERB, "accomplish");
    DOG        = dictionary.getIndexWord(POS.NOUN, "dog");
    CAT        = dictionary.lookupIndexWord(POS.NOUN, "cat");
    FUNNY      = dictionary.lookupIndexWord(POS.ADJECTIVE, "funny");
    DROLL      = dictionary.lookupIndexWord(POS.ADJECTIVE, "droll");
    MEN        = dictionary.lookupIndexWord(POS.NOUN, "men");
    WOMAN      = dictionary.lookupIndexWord(POS.NOUN, "woman");
    DRAW       = dictionary.lookupIndexWord(POS.VERB, "draw");
    BE         = dictionary.lookupIndexWord(POS.VERB, "be");

    System.out.println();
    System.out.println("Complex Example");
    
    printLemma(MEN);
    printLemma(DRAW);
    printLemma(WOMAN);
    printLemma(BE);
    printHypenyms(ACCOMPLISH);
    printHyponyms(DOG);
    printAsymmetricRelationships(DOG, CAT);
    printSymmetricRelationships(FUNNY, DROLL);
  }

  private void printLemma(IndexWord word) 
  {
    String lemma = word.getLemma();
    
    System.out.println("Word = " + word + "Lemma = " + lemma );
  }

  private void printHypenyms(IndexWord word) 
      throws JWNLException 
  {
    // Get all of the hypernyms (parents) of the first sense of <var>word</var>
    PointerTargetNodeList hypernyms = pointerUtils.getDirectHypernyms(word.getSense(1));
    
    System.out.println("Direct hypernyms of \"" + word.getLemma() + "\":");
    hypernyms.print();
  }

  private void printHyponyms(IndexWord word) 
      throws JWNLException 
  {
    // Get all the hyponyms (children) of the first sense of <var>word</var>
    PointerTargetTree hyponyms = pointerUtils.getHyponymTree(word.getSense(1));
    
    System.out.println("Hyponyms of \"" + word.getLemma() + "\":");
    hyponyms.print();
  }

  private void printAsymmetricRelationships(IndexWord start, IndexWord end) 
      throws JWNLException 
  {
    // Try to find a relationship between the first sense 
    // of <var>start</var> and the first sense of <var>end</var>
    RelationshipList list = relationshipFinder.findRelationships(start.getSense(1), 
                                                                 end.getSense(1), 
                                                                 PointerType.HYPERNYM);
    
    System.out.println("Hypernym relationship between \"" 
                       + start.getLemma() 
                       + "\" and \"" 
                       + end.getLemma() + "\":");
    for (Iterator<?> itr = list.iterator(); itr.hasNext();) 
    {
      ((Relationship) itr.next()).getNodeList().print();
    }
    
    System.out.println("Common Parent Index: " 
                       + ((AsymmetricRelationship) list.get(0)).getCommonParentIndex());
    System.out.println("Depth: " 
                       + ((Relationship) list.get(0)).getDepth());
  }

  private void printSymmetricRelationships(IndexWord start, IndexWord end) 
      throws JWNLException 
  {
    // find all synonyms that <var>start</var> and <var>end</var> have in common
    RelationshipList list = relationshipFinder.findRelationships(start.getSense(1), 
                                                                 end.getSense(1), 
                                                                 PointerType.SIMILAR_TO);
  
    System.out.println("Synonym relationship between \"" 
                        + start.getLemma() 
                        + "\" and \"" 
                        + end.getLemma() + "\":");
    for (Iterator<?> itr = list.iterator(); itr.hasNext();) 
    {
        ((Relationship) itr.next()).getNodeList().print();
    }
    
    System.out.println("Depth: " + ((Relationship) list.get(0)).getDepth());
  }    
}
