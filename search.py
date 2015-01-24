#!/usr/bin/env python
import re,sys,os
from Match import * 

# Code Check Search 0.1 is a search tool to look for sensitive function in java and in the future for .net as well 
# This is tool helps developers and security analystis to looking into
# sensitive functions in their codes for reviewing purporse it is a simple tool that prints the line number of the code and the function that they should investigate for possible flaws


print "Code Check 0.1 - A search tool for sensitive functions for java "
print "by Tiago Vilas tvilas at hushmail dot com"


if len(sys.argv) < 2:
    sys.exit('Usage: python %s CodeDirectory' % sys.argv[0])
else: 
    fcode=sys.argv[1]

        
def main(code):
    lcookies(code)
    lrequest(code)
    lhtmloutput(code)
    lhtmltags(code)
    linputcontrols(code)
    lwebconf(code)
    llogging(code)
    lthread(code)
    lreflection(code)
    lexeptions(code)
    lcrypto(code)
    lstorage(code)
    lautho(code)
    llegacy(code)
    linput(code)
    lservlets(code)
    lcross(code)
    lresponse(code)
    lredirection(code)
    lsqldatabase(code)
    lsql(code)
    lsession(code)
    linteraction(code)
    llog(code)
    lgeneric(code)


def look(code,func):
    num_lines=0
    file = open(code,"r")
    density=0
    for line in file:
        num_lines=num_lines+1
        if search(func,line,num_lines) is not None:
            print '\033[1;47m',num_lines,": ",search(func,line,num_lines),'\033[1;m'
            density=density+1
    #print "Code density: ",density
    if density>0:
        print '\033[1;33mCode density: ',density,'\033[1;m'
def search(o,p,q):
    for x in xrange(len(o)):
        match = re.search(o[x], p)
        if match:
            result = match.group()
            #print result
            return result
            #print q 
            return q 
        else:
            result = ""

def lcookies(code):
    print "Looking for COOKIES"
    look(code,cookies())

def lrequest(code):
    print "Looking for HTTP REQUESTS STRINGS"
    look(code,http_requests())

def lhtmloutput(code):
    print "Looking for HTML OUTPUT"
    look(code,html_output())
    
def lhtmltags(code):
    print "Looking for HTML TAGS"
    look(code,html_tags()) 

def linputcontrols(code):
    print "Looking for INPUT CONTROLS"
    look(code,input_controls())

def lwebconf(code):
    print "Looking for WEB CONFIG"
    look(code,web_config()) 

def llogging(code):
    print "Looking for LOGGING"
    look(code,logging())

def lthread(code):
    print "Looking for THREAD AND CONCURRENCY"
    look(code,thread_concurrency())

def lreflection(code):
    print "Looking for REFLECTION, SERIALIZATION"
    look(code,reclection_serial()) 

def lexeptions(code):
    print "Looking for EXCEPTIONS & ERRORS"
    look(code,exceptions_errors())

def lcrypto(code):
    print "Looking for CRYPTO"
    look(code,crypto())

def lstorage(code):
    print "Looking for STORAGE"
    look(code,storage())

def lautho(code):
    print "Looking for AUTHORIZATION, ASSERT & REVERT"
    look(code,auth_assert())

def llegacy(code):
    print "Looking for LEGACY METHODS"
    look(code,legacy_methods())

def linput(code):
    print "Looking for INPUT AND OUTPUT STREAMS"
    look(code,inout_streams())

def lservlets(code):
    print "Looking for SERVLETS"
    look(code,servlets())

def lcross(code):
    print "Looking for CROSS SITE SCRIPTING"
    look(code,cross_site_scripting())

def lresponse(code):
    print "Looking for RESPONSE SPLITING"
    look(code,response_spliting())

def lredirection(code):
    print "Looking for REDIRECTION"
    look(code,redirection()) 

def lsqldatabase(code):
    print "Looking for SQL & DATABASE"
    look(code,sql_database())

def lsql(code):
    print "Looking for SSL"
    look(code,ssl())

def lsession(code):
    print "Looking for SESSION MANAGEMENT"
    look(code,session_management())

def linteraction(code):
    print "Looking for LEGACY INTERACTION"
    look(code,legacy_interaction()) 

def llog(code):
    print "Looking for LOGGING" 
    look(code,log())

def lgeneric(code):
    print "Looking for generic keywords"
    look(code,generic()) 

def dirpath(path):
    dir_code = os.listdir(path)
    for ncode in dir_code:
        code = os.path.join(path, ncode)
        print '\033[1;46m ################ ' + code + ' ################\033[1;m'
        main(code)

dirpath(fcode)
