from blog.models import Hh_vacancy, Vacancy, Responsibility
from django.core.management.base import BaseCommand, CommandError

competences = ['OSI',
'TCP/IP', 'маршрутизация', 'коммутация', 'VPN', 'VLAN', 'DHCP','ESXi',
'AD', 'terminal services','Asterisk','CentOS',
'Hyper-V', 'администрирование IT-инфраструктуры','интернет', 'телефония',
'CRM','Администрирование сайтов','Postgresql', 'MS SQL','nix','Oracle', 'HP', 'Intel',
'GPO','DNS', 'RAID','Symantec Backup','Active Directory', 'Windows server',
'АТС','WI-FI','postfix', 'asterisk', 'iptables', 'samba', 'zabbix','Citrix XenApp', 'RouterOS','Cisco IOS','HelpDesk'
'Kaspersky', 'Lun', 'Veeam', 'Acronis','MySQL','СУБД', 'SIP', 'Windows Server 2012', 'PKI','helpdesk','Организация рабочих мест',
 '1С: Предприятие 8', 'Unix', '1С','Windows 7','MS Server 2008 R2', 'Terminal server', 'Debian', 'Ubuntu','Asterisk',
 'Exim', 'Dovecot', 'Apache', 'Windows Server', ' VDI', 'Dell', 'СХД' , 'Windows Server 2008R2','SAN','NAS',
'FC', 'iSCSI', 'мониторинг', 'VMWare', 'vSphere', 'FTP', 'английский язык', 'Citrix', 'Cisco', 'Mikrotik',
'MS Exchange 2010', 'Exchange', 'Kerio', 'PRTG', 'Word', 'Excel', 'PowerPoint','Windows XP','Windows Server', 'File Server', 'Print Server',
'Nginx', 'Elasticsearch', 'Kibana', 'RabbitMQ', 'couchbase', 'Oracle DB', 'SQL', 'Zimbra', 'Bacula' , 'Windows 7',
 'Администрирование сетевого оборудования','Администрирование серверов Windows','Резервное копирование', 'высшее образование', 'WSUS',
 'HTML', 'CSS' , 'MsSQL', '1с' , 'MAC OS', 'MAC' ,'bitrix', 'apache' , 'IP телефония' , '1С-Битрикс' , 'PHP', 'IIS', 'WiFi',
 'виртуализация', 'squid', 'VOIP', 'MSSQL', 'RHEL', 'БД', 'MS Office' , 'TS', 'Техническая поддержка', 'Ремонт ПК','Администрирование сетевого оборудования',
 'Windows 10', '2008 R2', '2012', '2012 R2', '2016', 'TCPIP', 'SMTP', '802.1X', 'SMB', 'ICMP', 'RADIUS', 'CA', 'FS',
 'АТС Panasonic','vmware','hyper-v', 'Python', 'Bash', 'CI/CD','Bamboo', 'Jenkins', 'mongodb', 'influxdb',
 'continuous integration','continuous delevery''bitbucket','jira', 'Adobe Photoshop','Firewall','Kerio Control','Kerio Connect','IP АТС',
 'Windows', 'PS', 'VBS', 'bat','почтовые серверы','Администрирование серверов','СХД HP','jenkins', 'ЭЦП', 'СКЗИ', 'IP-АТС Yealink', 'TCP\IP',
 ' Windows', 'Office', 'Linux-администрирования', 'OS X', ' R-Keeper', 'КритоПро', 'RDP',
 'POS-терминалы', 'Контур', 'ЛВС', 'Microsoft SQL Server', 'Apple','Mac', 'Ipad', 'Iphone',
 'PostgreSQL','JS','Битрикс24', 'ITIL', 'Radius', 'DFS', 'Маршрутизаторы', 'управляемые коммутаторы', 'firewall',
 'Veem Backup', 'Acronis Backup Advanced','Администрирование сетевого оборудования', 'FreeBSD', 'CCNA', 'CENT',
 'MongoDB', 'PostgreSQL', 'ISA', 'антивирусная защита', 'MDaemon','SNMP', 'IMAP', 'TMG', 'TS', 'ts', 'MCSA', 'MCP', 'mcp', 'MCSE', 'CCNP',
 'dba', 'DBA', 'Английский язык', 'Cisco ASA','HPE', 'Asus','iscsi', 'DameWare', 'TeamViewer']

vendors_technologies = {'OSI': 9,
'TCP/IP': 9, 'маршрутизация' : 9, 'коммутация' : 9, 'VPN': 9, 'VLAN': 9, 'DHCP': 1,'ESXi': 6,
'AD': 1, 'terminal services': 1,'Asterisk':14,'CentOS': 8,
'Hyper-V': 1, 'администрирование IT-инфраструктуры': 1,'интернет': 9, 'телефония':,14
'CRM': 11,'Администрирование сайтов': 11,'Postgresql': 8, 'MS SQL': 2,'nix': 8,'Oracle': 26, 'HP': 20, 'Intel': 20,
'GPO': 1,'DNS': 1, 'RAID': 20,'Symantec Backup': 17,'Active Directory': 1, 'Windows server': 1,
'АТС': 14,'WI-FI': 9,'postfix': 8, 'asterisk': 14, 'iptables': 8, 'samba': 8, 'zabbix': 15,'Citrix XenApp': 7, 'RouterOS':10,'Cisco IOS': 9,'HelpDesk':21,
'Kaspersky': 23, 'Lun': 20, 'Veeam': 17, 'Acronis': 17,'MySQL': 8,'СУБД': 8, 'SIP':14, 'Windows Server 2012': 1, 'PKI': 1,'helpdesk': 21,'Организация рабочих мест': 21,
 '1С: Предприятие 8': 13, 'Unix': 8, '1С': 13,'Windows 7': 4,'MS Server 2008 R2':1, 'Terminal server': 1, 'Debian': 8, 'Ubuntu': 8,'Asterisk': 14,
 'Exim': 8, 'Dovecot': 8, 'Apache': 8, 'Windows Server': 1, ' VDI': 1, 'Dell': 20, 'СХД' : 20 , 'Windows Server 2008R2': 1,'SAN': 20,'NAS': 20,
'FC': 20, 'iSCSI':1, 'мониторинг':15, 'VMWare': 6, 'vSphere': 6, 'FTP': 8, 'английский язык':19, 'Citrix':7, 'Cisco':9, 'Mikrotik':10,
'MS Exchange 2010': 3, 'Exchange': 3, 'Kerio':25, 'PRTG':15, 'Word':4, 'Excel': 4, 'PowerPoint': 4,'Windows XP':4,'Windows Server':1, 'File Server':1, 'Print Server':1,
'Nginx':8, 'Elasticsearch':8, 'Kibana': 8, 'RabbitMQ':8, 'couchbase':8, 'Oracle DB':26, 'SQL':2, 'Zimbra':8, 'Bacula':8, 'Windows 7':4,
 'Администрирование сетевого оборудования':9,'Администрирование серверов Windows':1,'Резервное копирование':17, 'высшее образование':18, 'WSUS':1,
 'HTML':11, 'CSS':11 , 'MsSQL':8, '1с':13 , 'MAC OS':22, 'MAC':22 ,'bitrix':13, 'apache':8 , 'IP телефония':14 , '1С-Битрикс':13 , 'PHP':11, 'IIS':1, 'WiFi':9,
 'виртуализация': 1, 'squid':8, 'VOIP':14, 'MSSQL':2, 'RHEL':8, 'БД':2, 'MS Office':4 , 'TS':1, 'Техническая поддержка':21, 'Ремонт ПК':21,'Администрирование сетевого оборудования': 9,
 'Windows 10':4, '2008 R2':1, '2012':1, '2012 R2': 1, '2016': 1, 'TCPIP':9, 'SMTP':3, '802.1X':9, 'SMB':1, 'ICMP':9, 'RADIUS':9, 'CA':1, 'FS':1,
 'АТС Panasonic':14,'vmware':6,'hyper-v':1, 'Python':24, 'Bash':24, 'CI/CD':16,'Bamboo':16, 'Jenkins':16, 'mongodb':8, 'influxdb':8,
 'continuous integration':16,'continuous delevery':16,'bitbucket':16,'jira':16, 'Adobe Photoshop':27,'Firewall':9,'Kerio Control':25,'Kerio Connect':25,'IP АТС':14,
 'Windows': 4, 'PS':5, 'VBS':5, 'bat':5,'почтовые серверы':3,'Администрирование серверов':1,'СХД HP':20,'jenkins':16, 'ЭЦП':27, 'СКЗИ':27, 'IP-АТС Yealink':14, 'TCP\IP':9,
 ' Windows': 4, 'Office':4, 'Linux-администрирования':8, 'OS X':22, ' R-Keeper':27, 'КритоПро':27, 'RDP':1,
 'POS-терминалы':20, 'Контур':27, 'ЛВС':9, 'Microsoft SQL Server':2, 'Apple':22,'Mac':22, 'Ipad':22, 'Iphone':22,
 'PostgreSQL':8,'JS':11,'Битрикс24':13, 'ITIL':27, 'Radius':9, 'DFS':1, 'Маршрутизаторы':9, 'управляемые коммутаторы':9, 'firewall':9,
 'Veem Backup': 17, 'Acronis Backup Advanced':17,'Администрирование сетевого оборудования':9, 'FreeBSD':8, 'CCNA':9, 'CENT':9,
 'MongoDB':8, 'PostgreSQL':8, 'ISA':1, 'антивирусная защита':23, 'MDaemon':8,'SNMP':3, 'IMAP':3, 'TMG':1, 'TS':1, 'ts':1, 'MCSA':1, 'MCP':1, 'mcp':1, 'MCSE':1, 'CCNP':9,
 'dba':8, 'DBA':8, 'Английский язык':19, 'Cisco ASA':9,'HPE':20, 'Asus':20,'iscsi':1, 'DameWare':21, 'TeamViewer':21
    }

vendors_technologies_id = { 0: 'Test',
                         1 : 'MS SERVER',
                        2 : 'MS SQL',
                        3 : 'MS Exchange',
                        4 : 'MS Client',
                        4 : 'MS SC',
                        5 : 'MS Scripting',
                        6 : 'VMWare',
                        7 : 'Citrix'
                        8 : 'Linux and Nix',
                        9 : 'Network Cisco',
                        10: 'Network Microtik',
                        11: 'WEB',
                        12: 'Test',
                        13: '1C'
                        14: 'VOIP',
                        15: 'Monitoring',
                        16: 'CI/CD',
                        17: 'Backup',
                        18: 'Education',
                        19: 'Language',
                        20: 'Hardware',
                        21: 'Helpdesk',
                        22: 'Apple',
                        23: 'Antivirus',
                        24: 'Linux_Scripting',
                        25: 'Kerio',
                        26: 'Oracle',
                        27: 'Other' 
}

def count_v_t(ls):
    for competences in ls:
        vhozhdenie = []
        vhozhdenie.append(vendors_technologies[competences]) 
    for i in range(len(vendors_technologies_id))
        count = []
        count.append(vhozhdenie.count(i))
    return count

def list_v_t(count):
    str_v_t
    for i in range(len(vendors_technologies_id)):
        if count[i] != 0:
            st = vendors_technologies_id[i]+ ' ' + str(count[i])
            str_v_t.append(st)
    



class Command(BaseCommand):
    help = 'competences HH'

    def handle(self, *args, **options):
        for vac in Vacancy.objects.all():
            list_of_competences=[]
            print(vac.vacancy_id)
            for competences_in in competences:
                exist = competences_in in vac.responsibility
                if exist == True:
                    list_of_competences.append(competences_in)
            if not Responsibility.objects.filter(vacancy_id=vac.vacancy_id):
                Responsibility.objects.create(
                        vacancy_id=vac.vacancy_id,name_list=str(list_of_competences),
                        associated=str(list_v_t(count_v_t(list_of_competences))) )
                print(list_of_competences)
                #print(vac.responsibility)
            else:
                print(list_of_competences)
                Responsibility.objects.filter(vacancy_id=vac.vacancy_id).update(name_list=list_of_competences,associated=str(list_v_t(count_v_t(list_of_competences))))
