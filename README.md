# Regx-Dev #

This package is made to developers for saving them time while playing in scraping the information.

## Feature's of this project

* Find's any format of phone number irrespective of the country.
* Can find links from the string.
* Can extract the mail id from string.
* Removes any links from the string.
* Return's the index of the matching word present in the string as list.
* Can replace any word provided with new word.

# How to install and using it.

`pip install Regx-Dev`

` from Regx-Dev import Regxdev as rd `

* For finding phone number from the string you passed.

  ` result = rd.phone_finder("PASS THE STRNG CONTAINING NUMBEERS") ` returns list of phone numbers 

    Note: This method works only if numbers starts with pre-fix '+' and not containing parentheses.

* For finding links.

  ` result = rd.link_finder("PASS THE STRING") ` returns list of links in the string.

* For extracting mail id's.
  
  ` result = rd.mail_extractor("PASS THE STRING") `

* For removing links.

  ` result = rd.link_remover("PASS THE STRING") `

* This returns a list of tuple's that is the index of matched word you were searching for in the list.

  ` result = rd.word_finder("WORD TO BE FOUND", "PASS THE STRING") `
  
  Example: when you run the above line you get output similar to ` result = [(2, 5), (11, 14)] ` each item are tuples, which contains start index and end index of the word. you can use this tuple and by slicing the string you will have the word.

* To replace any word from the string irrespective of length.
  
  ` result = rd.word_replacer("WORD TO REPLACE", "WORD TO BE REPLACED FOR", "PASS THE STRING") `

  This returns new string with replaced charecter.
