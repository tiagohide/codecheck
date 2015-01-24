# codecheck
Code Check is a search tool that look for sensitive functions in source code for reviewing purpose 

Code Check Search 0.1 is a search tool that look for sensitive function in java and in the future for .net as well 
Code Check helps developers and security community to looking into sensitive functions in their codes for reviewing purpose it is a simple tool that prints the line number of the code and the function that they should investigate for possible flaws


### Version
0.1

### Usage
```sh
$ python search.py java-samples/
```

### Sample output

```sh
################ ../../Juliet/src/testcases/CWE80_XSS/s01/CWE80_XSS__CWE182_Servlet_File_14.java ################
Looking for COOKIES
Looking for HTTP REQUESTS STRINGS
 22 :  InputStreamReader;
 23 :  InputStream;
 40 :  InputStream streamFileInput = null;
 41 :  InputStreamReader readerInputStream = null;
 46 :  InputStream(file);
 47 :  InputStream = new InputStreamReader(streamFileInput, "UTF-8");
 48 :  InputStream);
 75 :  InputStream != null)
 77 :  InputStream.close();
 82 :  InputStreamReader", exceptIO);
 94 :  InputStream", exceptIO);
Code density:  11 
Looking for HTML OUTPUT
Looking for HTML TAGS
Looking for INPUT CONTROLS
Looking for WEB CONFIG
 11 :  allow XSS (CWE 182: Collapse of Data into Unsafe Value)
 108 :  allow XSS with strings like <scr<script>ipt> (CWE 182: Collapse of Data into Unsafe Value) */
 134 :  allow XSS with strings like <scr<script>ipt> (CWE 182: Collapse of Data into Unsafe Value) */
 158 :  allow XSS with strings like <scr<script>ipt> (CWE 182: Collapse of Data into Unsafe Value) */
Code density:  4 
Looking for LOGGING
Looking for THREAD AND CONCURRENCY
Looking for REFLECTION, SERIALIZATION
Looking for EXCEPTIONS & ERRORS
Looking for CRYPTO
Looking for STORAGE
Looking for AUTHORIZATION, ASSERT & REVERT
Looking for LEGACY METHODS
Looking for INPUT AND OUTPUT STREAMS
 2 :  Filename: CWE80_XSS__CWE182_Servlet_File_14.java
 3 :  File: CWE80_XSS__CWE182_Servlet.label.xml
 4 :  File: sources-sink-14.tmpl.java
 9 :  File Read data from file (named c:\data.txt)
 21 :  BufferedReader;
 23 :  FileInputStream;
 24 :  File;
 29 :  File_14 extends AbstractTestCaseServlet
 39 :  File file = new File("C:\\data.txt");
 40 :  FileInputStream streamFileInput = null;
 42 :  BufferedReader readerBuffered = null;
 46 :  FileInputStream(file);
 47 :  FileInput, "UTF-8");
 48 :  BufferedReader(readerInputStream);
 70 :  BufferedReader", exceptIO);
 87 :  FileInput != null)
 89 :  FileInput.close();
 94 :  FileInputStream", exceptIO);
Code density:  18 
Looking for SERVLETS
 19 :  javax.servlet.http.*;
 32 :  HttpServletRequest request, HttpServletResponse response) throws Throwable
 109 :  getWriter().println("<br>bad(): data = " + data.replaceAll("(<script>)", ""));
 115 :  HttpServletRequest request, HttpServletResponse response) throws Throwable
 135 :  getWriter().println("<br>bad(): data = " + data.replaceAll("(<script>)", ""));
 141 :  HttpServletRequest request, HttpServletResponse response) throws Throwable
 159 :  getWriter().println("<br>bad(): data = " + data.replaceAll("(<script>)", ""));
 164 :  HttpServletRequest request, HttpServletResponse response) throws Throwable
Code density:  8 
Looking for CROSS SITE SCRIPTING
Looking for RESPONSE SPLITING
Looking for REDIRECTION
Looking for SQL & DATABASE
Looking for SSL
Looking for SESSION MANAGEMENT
Looking for LEGACY INTERACTION
Looking for LOGGING
Looking for generic keywords
 

```

License
----
MIT

**Free Software, Hell Yeah!**

