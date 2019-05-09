from piwebenum import *
from grabhead import *
from httpmethods import *
from robot import *
from apachestat import *
from dav import *
from sharedns import *
from commentssrc import *
from sslcert import *
from filebrute import *
from traceroute import *
from phpinfo import *
from cms import *
from serverdetect import *
from altsites import *
from core.Footprinting.Active_Recon.activeban import *
from core.Core.colors import *

def activeo(web):

    print(" [!] Module Selected : Active Reconnaissance\n\n")
    activeban()
    print('')
    time.sleep(0.3)
    v = raw_input (''+GR+'  [#] \033[1;4mTID\033[0m'+GR+' :> ' + color.END)
    print('')
    if v.strip() == '1':
        print(C+' [!] Type Selected : Ping/NPing Enumeration')
        piwebenum(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '2':
        print(C+' [!] Type Selected : Grab HTTP Headers')
        grabhead(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '3':
        print(C+' [!] Type Selected : HTTP Allowed Methods')
        httpmethods(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '4':
        print(C+' [!] Type Selected : robots.txt and sitemap.xml Hunt')
        robot(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '5':
        print(C+' [!] Type Selected : Scrape Comments')
        commentssrc(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '6':
        print(C+' [!] Type Selected '+B+': Traceroute')
        traceroute(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '7':
        print(C+' [!] Type Selected : DNS Hosts')
        sharedns(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '8':
        print(C+' [!] Type Selected : SSL Certificate')
        sslcert(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '9':
        print(C+' [!] Type Selected : CMS Detection')
        cms(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '10':
        print(C+' [!] Type Selected : Apache Status')
        apachestat(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '11':
        print(C+' [!] Type Selected : WebDAV HTTP Enumeration')
        dav(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '12':
        print(C+' [!] Type Selected : PHPInfo Enumeration')
        phpinfo(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '13':
        print(C+' [!] Type Selected : Server Detection')
        serverdetect(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '14':
        print(C+' [!] Type Selected : Alternate Sites ')
        altsites(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)

    elif v.strip() == '15':
        print(C+' [!] Type Selected : File Bruteforcers')
        filebrute(web)
        print('\n\n')
        raw_input(O+' [#] Press '+GR+'Enter'+O+' to continue...')
        activeo(web)