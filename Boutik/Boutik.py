from random import choice
from GesyonFichye import cart
from GesyonFichye.cart import panye_acha, kalkile_prix_total
from GesyonFichye.products import afiche_Pwodwi








print("==================================================================\n")
print("BYENVINI SOU SIT BOUTIK PLIS")
print("-------------------------------------------------------------------\n")

while True:
    print("+++++++++++++++++++++++  Meni    +++++++++++++++++++++++++++++++")
    print("1.   chache pwodwi")
    print("2.   we panye ou a ak pri yo")
    print("3.   femen")
      
    choice=int(input("chwazi youn nana opsyon sa yo:    "))
    if choice == "1":
     afiche_Pwodwi()
       
       
    elif choice == "2":
     cart.panye_acha()
     tot=cart.kalkile_prix_total()
        
     print("kantite kob pwodwi ou gen nan panyew se: ", +tot, "gdes")
        
    elif choice == "3":
      print("Ou soti nan pwogram nan")
      break
     

    
    else:
     print("***********Opsyon pa valab*******************.")
   
print("*******************************************************")
