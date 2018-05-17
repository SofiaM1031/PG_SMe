import pyautogui as pg
import webbrowser

counter = 0

firstQ = pg.confirm(text= "How do you want to socialize by not socializing?", title= "Anti-Social Social-Network", buttons=['Ordering Food', 'Social Media', 'Binge-Watching','Life Hacks'])
        ##counter += 1


if firstQ == "Ordering Food":
    OFq1 = pg.confirm(text= "How?", title= "Ordering Food", buttons= ['call','website', 'back'])

    if OFq1 == "call":
        pg.alert = ("hahaahhahah....as if....pfff extrovert alert")

    elif OFq1 == "website":
        OFq2 = pg.confirm(text= "What type of Food?", title= "Food", buttons= ["pizza", "Chicken Joes", "UBER EATS!!", "GrubHub"])

        if OFq2 == "pizza":
                webbrowser.open ("https://www.dominos.com/en/pages/order/#/locations/search/?type=Delivery")

        elif OFq2 == "Chicken Joes":
                 webbrowser.open ("https://www.chickenjoeschicken.com/")

        elif OFq2 == "UBER EATS!!":
                webbrowser.open ("https://www.ubereats.com/")

        elif OFq2 == "GrubHub":
                webbrowser.open ("https://www.grubhub.com/")
    

elif firstQ == "Social Media":
    OFq3 = pg.confirm(text= "Social Media?", title= "Social Media", buttons=["SnapChat", "Instagram","Facebook", "Twitter"])


#elif firstQ == "Binge-Watching":
    OFq


#elif firstQ == "Life Hacks":
