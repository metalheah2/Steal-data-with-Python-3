#Name:Copiar_archivos_automaticamente_Scrip_python
#Autor:Marco Jhoel Churata Torres
#Date:30-MARZO-2020

import glob  
import shutil 	
import os		

lista_archivos=glob.glob('E:/*.py')	

print(lista_archivos)			

numero=len(lista_archivos)	

data='G:/data.txt'

f=open(data,'w')

for valor in range (0,numero):	
	print(lista_archivos[valor])	
	shutil.copyfile(lista_archivos[valor],'G:/archivo'+str(valor))
	f.write(lista_archivos[valor]+'====>'+'G:/archivo'+str(valor)+'\n')
	
directorios1=glob.glob('E:/*')
cantidad=len(directorios1)


i=0

for valor in range (0,cantidad):
	buscar1=glob.glob(directorios1[valor]+'/*.py')
	
	for valor in range(0,len(buscar1)):
		i=i+1
		print(buscar1[valor])
		shutil.copyfile(buscar1[valor],'G:/archivo2'+str(i))
		f.write(buscar1[valor]+'====>'+'G:/archivos2'+str(i)+'\n')
	
	directorios2=glob.glob(directorios1[valor]+'/*')
	
	for valor in range(0,len(directorios2)):
		buscar2=glob.glob(directorios2[valor]+'/*.py')
		
		for valor in range(0,len(buscar2)):
			i=i+1
			print(buscar2[valor])
			shutil.copyfile(buscar2[valor],'G:archivos3'+str(i))
			f.write(buscar2[valor]+'===>'+'G:/archivos3'+str(i)+'\n')