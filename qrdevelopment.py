# after installation
from MyQR import myqr

def makeCode(studentinformation, filename, savedir):
    version, level, qr_name = myqr.run(
    studentinformation,
    version=1,
    level='H',
    picture=None,
    colorized=False,
    contrast=1.0,
    brightness=1.0,
    save_name = filename,
    save_dir= savedir
    )

studentfile = open('mentorgroup.txt', 'r')

for line in studentfile:
    values = line.split()
    print(line, end='')
    #print(values[0], "   ", values[1], "   ", values[2])
    filename = values[0]+'.png'
    print(filename, end='')
    #filename = values[0] +'.png'
    #values[1] = str(values[1])
    studentinformation = values[0] +" " +values[1] +" "+values[2]
    
    #print(filename)
    #studentinformation = values[2] +' ' +values[0] +" " +values[1]
    #print(studentinformation)
    savedir = 'qrcodes'
    makeCode(studentinformation, filename, savedir)



studentfile.close()

