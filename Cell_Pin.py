# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:56:28 2017

@author: DELL
"""
#
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 17:38:40 2017

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 16:45:02 2017

@author: DELL
"""
#from check_err import check_err
import time
import math
import sys
import tkMessageBox
import os
from time import gmtime, strftime

Port=None
ser=None
#echo_module=True
#echo_flag=None 
  
ACC_CMD=[2];
GDS=[7];
ST_CMD=[8];
SET_CURSOR_KEY_DATA_TIME=[0x10,0x10];
GET_FB_TIME_INFO=[11];
DISABLE_AUTO_REPLY=[13,1];
RESUME_CMD=[9];
SLV_ALW_ON = [15];
VER_CMD = [14];
DIAG_CMD=[2];
DIAG_MODE_ENABLE=[5,1];
DIAG_MODE_DISABLE=[5,1];
LATCH_ON=[5,2];
LATCH_OFF=[5,2];
ACC_ON=[5,3];
ACC_OFF=[5,4];
PEAK_POWER_CONSTANT=[5,5];
STEADY_POWER_CONSTANT=[5,6];
  
 # //ERROR PART CMD      
GET_ERROR_CMD=[3,0];
SLAVE_COMM_ERR =[3,1];
LATCH_ERR=[3,2];
SLAVE_ACC_FB_ERR=[3,4];
POWER_SURGE_ERR=[3,8];
OVER_TEMP_ERR=[3,10];
OVER_VOLT_ERR=[3,20];
DATA_INEGRITY_ERR=[3,40];#// The serial port
       
SOM=[0x80];
EOM=[0x81];
source_addr=[0x10]
       
som=[0x80];
eom=[0x81];

packet_A=[]
sd=[]
err_msg=[]
HCC_packet=[]
pat = True
mid = 'default'
HST_Version = []
   # cmd2=[0x80,0x0D,0x10,0x00,0x02,0x09 ,0x09,0x09,0x09,0x09,0x09,0x09,0x09,0x09,0x09,0x12,0x81] 
   # cmd1=[0x80,0x0D,0x10,0x02,0x02,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF ,0x10,0x81]
    #resume=[0x80,0x03,0x10,0x00,0x09,0x19,0x81]
   # lth=len(cmd2)
    #
   # ser.write(resume)
   # ser.write(cmd2)
 

    
    
def make_data(c,p):
     i=(c-1)
     temp_d=[0]*10
     num_pins=8
     for j in range(0,num_pins): 
       value=math.pow(2,j)
       if j==(p-1):
         temp_d[i]=int(value)
       
     print(temp_d,'   #temp_d') 
                      
     return temp_d

def send_data_basic(ser,host_addr,cmd,datap):
    global sd
    if datap==None:
        dlth=0
        sd=[]
        sd.extend(SOM)        
        if len(cmd)==1:
            sdlth=dlth+7
            dlth+=3
        elif len(cmd)==2:
            sdlth=dlth+8
            dlth+=4
#        sd.extend(SOM)
        sd.append(dlth)
        sd.extend(source_addr) # source_addr
        sd.append(host_addr)
        #print(sd)
        for i in range(0,len(cmd)):
           sd.append(cmd[i])
          
        chks=sd[2]
        for i in range(3,sdlth-2): #7=sdlth
           chks^=(sd[i])
        #print('chks:',chks)
        sd.append(chks)
        sd.extend(EOM)
         
        
        print sd,' send data basic'
        packet_A.append(sd)
        
        
        ser.write(sd)
#        #time.sleep(0.02)
#        rd=receive_data(ser)
#        print rd
#        while rd == []:
#            time.sleep(0.002)
#            rd=receive_data(ser)
#            print rd
#        rdd=rd[0]
#        HCC_packet=rd[0]
##        
##        try:
##           rd=receive_data(ser)[0]
##           HCC_packet=rd
##        except:
##            rd=[]
##            tkMessageBox.showwarning("WARNING", "receive_data null ")
##            ser.close()
##            return rd
#        if not sd==rdd:
#            msg='echo  Not  present'
#            print msg
##            tkMessageBox.showwarning("WARNING", msg)
##        else:
##            msg='echo present'
##            tkMessageBox.showwarning("WARNING", msg)
##        print msg
##        packet_A.append(msg)
##        print 'send_basic_done:sd:',sd
        return sd
    
    else:
        dlth=len(datap)
        sd=[]
        sd.extend(SOM)        
        if len(cmd)==1:
            sdlth=dlth+7
            dlth+=3
        elif len(cmd)==2:
            sdlth=dlth+8
            dlth+=4
#        sd.extend(SOM)
        sd.append(dlth)
        sd.extend(source_addr) # source_addr
        sd.append(host_addr)
        #print(sd)
        for i in range(0,len(cmd)):
           sd.append(cmd[i])
        sd.extend(datap)
        chks=sd[2]
        for i in range(3,sdlth-2): #7=sdlth
           chks^=(sd[i])
        #print('chks:',chks)
        sd.append(chks)
        sd.extend(EOM)
         
        
        print sd,' send_data_basic'
        packet_A.append(sd)
        ser.write(sd)
#        #time.sleep(0.015 )
#        rd=receive_data(ser)
#        print rd
#        while rd == []:
#            time.sleep(0.002)
#            rd=receive_data(ser)
#            print rd
#
#        rdd=rd[0]
#        HCC_packet=rd[0]
##        try:
##           rd=receive_data(ser)[0]
##           HCC_packet=rd
##        except:
##            tkMessageBox.showwarning("WARNING", "receive_data null ")
##            rd=[]
##            ser.close()
##            return rd
#        if not sd==rdd:
#            msg='echo  Not  present'
#            print msg
#            #tkMessageBox.showwarning("WARNING", msg)
##        else:
##            msg='echo present'
###            tkMessageBox.showwarning("WARNING", msg)
##        print msg
##        packet_A.append(msg)
##        print 'send_basic_done:sd:',sd
        return sd

def send_data_basic_HCC(ser,host_addr,cmd,datap):
    global HCC_packet
    sd=[]
    if datap==None:
        dlth=0
        sd=[]
        sd.extend(SOM)        
        if len(cmd)==1:
            sdlth=dlth+7
            dlth+=3
        elif len(cmd)==2:
            sdlth=dlth+8
            dlth+=4
#        sd.extend(SOM)
        sd.append(dlth)
        sd.extend(source_addr) # source_addr
        sd.append(host_addr)
        #print(sd)
        for i in range(0,len(cmd)):
           sd.append(cmd[i])
          
        chks=sd[2]
        for i in range(3,sdlth-2): #7=sdlth
           chks^=(sd[i])
        #print('chks:',chks)
        sd.append(chks)
        sd.extend(EOM)
         
        
#        print sd,' send data basic'
        packet_A.append(sd)
        
        
        ser.write(sd)
        time.sleep(0.03)
        try:
           rd=receive_data_HCC(ser)[0]
           HCC_packet=rd
        except:
            rd=[]
#            tkMessageBox.showwarning("WARNING", "receive_data null ")
            ser.close()
            return rd
        if not sd==rd:
            msg='echo  Not  present HCC'
            print msg
            #tkMessageBox.showwarning("WARNING", msg)
#        else:
#            msg='echo present'
#            tkMessageBox.showwarning("WARNING", msg)
#        print msg
#        packet_A.append(msg)
#        print 'send_basic_done:sd:',sd
        return sd
    
    else:
        dlth=len(datap)
        sd=[]
        sd.extend(SOM)        
        if len(cmd)==1:
            sdlth=dlth+7
            dlth+=3
        elif len(cmd)==2:
            sdlth=dlth+8
            dlth+=4
#        sd.extend(SOM)
        sd.append(dlth)
        sd.extend(source_addr) # source_addr
        sd.append(host_addr)
        #print(sd)
        for i in range(0,len(cmd)):
           sd.append(cmd[i])
        sd.extend(datap)
        chks=sd[2]
        for i in range(3,sdlth-2): #7=sdlth
           chks^=(sd[i])
        #print('chks:',chks)
        sd.append(chks)
        sd.extend(EOM)
         
        
#        print sd,' send_data_basic'
        packet_A.append(sd)
        ser.write(sd)
        time.sleep(0.03)
        try:
           rd=receive_data_HCC(ser)[0]
           HCC_packet=rd
        except:
#            tkMessageBox.showwarning("WARNING", "receive_data null ")
            rd=[]
            ser.close()
            return rd
        if not sd==rd:
            msg='echo  Not  present HCC'
            print msg
            #tkMessageBox.showwarning("WARNING", msg)
#        else:
#            msg='echo present'
##            tkMessageBox.showwarning("WARNING", msg)
#        print msg
#        packet_A.append(msg)
#        print 'send_basic_done:sd:',sd
        return sd    
    
def send_ZERO(ser,host_addr,cmd):
    global sd
    datap=[0]*10
    
#    resume(ser,host_addr)
##    receive_data(ser)
#    ser.flushInput()
    
    sd=send_data_basic(ser,host_addr,cmd,datap)
#    print 'all zero sent'
#    receive_data(ser)
    
    return sd


def parser(rd):
    global sd,HST_Version
    #msg=None
#    print rd,'rd in parser'
#    print 'in parser_func: '+str(rd)
    if len(rd)==0:
        msg="'receive_data Null'"
        print msg
        return msg
    
    
#    elif rd==sd:
#        msg="echo "
#        print msg+'in parser(send_data_basic)'
#        return msg
    if rd[2] == 255:
        msg = '********************************DEBUG DATA : ' + str(rd[3])
        print msg
        return msg
    elif rd[2]==16:
         if rd[4]==2:
              msg=':Actuation_cmd'
#              print msg
              return msg
         if rd[4]==9:
              msg=':Resumed'
              print msg
              return msg
         if rd[4]==11:
              msg=':Get FB_Time'
              print msg
              return msg
         if rd[4]==14:
              msg=':GET_Version'
              print msg
              return msg
         if rd[4]==15:
              msg=':PWR_Always_on'
              print msg
              return msg  
    elif rd[3]==16:
        #device status
        if rd[4]==7:
            if rd[5]==1:
              msg='INIT / Initialize phase where self test is not complete'
              return msg
            elif rd[5]==2:
              msg='READY / Ready to receive data'
              return msg
            elif rd[5]==4:
              msg='BUSY / HOST is in actuation cycle'
              return msg
            elif rd[5]==8:
              msg='ERROR / Stuck in comm. or latch error'
              return msg
            elif rd[5]==16:
              msg='SELF_TEST RESULT(PASS/FAIL)'
              return msg

        #success info
        if rd[4]==4 or 20:
          if rd[6]==129:
              msg='Success information'
              print msg
              return msg
        if rd[4]==15:
          if rd[6]==129:
              msg='Always on'
              print msg
              return msg
        if rd[4]==14:
          HST_Version = hex(rd[5]);
          msg='Version : ' + str(HST_Version)
#          tkMessageBox.showwarning("WARNING", 'Version : ' + str(HST_Version))
          print msg
          return msg
          
        if rd[4]==11:
              msg='Feedback Time Info'
              print msg
              return msg
          
          # errors
        if rd[4]==3: 
            if rd[5]==4:
                msg='Slave Actuation_FB error'
#                tkMessageBox.showwarning("WARNING", msg) ##continue prog. on this error
                return msg
            if rd[5]==8:
                msg='Power Surge Error'
                return msg 
            if rd[5]==32:
                msg='OVER Voltage Error'
                return msg
            if rd[5]==64:
                msg='DATA Integrity Error'
                return msg    
            
        # log & stop errors
        if rd[4]==19:
            if rd[5]==1:
                x=rd[6]
                print x,str('rd[6]')
                y=bin(x)[2:].zfill(4)
                print y
                z=[]
                for i in range(0,len(y)):
                        k=int(y[i])
                        if k==1:
                          z.append(i+1)        
#                print  z,' :missing slaves'
                msg='slave communication error. '+'list of missing slaves '+str(z)
                print msg
                err_msg.append(msg)
#                tkMessageBox.showwarning("WARNING", msg)
                return msg
            
            if rd[5]==2:
                if rd[6]&0x01:
                    msg='Character Latch error'
#                    tkMessageBox.showwarning("WARNING", msg)
                if rd[6]&0x02:
                    msg='Cursor Latch error'
#                    tkMessageBox.showwarning("WARNING", msg)                
                if rd[6]==3:
                    msg='Both(Char&Cursor) Latch error'
                if rd[6]==16:
                    msg='Character Latch Default Feedback'
#                    tkMessageBox.showwarning("WARNING", msg)
                if rd[6]==32:
                    msg='Cursor Latch Default Feedback'
#                    tkMessageBox.showwarning("WARNING", msg)                
                if rd[6]==48:
                    msg='Both(Char&Cursor) Default Feedback'
#                    tkMessageBox.showwarning("WARNING", msg)
                if rd[6] == 0:
                    msg = 'Latch Error'
                print msg  
                err_msg.append(msg)
                return msg
            
 
            if rd[5]==16:
                msg=='OVER Temperature error'
                err_msg.append(msg)
                return msg
 

    else:
         msg='Unknown packet :-< '+str(rd)
         print msg
         return msg


def log(str_type):#1.(*) #2.(-)
      global cycle_var
      showDate = strftime("%Y-%m-%d %H:%M:%S", time.localtime() ) 
      filename_csv=str(mid)+".log" 
      path = str( os.getcwd() ) + "\\Test_Results\\"
      if not os.path.exists(path):
            os.makedirs(path)
            
      if type(str_type)==int:  #is cycle
        try:
          with open(os.path.join(path, filename_csv), 'ab') as log:
               
               lbl='Time : '+showDate[0:10]+showDate[10:-1] +'--  Error :'+str_type
               log.write(lbl)
               return
        except IOError:
               tkMessageBox.showinfo("WARNING", "CSV file is open/close it. ")
               return


def make_packets(rd):
    rd_packets=[]
    som=0
    eom=0
    if len(rd)==0:
         return rd
    while 1:
        try:
            
            lth=rd[som+1]
#            print 'lth:',lth
#            print som,'som sum'
            eom=som+lth+3
#            print 'eom',eom
            packet=rd[som:eom+1]
#            print packet,' packet'
            rd_packets.append(packet) 
            
            som=eom+1
#            print som,'som'
            
#            break
        except IndexError:
              break
    return rd_packets   
        


def receive_data(ser):
    global sd
#    ser.close()
    
 
    try:
        d=ser.inWaiting()
#      ser.flushInput()
        print "data length in input buffer:--------",d
    except:
      tkMessageBox.showwarning("WARNING", 'Select proper Port/ Check Power Supply')  
    #print(d,'  :lth of rd')
    
#    i=0
    rd=[]
    while True:
#        i+=1
        
        c=ser.read(d)
#        if len(c)==0:
#            break
        for item in c:
            rd.append(int(ord(item)))
        
        time.sleep(0.01)
        d=ser.inWaiting()
        if d==0:
            break
#        print " attempt no"+str(i)+"  -----------d :",d
    print(rd,'  :rd_raw in receive data \n')
#    if not rd==[]:
#        packet_A.append(rd)
    
    rd_packets=make_packets(rd)
#    if rd_packets[0]==sd:
#        rd_packets.remove(rd_packets[0])
#        print "removing echo"
#    print rd_packets, 'rd_packets after make packet'
    
    for i in range(0,len(rd_packets)):
        if rd_packets[i]==sd:
            k=i
            
        else:    
            packet_A.append(rd_packets[i])
            msg=parser(rd_packets[i])
            packet_A.append(msg)
       # log(msg)
          
    try:
            print "removing echo:  "+str(rd_packets[k])
            rd_packets.remove(rd_packets[k])
            
    except Exception as e:
                 exc_type, exc_obj, exc_tb = sys.exc_info()
#                 filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                 print(exc_type, exc_tb.tb_lineno)
                 return None     
#    print rd_packets, 'rd_packets after removing echo'        
    return rd_packets


def receive_data_HCC(ser):
    try:
      d=ser.inWaiting()
    except:
      tkMessageBox.showwarning("WARNING", 'Select proper Port/ Check Power Supply')  
    #print(d,'  :lth of rd')
    
    rd=[]
    for x in range(0,d) :
        c=ser.read( )
        rd.append(int(ord(c)))
#    print(rd,'  :rd_raw in receive data \n')
    #ser.flushInput()
    
#    if not rd==[]:
#        packet_A.append(rd)
    
    rd_packets=make_packets(rd)
#    print rd_packets, 'rd_packets after make packet'
    
    for i in range(0,len(rd_packets)):
        packet_A.append(rd_packets[i])
        
        msg=parser(rd_packets[i])
        packet_A.append(msg)
          
    return rd_packets

def parse_data(ser,rd):
    if len(rd)==0:
        return False
    if len(rd)>4:
         if rd[3]==6 :   #bogus host_addr
           return True 
         else:
             return False
    else:
        return False
    

def send_data(ser,host_addr,cmd,cell_no,Data):
    #p=PIN
    global sd
    sd=send_ZERO(ser,host_addr,cmd)
    c=cell_no
    datap=[0]*10
    datap[c-1]=Data
    #print datap,'datap'
    #datap=make_data(c,p)
#    print datap,': datapM'
    
    resume(ser,host_addr)
#    receive_data(ser)
    ser.flushInput()
    
    sd=send_data_basic(ser,host_addr,cmd,datap)

def send_data_1(ser,host_addr,cmd,datap):
    #p=PIN
    global packet_A,sd
    dat=None;
    sd=send_data_basic(ser,host_addr,SLV_ALW_ON,dat)
    print '--ALWAYS_ON__'
   # time.sleep(.05)
    if pat == False:
        send_ZERO(ser,host_addr,cmd)
        time.sleep(.3)
        receive_data(ser)    
        print 's.d.1 send_zero done'
    resume(ser,host_addr)
    time.sleep(0.02)
    ser.flushInput()
    print 'flushed'
    
    sd=send_data_basic(ser,host_addr,cmd,datap)
    print '__Acctuated'
    time.sleep(.5)#.5
    rd_packets=receive_data(ser)
    print 'here'


    return  [True,packet_A]
    
def HC_CHECK(ser,host_addr,cmd,datap):
    global HCC_packet
    
    datap=[0]*10
    rd=send_data_basic_HCC(ser,host_addr,cmd,datap)
    if rd==[]:
        HCC_flag=False
        return HCC_flag
    
    try:    
       HCC_flag=parse_data(ser,HCC_packet)
    except:
       print 'power or connections'
       HCC_flag=False
#    print HCC_flag,':hcc_flag'
    return  HCC_flag
 

    
def resume(ser,host_addr):
    global sd
    datap=None
    sd=send_data_basic(ser,host_addr,RESUME_CMD,datap)
    print(' __resumed__')
    return 

def parse_fb_time(rd_packets):
    start_points=[]
    lth_list=[]
    cmd=[]
 
    for i in range(0,len(rd_packets)):
                cmd.append(rd_packets[i][4])
                lth_list.append(rd_packets[i][1])
            
#    print lth_list,'lth_list'
#    print cmd,'cmd'
    
    fb_packets=[]
#    print lth_list,':  lth_list fb '
    for i in range(0,len(rd_packets)):
           if  cmd[i]==11:
              fb_packets.append(rd_packets[i][lth_list[i]+1:5:-1])
    return fb_packets      
    

def GetFB_time(ser,host_addr):
    global packet_A,sd
    packet_A=[]
    datap=None
    sd=send_data_basic(ser,host_addr,GET_FB_TIME_INFO,datap)
    print 'sent getFBtime'
    time.sleep(.1)
#    print "sd in fb get :   ",sd
    rd_packets=receive_data(ser)

#    print rd_packets,'rd_ad'
    if len(rd_packets)<4:
        fb=[]
        print 'rd_packets len smaller than 4'
        return [fb,packet_A]    
#    print rd_packets ,'  :rd_packet before parse_fb_time '
    
    
    fb_packets=parse_fb_time(rd_packets)
#    print fb_packets ,'  :fb_packet  :after parse_fb_time '


    sd1=fb_packets[0]     #7th in start and 3rd from the last 
    sd2=fb_packets[1]
    sd3=fb_packets[2]
    sd4=fb_packets[3]
    fb=sd1+sd2+sd3+sd4
#    print fb ,' :after arranging gfb'
    return [fb,packet_A]

def get_version(ser,host_addr):
    global HST_Version
    send_data_basic(ser,host_addr,VER_CMD,None)
    rd_packets=receive_data(ser)

    
    
"""
    try:
      d=ser.inWaiting()
#      ser.flushInput()
    except:
      tkMessageBox.showwarning("WARNING", 'Select proper Port/ Check Power Supply')  
    #print(d,'  :lth of rd')
    
    rd=[]
    while d>0:
        print "data length in input buffer:--------",d
        for x in range(0,d) :
            c=ser.read( )
            rd.append(int(ord(c)))
#        print "flushed data: -----------",ser.flushInput()
        print(rd,'  :rd_raw in receive data \n')
        d=ser.inWaiting()
        print "2nd attempt d ----------- :",d

"""
"""
    i=0
    rd=[]
    while True:
        i+=1
        print "data length in input buffer:--------",d
        c=ser.read(d)
        for item in c:
            rd.append(int(ord(item)))
#        print "flushed data: -----------",ser.flushInput()
        
        time.sleep(0.01)
        d=ser.inWaiting()
        print " attempt no"+str(i)+"  -----------d :",d
     print(rd,'  :rd_raw in receive data \n')
"""     
   
