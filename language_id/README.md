UDHR Language ID
=========

Written in Python 2.7.6. with NLTK 2

This program is inspired by chapter 3, exercise 43 of the NLTK book.  The program checks an input text file (UTF-8 encoding) against the UDHR corpus for English, French, German, Italian, Portuguese, and Spanish.  The program ranks the liklihood that the input text is a match for one of these languages and returns the most likely language match.

In order to use the UDHR Language ID, you will need one plain text file in UTF-8 encoding.  The file can be in any one of English, French, German, Italian, Portuguese, or Spanish.

Make sure that 'MY_PATH' on line 5 points the the directory for this file.

'MY_TEXT_FILE' (on line 6) should contain the name of your text file.

You can test the program with the text files in the 'texts' subfolder of this repo.  There is one file, a Wikipedia article about soccer, for each of the aforementioned languages.

License
=========
Copyright (c) 2014 Justin Glover

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
