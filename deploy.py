import os


def install():
    print ("hi there, everyone!")
    print ("hi there, everyone!")
    print 'install pyhton'
    os.system("python --version")
    print 'now installe virtualenv'
    # os.system("pip install virtualenv")
    # os.system("sudo apt-get install python-pip")
    print "pour interface heroku"
    # os.system("heroku --version")

def deploy(path=None, git=None):

    if path != None:
        os.chdir(path)
        os.system("pwd")
        os.system("heroku login")
        os.system("heroku create")
        os.system("git push heroku master")
        os.system("heroku ps:scale web=1")
        os.system("heroku open")

    if git != None:
        github = 'git clone: ' + git
        os.system(github)
        os.chdir(path)
        os.system("heroku login")
        os.system("heroku create")
        os.system("git push heroku master")
        os.system("heroku ps:scale web=1")
        os.system("heroku open")

if __name__ == '__main__':
    # a = input("entrez votre nom : ")
    # a = str(a)
    # print 'Bienvenue {} dans notre script'.format(a)
    print 'Bienvenu sur Heroku Cloud  '
    print 'il faux suivre quelqu etape pour notre deploiment correctement'
    var = raw_input('est ce que tu est utliser heroku pour la premiere foix o/n: : ')
    var = str(var)

    if var == "o":
        print 'install pyhton'
        os.system("python --version")
        print 'now installe virtualenv'
        #os.system("pip install virtualenv")
        #os.system("sudo apt-get install python-pip")
        print "pour interface heroku"
        os.system("heroku --version")
        print "entre your authentification login and password"
        os.system("heroku login")
        print "now clone my project in git up "
        clone = raw_input('entrer le projet que voul vous clone : ')
        clone =str(clone)
        os.system(clone)
        #os.system("git clone https://github.com/heroku/python-getting-started.git")

        l = raw_input('entre le chemin de aplication: : ')
        l =str(l)
        #os.chdir("/home/kaddour/Bureau/n1/python-hello-world-flask")
        os.chdir(l)

        os.system("pwd")
        print "ton application  va deploi"
        os.system("heroku create")
        os.system("git push heroku master")
        os.system("heroku ps:scale web=1")
        os.system("heroku open")


    elif var == "n":
        input = raw_input('give a github repo')
        deploy(git=input)

    elif var == 'p':
        input = raw_input('give a path')
        deploy(path=input)
    else:
        print 'exit'



#os.system("heroku login")


