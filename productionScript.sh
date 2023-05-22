#!/bin/bash

mydir=/home/vboxuser/TestENvironment/ProtoReverser/nDPI/example

pcap=$1

cd $mydir
read -sn1 -p "|------------------------------|"; echo 
read -sn1 -p "|Этап 1 - фильтрация через ndpi|"; echo 
read -sn1 -p "|------------------------------|"; echo 


./ndpiReader -i $pcap
read -sn1 -p "|----------------------------|"; echo 
read -sn1 -p "|Этап 2 - проверка IP адресов|"; echo 
read -sn1 -p "|----------------------------|"; echo 

cd $HOME

#Загрузка json файла, содержащего IP адреса управляющих ботнет серверов
wget https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.json

read -sn1 -p "Press any key to continue..."; echo 

botnetIpList=$(readlink -f ipblocklist_recommended.json)

echo $botnetIpList

python botnetIpParser.py $pcap $botnetIpList
