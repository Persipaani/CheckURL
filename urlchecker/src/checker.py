'''
Created on 4.12.2014

This program checks what suffixes are reserved for a certain url.
For example if checked url is www.google there would be at least
www.google.com, www.google.fi and www.google.se in the results.
Results are stored in results.txt

@author: Sampo
'''

import urllib.request
import http.client
import time
import os

class checker(object):
    
    
    def __init__(self):
        self.url=""
        self.endings=[]
        self.working_urls=[]
        self.get_from_file()
        self.get_input()
        
    def get_from_file(self):
        #self.pull_and_parse() enable to generate new endings list if the file is empty
        endings_file = open("endings.txt","r+")
        endings = endings_file.readlines()[0]
        endings_file.close()
        self.endings = endings.split(" ")
        
    
    def get_input(self):
        '''
        Reads user input, starts and finishes the checking process and keeps a count at
        current status.
        '''
        self.working_urls = []
        input_value = input("Enter beginning of url (example: www.google)\n")
        amount = len(self.endings)
        current = 1.0
        prev_prog = 0.0
        
        start_time = time.time()
        
        for ending in self.endings:
            cur_prog = round((current/amount)*100,0)
            if(cur_prog != prev_prog):
                print(str(cur_prog) + " %")
            prev_prog = cur_prog
            current+=1
            
            self.check_this_ping(input_value, ending)
            #alternative method:
            #self.check_this(input, ending)
            
        end_time = time.time()
        
        print("This took: " + str(end_time-start_time) + " seconds.")
        
        print(self.working_urls)
        
        open("results.txt", "w").close()
        results_file = open("results.txt","r+")
        string = ""
        n = 0
        while(n<len(self.working_urls)):
            if(n==0):
                string+=self.working_urls[n]
            else:
                string+=" " + self.working_urls[n]
            n+=1
            
        print(str(round((len(self.working_urls)/amount)*100,0)) + " % of suffixes are in use")
        results_file.write(string)
        results_file.close()
        
        input_value = input("Press Enter to quit")
        
    def check_this(self,url,ending):
        '''
        Checks one full url, for example www.google.com
        '''
        
        full_url= url + ending
        errors = False
        try:
            socket = http.client.HTTPConnection(full_url)
            socket.connect()
        except:
            errors = True
        
        if (errors == False):
            self.working_urls.append(full_url)
            #print("Found: " + full_url)
    
    def check_this_ping(self,url,ending):
        '''
        Checks one full url, for example www.google.com
        '''
        
        full_url= url + ending
        ping = os.popen("ping " +  full_url + " -n 1")
        result = ping.readlines()
        commandline = result[-1].strip()
        #print(commandline)
        if (commandline[0:7] == "Minimum"):
            self.working_urls.append(full_url)
            #print("found")
    
    def pull_and_parse(self):
        '''
        Generates a list of suffixes based on list on www.computerhope.com
        You only need to call this if the endings file is empty
        '''
        
        linecount=0
        endings=[]
        
        html_file, headers = urllib.request.urlretrieve('http://www.computerhope.com/jargon/num/domains.htm')
        html = open(html_file)
        for line in html:
            linecount+=1
            if(linecount>=63 and linecount<=69):
                for word in line.split("<td>"):
                    if(word[0:3]=="<b>"):
                        #print(word[3:word.index('/b')-1])
                        endings.append(word[3:word.index('/b')-1])
                        
        endings_file=open("endings.txt","r+")
        n=0
        string=""
        while(n<len(endings)):
            if(n==0):
                string+=endings[n]
            else:
                string+=" " + endings[n]
            n+=1
            
        #print(string)
        endings_file.write(string)
        endings_file.close()
    

checker()
        
        