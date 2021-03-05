input("Script feito por Pato, aperte enter 6 vezes")
input("▄▄▄▄·  ▄· ▄▌   ▄▄▄· ▄▄▄· ▄▄▄▄▄▄      ")
input("▐█ ▀█▪▐█▪██▌  ▐█ ▄█▐█ ▀█ ▀•██ ▀ ▄█▀▄ ")
input("▐█▀▀█▄▐█▌▐█▪   ██▀·▄█▀▀█   ▐█.▪▐█▌.▐▌")
input("██▄▪▐█ ▐█▀·.  ▐█▪·•▐█▪ ▐▌  ▐█▌·▐█▌.▐▌")
input("·▀▀▀▀   ▀ •   .▀    ▀  ▀   ▀▀▀  ▀█▄▀▪")
input("    ATENÇAO, ESSE SCRIPT FOI FEITO PARA TESTAR SENHAS, NAO ME RESPONSABI.... AH TU JA SABE DESSA PORRA, aperte enter mais uma vez")
key=input("Digite uma senha para testar com no minimo 6 letras: ") 

Alfa2=('a','e', 'i', 'o', 'u', 'ba','be','bi','bo','bu','ca','ce','ci','co','cu','da','de','di','do','du','fa','fe','fi','fo','fu','ga','ge','gi','go','gu','ha','he','hi','ho','ia','ie','io','iu','hu','ja','je','ji','jo','ju','ka','ke','ki','ko','ku','la','le','li','lo','lu','ma','me','mi','mo','mu','na','ne','ni','no','nu','pa','pe','pi','po','pu','qu','ra','re','ri','ro','ru','sa','se','si','so','su','ta','te','ti','to','tu','va','ve','vi','vo','vu','wa','we','wi','wo','wu','xa','xe','xi','xo','xu','za','ze','zi','zo','zu', 'cha','che','chi','cho','chu','lha', 'lhe', 'lhi','lho', 'lhu', 'nha','nhe','nhi','nho','nhu','rra','rre','rri','rro','rru','ssa','sse','ssi','sso','ssu','qua','que','qui','quo','1','2','3','4','5','6','7'.'8','9','0',) 

Nums=list('0123456789')


for i1 in (Alfa2):
    for i2 in (Alfa2):
        for i3 in (Alfa2):
            y=(i1+i2+i3)
            print(y)
            if(y==key) :
                print('Encontrada')
                exit()
