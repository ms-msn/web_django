from blog.models import Hh_vacancy, Vacancy, Responsibility
from django.core.management.base import BaseCommand, CommandError

competences = ['OSI',
'TCP/IP', 'маршрутизация', 'коммутация', 'VPN', 'VLAN', 'DHCP','ESXi',
'AD', 'terminal services','Asterisk','CentOS',
'Hyper-V', 'администрирование IT-инфраструктуры','интернет', 'телефония',
'CRM','Администрирование сайтов','Postgresql', 'MS SQL','nix','Oracle', 'HP', 'Intel',
'GPO','DNS', 'RAID','Symantec Backup','Active Directory', 'Windows server',
'АТС','WI-FI','postfix', 'asterisk', 'iptables', 'samba', 'zabbix','Citrix XenApp', 'RouterOS','Cisco IOS','HelpDesk'
'Kaspersky']

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
            Responsibility.objects.create(
                vacancy_id=vac.vacancy_id,name_list=str(list_of_competences))
            print(list_of_competences)
            #print(vac.responsibility)

