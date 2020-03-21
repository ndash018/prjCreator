#prj Creator V 1.0 by NemerMore


import os
import shutil
import time


add = 1;


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def mainEditor():
	createFolder('../' + prj + '/ARTWORKS - MASTER/FROM AGENCY-CLIENT')
	createFolder('../' + prj + '/EXPORT/DATE')
	createFolder('../' + prj + '/EXPORT/FOR CG')
	createFolder('../' + prj + '/EXPORT/FOR GRADING')


	createFolder('../' + prj + '/MATS - MASTER/AUDIO/DATE')
	createFolder('../' + prj + '/MATS - MASTER/CONVERTED/DATE')
	createFolder('../' + prj + '/MATS - MASTER/GRADED/DATE')
	createFolder('../' + prj + '/MATS - MASTER/RAW')


	createFolder('../' + prj + '/PR')
	dest = '../' +  prj + '/PR/' + prj + '_001.prproj'
	shutil.copy2('./TEMPLATE/PR_TEMPLATE.prproj', dest )

	createFolder('../' + prj + '/RELEASE')


def addARTIST(p):
	print('Enter Artist Name')
	n = input()
	createFolder('../' + p + '/BACKROOM/' + n + '/3D/C4D')
	createFolder('../' + p + '/BACKROOM/' + n + '/3D/DL')
	createFolder('../' + p + '/BACKROOM/' + n + '/3D/MAYA')
	createFolder('../' + p + '/BACKROOM/' + n + '/3D/PLAYBLAST')
	createFolder('../' + p + '/BACKROOM/' + n + '/3D/FBX')
	
	createFolder('../' + p + '/BACKROOM/' + n + '/AE-FILES')
	dest = '../' + p + '/BACKROOM/' + n +'/AE-FILES/' + p + '-' + n + '_001.aep'
	shutil.copy2('./TEMPLATE/AE_TEMPLATE.aep', dest)

	createFolder('../' + p + '/BACKROOM/' + n + '/AE-RENDERS/PRE RENDER')
	createFolder('../' + p + '/BACKROOM/' + n + '/AE-RENDERS/IMG SEQUENCE')
	createFolder('../' + p + '/BACKROOM/' + n + '/AE-RENDERS/STILLS')
	createFolder('../' + p + '/BACKROOM/' + n + '/AE-RENDERS/DATE')

	createFolder('../' + p + '/BACKROOM/' + n + '/ARTWORKS/FROM CLIENT')


	createFolder( '../' + p + '/BACKROOM/' +  '/ONLINE_MATS/AUDIO')
	createFolder( '../' + p + '/BACKROOM/' +  '/ONLINE_MATS/CONVERTED')
	createFolder( '../' + p + '/BACKROOM/' +  '/ONLINE_MATS/GRADED')
	#createFolder( p + '/BACKROOM/' + n + '/MATS/CG RAW')
	#createFolder( p + '/BACKROOM/' + n + '/MATS/FOR CG')
	createFolder( '../' + p + '/BACKROOM/' +  '/ONLINE_MATS/OFFLINE')



print('Enter PROJECT NAME')
prj = input()
print('Are you the main Editor? Press [ Y ] to ADD, Press [ N ] to Exit ')
ME = input()

if( ME == 'Y'):
	mainEditor()

while True:
	addARTIST(prj)
	print('Add ARTIST? Press [ Y ] to ADD, Press [ N ] to Exit ')
	add = input()
	if( add == 'N'):
		break

print('Folders for Project ' + prj + 'has been Created')



	


# Creates a folder in the current directory called data