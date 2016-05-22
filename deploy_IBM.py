import os
import yaml

def get_application_name():
    f = open('manifest.yml')
    data = yaml.load(f)
    f.close()
    return data['applications'][0]['name']

def install_ibm():
    print 'insatll CLI of Cloud fondry'
    os.system("curl -L 'https://cli.run.pivotal.io/stable?release=linux64-binary&source=github' | tar -zx")
    os.system("./cf --version")
    os.system("cf --version")

def deploy_ibm(path):

    #if not (app_name and path):
        #raise Exception('Entres le chemin et le nom de lapplication')



    print '=============debut de depoilment ============'
    print '==============authentification==============='
    os.chdir(path)
    os.system("pwd")
    get_application_name()
    os.system("cf login")
    os.system("cf push " + get_application_name())

if __name__ == '__main__':
    print 'voici c : {}'
    print 'Bienvenu sur IBMBLUEMIX CLOUD'
    print 'il faux suivre quelqu etape pour notre deploiment correctement'
    var = raw_input('est ce que tu est utliser heroku pour la premiere foix o/n: : ')
    var =str(var)

    if var == "o":
        print '=============debut de depoilment ============'
        print '==============authentification==============='
        r = raw_input('choisis le chemin de aplication: : ')
        r =str(r)
        #os.chdir("/home/kaddour/Bureau/n1/python-hello-world-flask")
        os.chdir(r)
        os.system("pwd")
        os.system("cf login")
        os.system("cf push python-hello-world-flask")
        os.system("")
    elif var == "n":
        print 'insatll CLI of Cloud fondry'
        os.system("curl -L 'https://cli.run.pivotal.io/stable?release=linux64-binary&source=github' | tar -zx")
        os.system("./cf --version")
        l = raw_input('choisis le chemin de aplication: : ')
        l =str(l)
        #os.chdir("/home/kaddour/Bureau/n1/python-hello-world-flask")
        os.chdir(l)
        os.system("pwd")
        os.system("cf login")
        os.system("cf push python-hello-world-flask")
        os.system("")
    else:
        print 'exit'

