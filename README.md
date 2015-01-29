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
 ################ ../../Juliet/src/testcases/CWE83_XSS_Attribute/CWE83_XSS_Attribute__Servlet_connect_tcp_22b.java ################
Looking for COOKIES
Looking for HTTP REQUESTS STRINGS
 24 :  import java.io.InputStreamReader;

 43 :                  InputStreamReader readerInputStream = null;

 49 :                      readerInputStream = new InputStreamReader(socket.getInputStream(), "UTF-8");

 50 :                      readerBuffered = new BufferedReader(readerInputStream);

 75 :                          if (readerInputStream != null)

 77 :                              readerInputStream.close();

 82 :                          IO.logger.log(Level.WARNING, "Error closing InputStreamReader", exceptIO);

Code density:  7 
Looking for HTML OUTPUT
Looking for HTML TAGS
Looking for INPUT CONTROLS
Looking for WEB CONFIG
Looking for LOGGING
Looking for THREAD AND CONCURRENCY
Looking for REFLECTION, SERIALIZATION
Looking for EXCEPTIONS & ERRORS
Looking for CRYPTO
Looking for STORAGE
Looking for AUTHORIZATION, ASSERT & REVERT
Looking for LEGACY METHODS
Looking for INPUT AND OUTPUT STREAMS
 2 :  Filename: CWE83_XSS_Attribute__Servlet_connect_tcp_22b.java

 3 :  Label Definition File: CWE83_XSS_Attribute__Servlet.label.xml

 4 :  Template File: sources-sink-22b.tmpl.java

 23 :  import java.io.BufferedReader;

 42 :                  BufferedReader readerBuffered = null;

 50 :                      readerBuffered = new BufferedReader(readerInputStream);

 70 :                          IO.logger.log(Level.WARNING, "Error closing BufferedReader", exceptIO);

Code density:  7 
Looking for SERVLETS
 21 :  import javax.servlet.http.*;

 32 :      public String badSource(HttpServletRequest request, HttpServletResponse response) throws Throwable

 49 :                      readerInputStream = new InputStreamReader(socket.getInputStream(), "UTF-8");

 110 :      public String goodG2B1Source(HttpServletRequest request, HttpServletResponse response) throws Throwable

 132 :      public String goodG2B2Source(HttpServletRequest request, HttpServletResponse response) throws Throwable

Code density:  5 
Looking for CROSS SITE SCRIPTING
Looking for RESPONSE SPLITING
Looking for REDIRECTION
Looking for SQL & DATABASE
Looking for SSL
Looking for SESSION MANAGEMENT
Looking for LEGACY INTERACTION
Looking for LOGGING
Looking for generic keywords
 ################ ../../Juliet/src/testcases/CWE83_XSS_Attribute/CWE83_XSS_Attribute__Servlet_connect_tcp_31.java ################
Looking for COOKIES
Looking for HTTP REQUESTS STRINGS
 24 :  import java.io.InputStreamReader;

 45 :                  InputStreamReader readerInputStream = null;

 54 :                      readerInputStream = new InputStreamReader(socket.getInputStream(), "UTF-8");

 55 :                      readerBuffered = new BufferedReader(readerInputStream);

 81 :                          if (readerInputStream != null)

 83 :                              readerInputStream.close();

 88 :                          IO.logger.log(Level.WARNING, "Error closing InputStreamReader", exceptIO);

Code density:  7 
Looking for HTML OUTPUT
Looking for HTML TAGS
Looking for INPUT CONTROLS
Looking for WEB CONFIG
Looking for LOGGING
Looking for THREAD AND CONCURRENCY
Looking for REFLECTION, SERIALIZATION
Looking for EXCEPTIONS & ERRORS
Looking for CRYPTO
Looking for STORAGE
Looking for AUTHORIZATION, ASSERT & REVERT
Looking for LEGACY METHODS
Looking for INPUT AND OUTPUT STREAMS
 2 :  Filename: CWE83_XSS_Attribute__Servlet_connect_tcp_31.java

 3 :  Label Definition File: CWE83_XSS_Attribute__Servlet.label.xml

 4 :  Template File: sources-sink-31.tmpl.java

 23 :  import java.io.BufferedReader;

 44 :                  BufferedReader readerBuffered = null;

 55 :                      readerBuffered = new BufferedReader(readerInputStream);

 76 :                          IO.logger.log(Level.WARNING, "Error closing BufferedReader", exceptIO);

Code density:  7 
Looking for SERVLETS
 21 :  import javax.servlet.http.*;

 33 :      public void bad(HttpServletRequest request, HttpServletResponse response) throws Throwable

 54 :                      readerInputStream = new InputStreamReader(socket.getInputStream(), "UTF-8");

 114 :                  response.getWriter().println("<br>bad() - <img src=\"" + data + "\">");

 120 :      public void good(HttpServletRequest request, HttpServletResponse response) throws Throwable

 126 :      private void goodG2B(HttpServletRequest request, HttpServletResponse response) throws Throwable

 143 :                  response.getWriter().println("<br>bad() - <img src=\"" + data + "\">");

Code density:  7 
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

