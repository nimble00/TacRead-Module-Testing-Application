# -*- coding: utf-8 -*-
"""
Created on Mon june 12 17:22:41 2017

@author: DELL
"""
import serial
import datetime 
import time
import os ,csv
from time import gmtime, strftime

ser=serial.Serial("COM11", 115200)   ## change  "COM11"


M_id=raw_input("Enter Module ID:")
#print str(M_id)
                 
keys=[1,2,3,4,5,6,7,8,9,10]

def write_csv():
      global M_id
      showDate = strftime("%Y-%m-%d %H:%M:%S", time.localtime() ) 
      lbl_time=[showDate[0:10],showDate[10:-1]]      
      counter=0 # to check except condition (conti. except)
      filename_csv=str(M_id)+".csv" 
      path = str( os.getcwd() )
#      if not os.path.exists(path):
#            os.makedirs(path)
      try:
          with open(os.path.join(path, filename_csv), 'ab') as file:
               a = csv.writer(file)
               lbl=[str(M_id),'Success']
               a.writerow(lbl_time)
               a.writerow(lbl)
               
          counter=0     
      except IOError:
           tkMessageBox.showinfo("WARNING", "CSV file is open/close it. ") 
           counter+=1
           if counter==5:
               return
           write_csv()
           
              
def delete_key(num):
    global keys,empty
#    print int(num),'num to be  del'
    
    for i in range (0,len(keys)):
          if keys[i]==int(num):
              index=i
    try:
       del keys[index]
    except:
        pass

    if keys==[]:
        empty=True
        print 'Success'
        write_csv()
        
         


def cursor_keypressed():
    global keys
    a = datetime.datetime.now()
    receive_data()
    d=ser.inWaiting()
    while d==0:
        d=ser.inWaiting()
        b = datetime.datetime.now()
        c = b - a
        t= divmod(c.days * 86400 + c.seconds, 60)
        #print(t)
        tt=(t[0]*60+t[1])*1000#in milli
        #print(tt)
        if tt>2000:
#          print("...")
          cursor_keypressed()
#          break
    rd1=receive_data()
    
        #p rd=[]rint(rdd,":rdd")
   
    #rd==rdd[:-1]
    
    rd=rd1[0]
    #print(rd)
        
     
    #print[kd[0]]
    #print(rd[5],"\t",rd[6])
    if len(rd)==0:
        print("timeout")
        return 
    try:
        rd6=rd[6]
        rd5=rd[5]
    except:
        print 'Press again'
        cursor_keypressed()
    if rd[5]==hex(0x0):
        if rd[6]==hex(0x1):
            #print("D9: working")
            print(10)
            delete_key(10)
             
        elif rd[6]==hex(0x2):
            #print("D8: working")
            print(9)
            delete_key(9)
            
        elif rd[6]==hex(0x4):
            #print("D7: working")
            print(8)
            delete_key(8)
            
        elif rd[6]==hex(0x8):
            #print("D6: working")
            print(7)
            delete_key(7)
            
        elif rd[6]==hex(0x10):
            print(6)
            delete_key(6)
            
        elif rd[6]==hex(0x20):
            print(5)
            delete_key(5)
             
        elif rd[6]==hex(0x40):
            print(4)
            delete_key(4)
             
        elif rd[6]==hex(0x80):
            print(3)
            delete_key(3)
             
    elif rd[6]==hex(0x0):
        if rd[5]==hex(0x1):
            print(2)
            delete_key(2)
             
        elif rd[5]==hex(0x2):
            print(1)
            delete_key(1)
             
    else:
        pass
#        print("no response")
#    print keys,'keys'        
    cursor_keypressed()
    
def receive_data():
    
    d=ser.inWaiting()
    #print(d,'  :lth of rd')
    
    rd=[]
    for x in range(0,d) :
        c=ser.read( )
        rd.append(hex(ord(c)))
    #print(rd,'  :rd \n')
    #rd=rd.append(d)
    time.sleep(.2)
    return [rd];  


 
 
 

print("Press Cursor Key...")
cursor_keypressed()
ser.close()
 

 
 