# codecheck
Code Check is a search tool that look for sensitive functions in source code for reviewing purpose 

Code Check Search 0.1 is a search tool that look for sensitive function in java and in the future for .net as well 
Code Check helps developers and security community to looking into sensitive functions in their codes for reviewing purpore it is a simple tool that prints the line number of the code and the function that they should investigate for possible flaws


### Version
0.1

### Usage
```sh
$ python search.py java-samples/
```

### Sample output

```sh
 ################ Java/class files/Polling.class ################
Looking for COOKIES
Looking for HTTP REQUESTS STRINGS
Looking for HTML OUTPUT
Looking for HTML TAGS
Looking for INPUT CONTROLS
Looking for WEB CONFIG
Looking for LOGGING
Looking for THREAD AND CONCURRENCY
Looking for REFLECTION, SERIALIZATION
Looking for EXCEPTIONS & ERRORS
Looking for CRYPTO
 116 :  DESL?	 TEMPSEN I.CODE?
 PicoPass 16? PicoPass 16K? PicoPass 16K(8x2? PicoPass 16KS(8x2? PicoPass 32KS(16+16? PicoPass 32KS(16+8x2? PicoPass 32KS(8x2+16? PicoPass 32KS(8x2+8x? LRI6?
      I.CODE UI?
                 I.CODE EP? LRI1? LRI12?
                                         Mifare Min?
                                                    067577810280 
 117 :  DESFir?50122345561253544E3381C?	ST19XRC8ERIDVacardNamecallCardConnect(I)IreqTypeACSModule$SCARD_IO_REQUEST 
Code density:  2 
Looking for STORAGE
Looking for AUTHORIZATION, ASSERT & REVERT
Looking for LEGACY METHODS
Looking for INPUT AND OUTPUT STREAMS
 126 :  File
            Polling.java
ParallelGroupSequentialGroupDjavax/swing/LayoutStyleComponentPlacement! swing/GroupLayout$GroupGroup
Code density:  1 
Looking for SERVLETS
Looking for CROSS SITE SCRIPTING
Looking for RESPONSE SPLITING
Looking for REDIRECTION
Looking for SQL & DATABASE
```

License
----
MIT

**Free Software, Hell Yeah!**

