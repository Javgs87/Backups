#!/usr/bin/env python

import getpass
import sys
import telnetlib

#Usuario y contraseña
user = raw_input("Ingresa tu usuario: ")
password = getpass.getpass()

#Abre el archivo donde estan todas las ips de los switches
f = open("lista_switches")

#Telnet a los equipos
for line in f:
        print "Obteniendo configuraciòn " + (line)
        HOST = line.strip()
        tn = telnetlib.Telnet(HOST)

        tn.read_until("Username: ")
        tn.write(user + "\n")

        if password:
                tn.read_unitl("Password: ")
                tn.write(password + "\n")

        tn.write("terminal length 0\n")
        tn.write("show run\n")
        tn.write("exit\n")

#Guardar configuración
readoutput = tn.read_all()
saveoutput = open("switch" + HOST, "w")
saveoutput.write(readoutput)
saveoutput.close
