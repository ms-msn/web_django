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
 'виртуализация', 'squid', 'VOIP', 'MSSQL', 'RHEL', 'БД', 'MS Office' , 'TS', 'Техническая поддержка', 'Ремонт ПК','Аинистрирование сетевого оборудования',
 'Windows 10', '2008 R2', '2012', '2012 R2', '2016', 'TCPIP', 'SMTP', '802.1X', 'SMB', 'ICMP', 'RADIUS', 'CA', 'FS',
 'АТС Panasonic','vmware','hyper-v', 'Python', 'Bash', 'CI/CD','Bamboo', 'Jenkins', 'mongodb', 'influxdb',
 'continuous integration','continuous delevery''bitbucket','jira', 'Adobe Photoshop','Firewall','Kerio Control','Kerio Connect','IP АТС',
 'Windows', 'PS', 'VBS', 'bat','почтовые серверы','Администрирование серверов','СХД HP','jenkins', 'ЭЦП', 'СКЗИ', 'IP-АТС Yealink', 'TCP\IP',
 ' Windows', 'Office', 'Linux-администрирования', 'OS X', ' R-Keeper', 'КритоПро', 'RDP',
 'POS-терминалы', 'Контур', 'ЛВС', 'Microsoft SQL Server', 'Apple','Mac', 'Ipad', 'Iphone',
 'PostgreSQL','JS','Битрикс24', 'ITIL', 'Radius', 'DFS', 'Маршрутизаторы', 'управляемые коммутаторы', 'firewall',
 'Veem Backup', 'Acronis Backup Advanced','Администрирование сетевого оборудования', 'FreeBSD', 'CCNA',
 'MongoDB', 'PostgreSQL', 'ISA', 'антивирусная защита', 'MDaemon','SNMP', 'IMAP', 'TMG', 'TS', 'ts', 'MCSA', 'MCP', 'mcp', 'MCSE', 'CCNP',
 'dba', 'DBA', 'Английский язык', 'Cisco ASA','HPE', 'Asus','iscsi', 'DameWare', 'TeamViewer']

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
                        vacancy_id=vac.vacancy_id,name_list=str(list_of_competences))
                print(list_of_competences)
                #print(vac.responsibility)
            else:
                print(list_of_competences)
                Responsibility.objects.filter(vacancy_id=vac.vacancy_id).update(name_list=list_of_competences)
