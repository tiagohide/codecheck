
def http_requests():
    s =   "(java.io.PrintStream.write).*","(accepttypes).*","(request.browser).*","(request.files).*","(request.headers).*","(request.httpmethod).*","(request.item).*","(request.querystring).*","(request.form).*","(request.cookies).*","(request.certificate).*","(request.rawurl).*","(request.servervariables).*","(request.url).*","(request.urlreferrer).*","(request.useragent).*","(request.userlanguages).*","(request.IsSecureConnection).*","(request.TotalBytes).*","(request.BinaryRead).*","(InputStream).*","(HiddenField.Value).*","(TextBox.Text).*","(recordSet).*"
    return s

def html_output():
    s = "(response.write).*","(<% =).*","(HttpUtility).*","(HtmlEncode).*"
    return s

def cookies():
    s = "(System.Net.Cookie).*","(HTTPOnly).*","(document.cookie).*"
    return s

def html_tags(): 
    s = "(HtmlEncode).*","(URLEncode).*","(<applet>).*","(<frameset>).*","(<embed>).*","(<frame>).*","(<html>).*","(<iframe>).*","(<img>).*","(<style>).*","(<layer>).*","(<ilayer>).*","(<meta>).*","(<object>).*","(<body>).*","(<frame security).*","(<iframe security).*"
    return s

def input_controls(): 
    s = "(system.web.ui.htmlcontrols.htmlinputhidden).*","(system.web.ui.webcontrols.hiddenfield).*","(system.web.ui.webcontrols.hyperlink).*","(system.web.ui.webcontrols.textbox).*","(system.web.ui.webcontrols.label).*","(system.web.ui.webcontrols.linkbutton).*","(system.web.ui.webcontrols.listbox).*","(system.web.ui.webcontrols.checkboxlist).*","(system.web.ui.webcontrols.dropdownlist).*"
    return s

def web_config(): 
    s = "(requestEncoding).*","(responseEncoding).*","(trace).*","(authorization).*","(compilation).*","(CustomErrors).*","(httpCookies).*","(httpHandlers).*","(httpRuntime).*","(sessionState).*","(maxRequestLength).*","(debug).*","(forms protection).*","(appSettings).*","(ConfigurationSettings).*","(appSettings).*","(connectionStrings).*","(authentication mode).*","(allow).*","(deny).*","(credentials).*","(identity impersonate).*","(timeout).*","(remote).*","(global.asax).*","(Application_OnAuthenticateRequest).*","(Application_OnAuthorizeRequest).*","(Session_OnStart).*","(Session_OnEnd).*"
    return s

def logging(): 
    s = "(log4net).*","(Console.WriteLine).*","(System.Diagnostics.Debug).*","(System.Diagnostics.Trace).*","(Machine.config).*","(validateRequest).*","(enableViewState).*","(enableViewStateMac).*"
    return s

def thread_concurrency(): 
    s = "(Thread).*","(Dispose).*"
    return s


def reclection_serial(): 
    s = "(Serializable).*","(AllowPartiallyTrustedCallersAttribute).*","(GetObjectData).*","(StrongNameIdentityPermission).*","(StrongNameIdentity).*","(System.Reflection).*"
    return s

def exceptions_errors():
    s = "(catch{).*","(Finally).*","(trace enabled).*","(customErrors mode).*"
    return s


def crypto():
    s = "(RNGCryptoServiceProvider).*","(SHA).*","(MD5).*","(base64).*","(xor).*","(DES).*","(RC2).*","(System.Random).*","(Random).*","(System.Security.Cryptography).*"
    return s

def storage():
    s = "(SecureString).*","(ProtectedMemory).*"
    return s

def auth_assert():
    s = "(.RequestMinimum).*","(.RequestOptional).*","(Assert).*","(Debug.Assert).*","(CodeAccessPermission).*","(ReflectionPermission.MemberAccess).*","(SecurityPermission.ControlAppDomain).*","(SecurityPermission.UnmanagedCode).*","(SecurityPermission.SkipVerification).*","(SecurityPermission.ControlEvidence).*","(SecurityPermission.SerializationFormatter).*","(SecurityPermission.ControlPrincipal).*","(SecurityPermission.ControlDomainPolicy).*","(SecurityPermission.ControlPolicy).*"
    return s

def legacy_methods():
    s = "(printf).*","(strcpy).*"
    return s

def inout_streams():
    s = "(Java.io).*","(java.util.zip).*","(java.util.jar).*","(FileInputStream).*","(ObjectInputStream).*","(FilterInputStream).*","(PipedInputStream).*","(SequenceInputStream).*","(StringBufferInputStream).*","(BufferedReader).*","(ByteArrayInputStream).*","(CharArrayReader).*","(File).*","(ObjectInputStream).*","(PipedInputStream).*","(StreamTokenizer).*","(getResourceAsStream).*","(java.io.FileReader).*","(java.io.FileWriter).*","(java.io.RandomAccessFile).*","(java.io.File).*","(java.io.FileOutputStream).*","(mkdir).*","(renameTo).*"
    return s

def servlets(): 
    s  = "(javax.servlet.).*","(getParameterNames).*","(getParameterValues).*","(getParameter).*","(getParameterMap).*","(getScheme).*","(getProtocol).*","(getContentType).*","(getServerName).*","(getRemoteAddr).*","(getRemoteHost).*","(getRealPath).*","(getLocalName).*","(getAttribute).*","(getAttributeNames).*","(getLocalAddr).*","(getAuthType).*","(getRemoteUser).*","(getCookies).*","(isSecure).*","(HttpServletRequest).*","(getQueryString).*","(getHeaderNames).*","(getHeaders).*","(getPrincipal).*","(getUserPrincipal).*","(isUserInRole).*","(getInputStream).*","(getOutputStream).*","(getWriter).*","(addCookie).*","(addHeader).*","(setHeader).*","(setAttribute).*","(putValue).*","(javax.servlet.http.Cookie).*","(getName).*","(getPath).*","(getDomain).*","(getComment).*","(getMethod).*","(getPath).*","(getReader).*","(getRealPath).*","(getRequestURI).*","(getRequestURL).*","(getServerName).*","(getValue).*","(getValueNames).*","(getRequestedSessionId).*"
    return s

def cross_site_scripting(): 
    s = "(javax.servlet.ServletOutputStream.print).*","(javax.servlet.jsp.JspWriter.print).*","(java.io.PrintWriter.print).*"
    return s

def response_spliting(): 
    s = "(javax.servlet.http.HttpServletResponse.sendRedirect).*","(addHeader, setHeader).*"
    return s
def redirection(): 
    s = "(sendRedirect).*","(setStatus).*","(addHeader, setHeader).*"
    return s

def sql_database():
    s = "(jdbc).*","(executeQuery).*","(select).*","(insert).*","(update).*","(delete).*","(execute).*","(executestatement).*","(createStatement).*","(java.sql.ResultSet.getString).*","(java.sql.ResultSet.getObject).*","(java.sql.Statement.executeUpdate).*","(java.sql.Statement.executeQuery).*","(java.sql.Statement.execute).*","(java.sql.Statement.addBatch).*","(java.sql.Connection.prepareStatement).*","(java.sql.Connection.prepareCall).*","(sp_executesql).*","(select from).*","(Insert).*","(update).*","(delete from where).*","(delete).*","(exec sp_).*","(execute sp_).*","(exec xp_).*","(execute sp_).*","(exec@).*","(execute@).*","(executestatement).*","(executeSQL).*","(setfilter).*","(executeQuery).*","(GetQueryResultInXML).*","(adodb).*","(sqloledb).*","(sql server).*","(driver).*","(Server.CreateObject).*","(.Provider).*","(.Open).*","(ADODB.recordset).*","(New OleDbConnection).*","(ExecuteReader).*","(DataSource).*","(SqlCommand).*","(Microsoft.Jet).*","(SqlDataReader).*","(ExecuteReader).*","(GetString).*","(SqlDataAdapter).*","(CommandType).*","(StoredProcedure).*","(System.Data.sql).*"
    return s
def ssl():
    s = "(com.sun.net.ssl).*","(SSLContext).*","(SSLSocketFactory).*","(TrustManagerFactory).*","(HttpsURLConnection).*","(KeyManagerFactory).*"
    return s

def session_management():
    s = "(getSession).*","(invalidate).*","(getId).*"
    return s

def legacy_interaction(): 
    s = "(java.lang.Runtime.exec).*","(java.lang.Runtime.getRuntime).*"
    return s
def log(): 
    s = "(java.io.PrintStream.write).*","(log4j).*","(jLo).*","(Lumberjack).*","(MonoLog).*","(qflog).*","(just4log).*","(log4Ant).*","(JDLabAgent).*"
    return s

def generic(): 
    s = "(Hack).*","(Kludge).*","(Bypass).*","(Steal).*","(Stolen).*","(Divert).*","(Broke).*","(Trick).*","(FIXME).*","(ToDo).*","(Password).*","(Backdoor).*"
    return s
