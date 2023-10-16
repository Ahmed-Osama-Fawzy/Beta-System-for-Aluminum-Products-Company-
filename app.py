from flask import Flask,render_template,request
import sqlite3
#import webview
import os
import traceback
import sys

###################################################################################################################################################
# System Database Section #
###################################################################################################################################################

db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
cr = db.cursor()
cr.execute(f"CREATE TABLE IF NOT EXISTS Clients(Date DATE , Name TEXT , Id INTEGER , Address TEXT, Mobile INTEGER , Location TEXT , NumberOfWorks INTEGER)")
cr.execute(f"CREATE TABLE IF NOT EXISTS Works(Date DATE , CName TEXT , CId INTEGER , WId INTEGER , Address TEXT, Location TEXT , Drive TEXT , Type TEXT , INMoney INTEGER , OUTMoney INTEGER , TOTALMoney INTEGER , Rest INTEGER GENERATED ALWAYS AS (TOTALMoney-INMoney) VIRTUAL , Profits INTEGER GENERATED ALWAYS AS (INMoney-OUTMoney) VIRTUAL)")
cr.execute(f"CREATE TABLE IF NOT EXISTS Marchants(Date DATE , Name TEXT , Id INTEGER , Location TEXT , Mobile INTEGER , Address TEXT , Type TEXT , TotalMoney INTEGER)")
cr.execute(f"CREATE TABLE IF NOT EXISTS Cars(Date DATE , Id INTEGER , Number INTEGER , Chars TEXT  , Color TEXT , Type TEXT ,  Shape TEXT  , Input INTEGER , Output INTEGER , Rest INTEGER GENERATED ALWAYS AS (Input-Output) VIRTUAL)")
cr.execute(f"CREATE TABLE IF NOT EXISTS Workers(Date DATE , Name TEXT , Id INTEGER , Mobile INTEGER , Location TEXT  , Address TEXT , WType TEXT , SType TEXT , PerDay INTEGER , CardNumber INTEGER , DaysNumber INTEGER , Get INTEGER , Discounts INTEGER ,  Need INTEGER GENERATED ALWAYS AS ((PerDay*DaysNumber)-Get-Discounts) VIRTUAL)")
cr.execute(f"CREATE TABLE IF NOT EXISTS Rents(Date DATE , Amount INTEGER , Month INTEGER)")
cr.execute(f"CREATE TABLE IF NOT EXISTS GovernPayments(Date DATE , Amount INTEGER , Type TEXT)")
cr.execute(f"CREATE TABLE IF NOT EXISTS Payments(Date DATE , Amount INTEGER , For TEXT)")
cr.execute(f"CREATE TABLE IF NOT EXISTS HRents(Date DATE , Amount INTEGER , Month INTEGER)")
cr.execute(f"CREATE TABLE IF NOT EXISTS HGovernPayments(Date DATE , Amount INTEGER , Type TEXT)")
cr.execute(f"CREATE TABLE IF NOT EXISTS HSchoolPayments(Date DATE , Amount INTEGER , Type TEXT)")
cr.execute(f"CREATE TABLE IF NOT EXISTS HPayments(Date DATE , Amount INTEGER , For TEXT)")
cr.execute(f"CREATE TABLE IF NOT EXISTS Passwords(Password INTEGER , Name TEXT)")
cr.execute(f"CREATE TABLE IF NOT EXISTS Specifications(WId INTEGER , CId INTEGER , CName TEXT , WName TEXT , CNClient INTEGER , CNWorker INTEGER , MOClient INTEGER , MOWorker INTEGER , ADClient  TEXT , ADWorker TEXT , PRType TEXT , PRColor TEXT , PRShape TEXT , GRAType TEXT , GRAColor TEXT , WIRType TEXT , WIRColor TEXT , GLAType TEXT , GLAColor TEXT , GLAShape TEXT , FIPType TEXT , FIPColor TEXT , DOORType TEXT , DOORShape TEXT , ADDT TEXT , FAREA INTEGER , OMPrice INTEGER , FAREAPrice INTEGER , ADDTPrice INTEGER , TRAPrice INTEGER , FULLPrice INTEGER , FBATDate DATE , SBATDate DATE , TBATDate DATE , FBATAmount INTEGER , SBATAmount INTEGER , TBATAmount INTEGER , DELDate DATE , GIVDate DATE , GIVPostion TEXT )")
db.close()

###################################################################################################################################################
# Prices DataBase Section #
###################################################################################################################################################

db2 = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
cr2 = db2.cursor()
cr2.execute(f"CREATE TABLE IF NOT EXISTS Granium(Date DATE , Id TEXT , Price INTEGER , Color TEXT , Notes TEXT)")
cr2.execute(f"CREATE TABLE IF NOT EXISTS GarniumAddtions(Date DATE , Id TEXT , Price INTEGER , TheAddtion TEXT , Notes TEXT)")
cr2.execute(f"CREATE TABLE IF NOT EXISTS Glass(Date DATE , Id TEXT , Price INTEGER , MainPrice INTEGER , Color TEXT , Notes TEXT)")
cr2.execute(f"CREATE TABLE IF NOT EXISTS GlassAddtions(Date DATE , Id TEXT , Price INTEGER , TheAddtion TEXT , Notes TEXT)")
cr2.execute(f"CREATE TABLE IF NOT EXISTS Fibr(Date DATE , Id TEXT , Price INTEGER , Type TEXT , Notes TEXT)")
cr2.execute(f"CREATE TABLE IF NOT EXISTS ShutersMachines(Date DATE , Id TEXT , Price INTEGER , Type TEXT , Shape TEXT , Notes TEXT)")
cr2.execute(f"CREATE TABLE IF NOT EXISTS Addtions(Date DATE , Id TEXT , Price INTEGER , Type TEXT , Name TEXT , Section TEXT , Notes TEXT)")
cr2.execute(f"CREATE TABLE IF NOT EXISTS Windows(Date DATE , Id TEXT , Price INTEGER , Type TEXT , Shape TEXT , Spec TEXT ,  Notes TEXT )")
cr2.execute(f"CREATE TABLE IF NOT EXISTS Doors(Date DATE , Id TEXT , Price INTEGER , Type TEXT , Shape TEXT , Spec TEXT  , Notes TEXT)")
cr2.execute(f"CREATE TABLE IF NOT EXISTS Kitchens(Date DATE , Id TEXT , Price INTEGER , Type TEXT , Shape TEXT , Spec TEXT  , Notes TEXT )")
cr2.execute(f"CREATE TABLE IF NOT EXISTS Wires(Date DATE , Id TEXT , Price INTEGER , Type TEXT , Color TEXT , Shape TEXT , Spec TEXT , Notes TEXT )")
cr2.execute(f"CREATE TABLE IF NOT EXISTS Covers(Date DATE , Id TEXT , Price INTEGER , Type TEXT , Color TEXT , Spec TEXT  , Notes TEXT)")
cr2.execute(f"CREATE TABLE IF NOT EXISTS Shuters(Date DATE , Id TEXT , Price INTEGER , Type TEXT , Color TEXT  , Spec TEXT  , Notes TEXT )")
db2.close()

###################################################################################################################################################
# Applaction Section #
###################################################################################################################################################

app = Flask(__name__)
TheFullComapnyName = "الإسراء لأعمال الالوميتال"
heCompanyShortName= "الإسراء"
#window = webview.create_window("Elesraa" , app)

###################################################################################################################################################
# Specifications Section #
###################################################################################################################################################

@app.route('/Add_Specifications' , methods=['GET', 'POST'])
def Add_Specifications(): 
    if request.method == "POST":
        try:
            WId = request.form.get("WId")
            CId = request.form.get("CId")
            CName = request.form.get("CName")
            WName = request.form.get("WName")
            CNClient = request.form.get("CNClient")
            CNWorker = request.form.get("CNWorker")
            MOClient = request.form.get("MOClient")
            MOWorker = request.form.get("MOWorker")
            ADClient = request.form.get("ADClient")
            ADWorker = request.form.get("ADWorker")
            PRType = request.form.get("PRType")
            PRColor = request.form.get("PRColor")
            PRShape = request.form.get("PRShape")
            GRAType = request.form.get("GRAType")
            GRAColor = request.form.get("GRAColor")
            WIRType = request.form.get("WIRType")
            WIRColor = request.form.get("WIRColor")
            GLAColor = request.form.get("GLAColor")
            GLAShape = request.form.get("GLAShape")
            GLAType = request.form.get("GLAType")
            FIPType = request.form.get("FIPType")
            FIPColor = request.form.get("FIPColor")
            DOORType = request.form.get("DOORType")
            DOORShape = request.form.get("DOORShape")
            ADDT = request.form.get("ADDT")
            #listToStr = ' '.join([str(elem) for elem in ADDT])
            FAREA = request.form.get("FAREA")
            OMPrice = request.form.get("OMPrice")
            FAREAPrice = request.form.get("FAREAPrice")
            ADDTPrice = request.form.get("ADDTPrice")
            TRAPrice = request.form.get("TRAPrice")
            FULLPrice = request.form.get("FULLPrice")
            FBATDate = request.form.get("FBATDate")
            SBATDate = request.form.get("SBATDate")
            TBATDate = request.form.get("TBATDate")
            FBATAmount = request.form.get("FBATAmount")
            SBATAmount = request.form.get("SBATAmount")
            TBATAmount = request.form.get("TBATAmount")
            DELDate = request.form.get("DELDate")
            GIVDate = request.form.get("GIVDate")
            GIVPostion = request.form.get("GIVPostion")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO Specifications VALUES({WId} , {CId} ,'{CName}','{WName}',{CNClient},{CNWorker},{MOClient},{MOWorker},'{ADClient}','{ADWorker}','{PRType}','{PRColor}','{PRShape}','{GRAType}','{GRAColor}','{WIRType}','{WIRColor}','{GLAType}','{GLAColor}','{GLAShape}','{FIPType}','{FIPColor}','{DOORType}','{DOORShape}','{ADDT}',{FAREA},{OMPrice},{FAREAPrice},{ADDTPrice},{TRAPrice},{FULLPrice},'{FBATDate}','{SBATDate}','{TBATDate}',{FBATAmount},{SBATAmount},{TBATAmount},'{DELDate}','{GIVDate}','{GIVPostion}')")
                con.commit() 
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        finally:
            con.close()
    return render_template('Specifications.html' ,  title="Specifications" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Modify_Specifications' , methods=['GET', 'POST'])
def Modify_Specifications():
    if request.method == "POST":
        try:
            WId = request.form.get("WId")
            CId = request.form.get("CId")
            CName = request.form.get("CName")
            WName = request.form.get("WName")
            CNClient = request.form.get("CNClient")
            CNWorker = request.form.get("CNWorker")
            MOClient = request.form.get("MOClient")
            MOWorker = request.form.get("MOWorker")
            ADClient = request.form.get("ADClient")
            ADWorker = request.form.get("ADWorker")
            PRType = request.form.get("PRType")
            PRColor = request.form.get("PRColor")
            PRShape = request.form.get("PRShape")
            GRAType = request.form.get("GRAType")
            GRAColor = request.form.get("GRAColor")
            WIRType = request.form.get("WIRType")
            WIRColor = request.form.get("WIRColor")
            GLAColor = request.form.get("GLAColor")
            GLAShape = request.form.get("GLAShape")
            GLAType = request.form.get("GLAType")
            FIPType = request.form.get("FIPType")
            FIPColor = request.form.get("FIPColor")
            DOORType = request.form.get("DOORType")
            DOORShape = request.form.get("DOORShape")
            ADDT = request.form.get("ADDT")
            #listToStr = ''.join([str(elem) for elem in ADDT])
            FAREA = request.form.get("FAREA")
            OMPrice = request.form.get("OMPrice")
            FAREAPrice = request.form.get("FAREAPrice")
            ADDTPrice = request.form.get("ADDTPrice")
            TRAPrice = request.form.get("TRAPrice")
            FULLPrice = request.form.get("FULLPrice")
            FBATDate = request.form.get("FBATDate")
            SBATDate = request.form.get("SBATDate")
            TBATDate = request.form.get("TBATDate")
            FBATAmount = request.form.get("FBATAmount")
            SBATAmount = request.form.get("SBATAmount")
            TBATAmount = request.form.get("TBATAmount")
            DELDate = request.form.get("DELDate")
            GIVDate = request.form.get("GIVDate")
            GIVPostion = request.form.get("GIVPostion")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                if WId:
                    cur.execute(f"UPDATE Specifications SET WId ={WId}  WHERE WId = {WId}")
                if CId:
                    cur.execute(f"UPDATE Specifications SET CId ={CId}  WHERE WId = {WId}")
                if CName:
                    cur.execute(f"UPDATE Specifications SET CName ='{CName}'  WHERE WId = {WId}")
                if WName:
                    cur.execute(f"UPDATE Specifications SET WName ='{WName}'  WHERE WId = {WId}")
                if CNClient:
                    cur.execute(f"UPDATE Specifications SET CNClient ={CNClient}  WHERE WId = {WId}")
                if CNWorker:
                    cur.execute(f"UPDATE Specifications SET CNWorker ={CNWorker}  WHERE WId = {WId}")
                if MOClient:
                    cur.execute(f"UPDATE Specifications SET MOClient ={MOClient}  WHERE WId = {WId}")
                if MOWorker:
                    cur.execute(f"UPDATE Specifications SET MOWorker ={MOWorker}  WHERE WId = {WId}")
                if ADClient:
                    cur.execute(f"UPDATE Specifications SET ADClient ='{ADClient}'  WHERE WId = {WId}")
                if ADWorker:
                    cur.execute(f"UPDATE Specifications SET ADWorker ='{ADWorker}'  WHERE WId = {WId}")
                if PRType:
                    cur.execute(f"UPDATE Specifications SET PRType ='{PRType}'  WHERE WId = {WId}")
                if PRColor:
                    cur.execute(f"UPDATE Specifications SET PRColor ='{PRColor}'  WHERE WId = {WId}")
                if PRShape:
                    cur.execute(f"UPDATE Specifications SET PRShape ='{PRShape}'  WHERE WId = {WId}")
                if GRAType:
                    cur.execute(f"UPDATE Specifications SET GRAType ='{GRAType}'  WHERE WId = {WId}")
                if GRAColor:
                    cur.execute(f"UPDATE Specifications SET GRAColor ='{GRAColor}'  WHERE WId = {WId}")
                if WIRType:
                    cur.execute(f"UPDATE Specifications SET WIRType ='{WIRType}'  WHERE WId = {WId}")
                if WIRColor:
                    cur.execute(f"UPDATE Specifications SET WIRColor ='{WIRColor}'  WHERE WId = {WId}")
                if GLAColor:
                    cur.execute(f"UPDATE Specifications SET GLAColor ='{GLAColor}'  WHERE WId = {WId}")
                if GLAShape:
                    cur.execute(f"UPDATE Specifications SET GLAShape ='{GLAShape}'  WHERE WId = {WId}")
                if GLAType:
                    cur.execute(f"UPDATE Specifications SET GLAType ='{GLAType}'  WHERE WId = {WId}")
                if FIPType:
                    cur.execute(f"UPDATE Specifications SET FIPType ='{FIPType}'  WHERE WId = {WId}")
                if FIPColor:
                    cur.execute(f"UPDATE Specifications SET FIPColor ='{FIPColor}'  WHERE WId = {WId}")
                if DOORType:
                    cur.execute(f"UPDATE Specifications SET DOORType ='{DOORType}'  WHERE WId = {WId}")
                if DOORShape:
                    cur.execute(f"UPDATE Specifications SET DOORShape ='{DOORShape}'  WHERE WId = {WId}")
                if ADDT:
                    cur.execute(f"UPDATE Specifications SET ADDT ='{ADDT}'  WHERE WId = {WId}")
                if FAREA:
                    cur.execute(f"UPDATE Specifications SET FAREA ={FAREA}  WHERE WId = {WId}")
                if OMPrice:
                    cur.execute(f"UPDATE Specifications SET OMPrice ={OMPrice}  WHERE WId = {WId}")
                if FAREAPrice:
                    cur.execute(f"UPDATE Specifications SET FAREAPrice ={FAREAPrice}  WHERE WId = {WId}")
                if ADDTPrice:
                    cur.execute(f"UPDATE Specifications SET ADDTPrice ={ADDTPrice}  WHERE WId = {WId}")
                if TRAPrice:
                    cur.execute(f"UPDATE Specifications SET TRAPrice ={TRAPrice}  WHERE WId = {WId}")
                if FULLPrice:
                    cur.execute(f"UPDATE Specifications SET FULLPrice ={FULLPrice}  WHERE WId = {WId}")
                if FBATDate:
                    cur.execute(f"UPDATE Specifications SET FBATDate ='{FBATDate}'  WHERE WId = {WId}")
                if SBATDate:
                    cur.execute(f"UPDATE Specifications SET SBATDate ='{SBATDate}'  WHERE WId = {WId}")
                if TBATDate:
                    cur.execute(f"UPDATE Specifications SET TBATDate ='{TBATDate}'  WHERE WId = {WId}")
                if FBATAmount:
                    cur.execute(f"UPDATE Specifications SET FBATAmount ={FBATAmount}  WHERE WId = {WId}")
                if SBATAmount:
                    cur.execute(f"UPDATE Specifications SET SBATAmount ={SBATAmount}  WHERE WId = {WId}")
                if TBATAmount:
                    cur.execute(f"UPDATE Specifications SET TBATAmount ={TBATAmount}  WHERE WId = {WId}")
                if DELDate:
                    cur.execute(f"UPDATE Specifications SET DELDate ='{DELDate}'  WHERE WId = {WId}")
                if GIVDate:
                    cur.execute(f"UPDATE Specifications SET GIVDate ='{GIVDate}'  WHERE WId = {WId}")
                if GIVPostion:
                    cur.execute(f"UPDATE Specifications SET GIVPostion ='{GIVPostion}'  WHERE WId = {WId}")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Modify Specifications.html' ,  title="Modify Specifications" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Show_Specifications' , methods=['GET', 'POST'])
def Show_Specifications():
    if request.method == "POST":
        WId = request.form.get("Id")
        db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
        cr = db.cursor()
        cr.execute(f"SELECT * FROM Specifications WHERE WId = {WId}")
        TheData = [list(tup) for tup in cr.fetchall()]
        db.close()
        return render_template('Show Specifications.html' , title="Show Specifications" , TheData=TheData ,TheFullComapnyName = TheFullComapnyName)
    return render_template('Get Specifications Id.html' ,  title="Get Specifications Id" ,TheFullComapnyName = TheFullComapnyName)

###################################################################################################################################################
# Accounts Section #
###################################################################################################################################################

@app.route('/New_Account' , methods=['GET', 'POST'])
def New_Account():
    if request.method == "POST":
        try:
            Name = request.form.get("Name")
            Password = request.form.get("Password")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO Passwords(Password,Name) VALUES({Password},'{Name}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
        return render_template('Get Password.html' ,  title="Get Password" , TheFullComapnyName = TheFullComapnyName)
    return render_template('Set Password.html' ,  title="Set Password" , TheFullComapnyName = TheFullComapnyName)

@app.route('/Sign_In' , methods=['GET', 'POST'])
def Sign_In():
    if request.method == "POST":
        try:
            Name = request.form.get("Name")
            Password = request.form.get("Password")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Name,Password FROM Passwords")
                TheData = [list(tup) for tup in cur.fetchall()]
                for D in TheData:
                    if D[0] == Name and D[1] == int(Password):
                        return render_template('Main.html' ,  title="Home", TheFullComapnyName = TheFullComapnyName)
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Get Password.html' ,  title="Get Password" , TheFullComapnyName = TheFullComapnyName)

@app.route('/Reset_Password' , methods=['GET', 'POST'])
def Reset_Password():
    if request.method == "POST":
        try:
            Name = request.form.get("Name")
            OPassword = request.form.get("OPassword")
            NPassword = request.form.get("NPassword")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Name,Password FROM Passwords")
                TheData = [list(tup) for tup in cur.fetchall()]
                for D in TheData:
                    if D[0] == Name and D[1] == int(OPassword):
                        cur.execute(f"UPDATE Passwords SET Password = {int(NPassword)} WHERE Name = '{Name}'")
                        return render_template('Get Password.html' ,  title="Get Password" , TheFullComapnyName = TheFullComapnyName)
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Reset Password.html' ,  title="Reset Password" , TheFullComapnyName = TheFullComapnyName)

###################################################################################################################################################
# Main Page Section #
###################################################################################################################################################

@app.route('/')
def index():
    return render_template('Set Password.html' , title="Home" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Main')
def Main():
    return render_template('Main.html' , title="Home" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Client')
def Client():
    return render_template('Clients.html' ,  title="Client" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Prices')
def Prices():
    return render_template('Prices.html' ,  title="Prices" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Work')
def Work():
    return render_template('Works.html' ,  title="Work" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Marchant')
def Marchant():
    return render_template('Marchants.html' ,  title="Marchant" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Car')
def Car():
    return render_template('Cars.html' ,  title="Car" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Worker')
def Worker():
    return render_template('Workers.html' ,  title="Worker" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Factory')
def Factory():
    return render_template('Factory.html' ,  title="Factory" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Home')
def Home():
    return render_template('Home.html' ,  title="Home" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Report')
def Report():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute(f"SELECT Profits FROM Works")
    TheProfits = [list(tup) for tup in cr.fetchall()]
    TP = 0
    for i in TheProfits:
        TP += int(i[0])
    cr.execute(f"SELECT Get FROM Workers")
    TheSalary = [list(tup) for tup in cr.fetchall()]
    TS = 0
    for i in TheSalary:
        TS += int(i[0])

    cr.execute(f"SELECT Amount FROM Rents")
    TheFRents = [list(tup) for tup in cr.fetchall()]
    TFR = 0
    for i in TheFRents:
        TFR += int(i[0])
    cr.execute(f"SELECT Amount FROM GovernPayments")
    TheFGPayments = [list(tup) for tup in cr.fetchall()]
    TFGP = 0
    for i in TheFGPayments:
        TFGP += int(i[0])
    cr.execute(f"SELECT Amount FROM Payments")
    TheFPayments = [list(tup) for tup in cr.fetchall()]
    TFP = 0
    for i in TheFPayments:
        TFP += int(i[0])
    TF = TFP + TFGP + TFR

    cr.execute(f"SELECT Amount FROM HRents")
    TheHRents = [list(tup) for tup in cr.fetchall()]
    THR = 0
    for i in TheHRents:
        THR += int(i[0])

    cr.execute(f"SELECT Amount FROM HGovernPayments")
    TheHGPayments = [list(tup) for tup in cr.fetchall()]
    THGP = 0
    for i in TheHGPayments:
        THGP += int(i[0])

    cr.execute(f"SELECT Amount FROM HSchoolPayments")
    TheHSPayments = [list(tup) for tup in cr.fetchall()]
    THSP = 0
    for i in TheHSPayments:
        THSP += int(i[0])

    cr.execute(f"SELECT Amount FROM HPayments")
    TheHPayments = [list(tup) for tup in cr.fetchall()]
    THP = 0
    for i in TheHPayments:
        THP += int(i[0])
    TH = THR + THGP + THP + THSP
    Rest = TP - TS - TF - TH
    return render_template('Report.html' ,  title="Report" ,TheFullComapnyName = TheFullComapnyName,TheProfits=str(TP),TheTSalary=str(TS),TheTHome=str(TH),TheTFactory=str(TF),TheRest=str(Rest))

###################################################################################################################################################
# Price Section #
###################################################################################################################################################

@app.route('/Add_Granium_Price', methods=['GET', 'POST'])
def Add_Granium_Price():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Color = request.form.get("Color")
            Price = request.form.get("Price")
            Notes = request.form.get("Notes")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Granium")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Granium VALUES('{Date}','G{TheId}',{Price},'{Color}','{Notes}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Granium")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Granium Price.html' ,  title="Add Granium Price", Id=f'G{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_GraniumAddtions_Price', methods=['GET', 'POST'])
def Add_GraniumAddtions_Price():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Price = request.form.get("Price")
            TheAddtion = request.form.get("Addtion")
            Notes = request.form.get("Notes")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM GarniumAddtions")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO GarniumAddtions VALUES('{Date}','GA{TheId}',{Price},'{TheAddtion}','{Notes}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM GarniumAddtions")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add GraniumAddtions Price.html' ,  title="Add Granium Addtions Price", Id=f'GA{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_Glass_Price', methods=['GET', 'POST'])
def Add_Glass_Price():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Price = request.form.get("Price")
            Color = request.form.get("Color")
            Notes = request.form.get("Notes")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Glass")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Glass VALUES('{Date}','GL{TheId}',{Price},0,'{Color}','{Notes}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Glass")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Glass Price.html' ,  title="Add Glass Price" , Id=f'GL{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_GlassAddtions_Price', methods=['GET', 'POST'])
def Add_GlassAddtions_Price():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Price = request.form.get("Price")
            TheAddtion = request.form.get("Addtion")
            Notes = request.form.get("Notes")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM GlassAddtions")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO GlassAddtions VALUES('{Date}','GLA{TheId}',{Price},'{TheAddtion}','{Notes}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM GlassAddtions")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add GlassAddtions Price.html' ,  title="Add Glass Addtions Price" , Id=f'GLA{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_Fibr_Price', methods=['GET', 'POST'])
def Add_Fibr_Price():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Type = request.form.get("Type")
            Price = request.form.get("Price")
            Notes = request.form.get("Notes")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Fibr")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Fibr VALUES('{Date}','F{TheId}',{Price},'{Type}','{Notes}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Fibr")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Fibr Price.html' ,  title="Add Fibr Price" , Id = f'F{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_ShutersMachines_Price', methods=['GET', 'POST'])
def Add_ShutersMachines_Price():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Type = request.form.get("Type")
            Price = request.form.get("Price")
            Shape = request.form.get("Shape")
            Notes = request.form.get("Notes")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM ShutersMachines")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO ShutersMachines VALUES('{Date}','SHM{TheId}',{Price},'{Type}','{Shape}','{Notes}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM ShutersMachines")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add ShutersMachines Price.html' ,  title="Add Shuters Machines Price", Id=f'SHM{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_Addtions_Price', methods=['GET', 'POST'])
def Add_Addtions_Price():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Type = request.form.get("Type")
            Price = request.form.get("Price")
            Notes = request.form.get("Notes")
            Name = request.form.get("Name")
            Section = request.form.get("Section")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Addtions")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Addtions VALUES('{Date}','AD{TheId}',{Price},'{Type}','{Name}','{Section}','{Notes}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Addtions")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Addtions Price.html' ,  title="Add Addtions Price" ,Id = f'AD{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_Windows_Price', methods=['GET', 'POST'])
def Add_Windows_Price():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Type = request.form.get("Type")
            Price = request.form.get("Price")
            Shape = request.form.get("Shape")
            Spec = request.form.get("Spec")
            Notes = request.form.get("Notes")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Windows")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Windows VALUES('{Date}','W{TheId}',{Price},'{Type}','{Shape}','{Spec}','{Notes}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Windows")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Windows Price.html' ,  title="Add Windows Price", Id=f'W{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_Doors_Price', methods=['GET', 'POST'])
def Add_Doors_Price():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Type = request.form.get("Type")
            Price = request.form.get("Price")
            Shape = request.form.get("Shape")
            Spec = request.form.get("Spec")
            Notes = request.form.get("Notes")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Doors")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Doors VALUES('{Date}','D{TheId}',{Price},'{Type}','{Shape}','{Spec}','{Notes}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Doors")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Doors Price.html' ,  title="Add Doors Price" , Id=f'D{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_Kitchens_Price', methods=['GET', 'POST'])
def Add_Kitchens_Price():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Type = request.form.get("Type")
            Price = request.form.get("Price")
            Shape = request.form.get("Shape")
            Spec = request.form.get("Spec")
            Notes = request.form.get("Notes")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Kitchens")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Kitchens VALUES('{Date}','K{TheId}',{Price},'{Type}','{Shape}','{Spec}','{Notes}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Kitchens")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Kitchens Price.html' ,  title="Add Kitchens Price" , Id=f'K{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_Shutters_Price', methods=['GET', 'POST'])
def Add_Shutters_Price():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Type = request.form.get("Type")
            Price = request.form.get("Price")
            Color = request.form.get("Color")
            Spec = request.form.get("Spec")
            Notes = request.form.get("Notes")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Shuters")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Shuters VALUES('{Date}','S{TheId}',{Price},'{Type}','{Color}','{Spec}','{Notes}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Shuters")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Shuters Price.html' ,  title="Add Shuters Price" , Id=f'S{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_Covers_Price', methods=['GET', 'POST'])
def Add_Covers_Price():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Type = request.form.get("Type")
            Price = request.form.get("Price")
            Color = request.form.get("Color")
            Spec = request.form.get("Spec")
            Notes = request.form.get("Notes")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Covers")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Covers VALUES('{Date}','C{TheId}',{Price},'{Type}','{Color}','{Spec}','{Notes}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Covers")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Covers Price.html' ,  title="Add Covers Price" , Id=f'C{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_Wires_Price', methods=['GET', 'POST'])
def Add_Wires_Price():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Type = request.form.get("Type")
            Price = request.form.get("Price")
            Shape = request.form.get("Shape")
            Color = request.form.get("Color")
            Spec = request.form.get("Spec")
            Notes = request.form.get("Notes")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Wires")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Wires VALUES('{Date}','W{TheId}',{Price},'{Type}','{Color}','{Shape}','{Spec}','{Notes}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Wires")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Wires Price.html' ,  title="Add Wires Price", Id=f'W{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Select_Section', methods=['GET', 'POST'])
def Select_Section():
    if request.method == "POST":
        Section = request.form.get("Section")
        if (Section == "Granuim"):
            return(Add_Granium_Price())
        elif (Section == "GranuimAddtions"):
            return(Add_GraniumAddtions_Price())
        elif (Section == "ShutersMachines"):
            return(Add_ShutersMachines_Price())
        elif (Section == "Glass"):
            return(Add_Glass_Price())
        elif (Section == "Fibr"):
            return(Add_Fibr_Price())
        elif (Section == "Kitchens"):
            return(Add_Kitchens_Price())
        elif (Section == "Windows"):
            return(Add_Windows_Price())
        elif (Section == "Shutters"):
            return(Add_Shutters_Price())
        elif (Section == "Doors"):
            return(Add_Doors_Price())
        elif (Section == "Covers"):
            return(Add_Covers_Price())
        elif (Section == "Wires"):
            return(Add_Wires_Price())
        elif (Section == "Addtions"):
            return(Add_Addtions_Price())
        elif (Section == "GlassAddtions"):
            return(Add_GlassAddtions_Price())
        else:
            return render_template('Error.html' ,  title="Have Error" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_Price', methods=['GET', 'POST'])
def Add_Price():
    return render_template('Add Price.html' ,  title="Add Price" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Choose_Show_Section', methods=['GET', 'POST'])
def Choose_Show_Section():
    return render_template('Select Section.html' ,  title="Choose Show Section" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Show_Section_Price', methods=['GET', 'POST'])
def Show_Section_Price():
    if request.method == "POST":
        db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Price.db")
        cr = db.cursor()
        Section = request.form.get("Section")
        if (Section == "Granuim"):
            cr.execute("SELECT * FROM Granium")
            TheData = [list(tup) for tup in cr.fetchall()]
            return render_template('Show Section Price.html' , TheData=TheData , Type="Granuim",  title="Granuim" ,TheFullComapnyName = TheFullComapnyName)
            
        
        elif (Section == "GranuimAddtions"):
            cr.execute("SELECT * FROM GarniumAddtions")
            TheData = [list(tup) for tup in cr.fetchall()]
            return render_template('Show Section Price.html' , TheData=TheData , Type="GarniumAddtions" ,  title="GarniumAddtions" ,TheFullComapnyName = TheFullComapnyName)
            
        
        elif (Section == "Glass"):
            cr.execute("SELECT * FROM Glass")
            TheData = [list(tup) for tup in cr.fetchall()]
            return render_template('Show Section Price.html' , TheData=TheData , Type="Glass" ,  title="Glass" ,TheFullComapnyName = TheFullComapnyName)
            
        
        elif (Section == "GlassAddtions"):
            cr.execute("SELECT * FROM GlassAddtions")
            TheData = [list(tup) for tup in cr.fetchall()]
            return render_template('Show Section Price.html' , TheData=TheData , Type="GlassAddtions" ,  title="GlassAddtions"  ,TheFullComapnyName = TheFullComapnyName)
            
        
        elif (Section == "Fibr"):
            cr.execute("SELECT * FROM Fibr")
            TheData = [list(tup) for tup in cr.fetchall()]
            return render_template('Show Section Price.html', TheData=TheData , Type="Fibr" ,  title="Fibr" ,TheFullComapnyName = TheFullComapnyName)
            
            
        
        elif (Section == "Kitchens"):
            cr.execute("SELECT * FROM Kitchens")
            TheData = [list(tup) for tup in cr.fetchall()]
            return render_template('Show Section Price.html' , TheData=TheData , Type="Kitchens" ,  title="Kitchens"  ,TheFullComapnyName = TheFullComapnyName)
            
            
        elif (Section == "Windows"):
            cr.execute("SELECT * FROM Windows")
            TheData = [list(tup) for tup in cr.fetchall()]
            return render_template('Show Section Price.html', TheData=TheData , Type="Windows" ,  title="Windows"  ,TheFullComapnyName = TheFullComapnyName)
            
        
        elif (Section == "ShutersMachines"):
            cr.execute("SELECT * FROM ShutersMachines")
            TheData = [list(tup) for tup in cr.fetchall()]    
            return render_template('Show Section Price.html' , TheData=TheData , Type="ShutersMachines" ,  title="ShutersMachines"  ,TheFullComapnyName = TheFullComapnyName)
            
        
        elif (Section == "Shutters"):
            cr.execute("SELECT * FROM Shuters")
            TheData = [list(tup) for tup in cr.fetchall()]    
            return render_template('Show Section Price.html' , TheData=TheData , Type="Shuters" ,  title="Shuters" ,  TheFullComapnyName = TheFullComapnyName)
            
        
        elif (Section == "Doors"):
            cr.execute("SELECT * FROM Doors")
            TheData = [list(tup) for tup in cr.fetchall()]    
            return render_template('Show Section Price.html' , TheData=TheData , Type="Doors" ,  title="Doors" ,  TheFullComapnyName = TheFullComapnyName)
            
        
        elif (Section == "Covers"):
            cr.execute("SELECT * FROM Covers")
            TheData = [list(tup) for tup in cr.fetchall()]    
            return render_template('Show Section Price.html' , TheData=TheData , Type="Covers" ,  title="Covers"  ,TheFullComapnyName = TheFullComapnyName)

        
        elif (Section == "Wires"):
            cr.execute("SELECT * FROM Wires")
            TheData = [list(tup) for tup in cr.fetchall()]
            return render_template('Show Section Price.html' , TheData=TheData , Type="Wires" ,  title="Wires"  ,TheFullComapnyName = TheFullComapnyName)

        
        elif (Section == "Addtions"):
            cr.execute("SELECT * FROM Addtions")
            TheData = [list(tup) for tup in cr.fetchall()]
            return render_template('Show Section Price.html' , TheData=TheData , Type="Addtions" ,  title="Addtions"  ,TheFullComapnyName = TheFullComapnyName)
        
        else:
            return render_template('Error.html' ,  title="Have Error" ,TheFullComapnyName = TheFullComapnyName)

###################################################################################################################################################
# Clients Section #
###################################################################################################################################################

@app.route('/Modify_Client' , methods=['GET', 'POST'])
def Modify_Client():
    if request.method == "POST":
        try:
            Address = request.form.get("Address")
            Location = request.form.get("Location")
            CID = request.form.get("CID")
            Mobile = request.form.get("Mobile")
            Name = request.form.get("Name")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                if Name:
                    cur.execute(f"UPDATE Clients SET Name ='{Name}'  WHERE Id = {CID}")
                if Address:
                    cur.execute(f"UPDATE Clients SET Address ='{Address}'  WHERE Id = {CID}")
                if Mobile:
                    cur.execute(f"UPDATE Clients SET Mobile ={Mobile}  WHERE Id = {CID}")
                if Location:
                    cur.execute(f"UPDATE Clients SET Location ='{Location}'  WHERE Id = {CID}")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Modify Client.html' , title="Modify Client" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Show_Clients')
def Show_Clients():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM Clients")
    TheData = [list(tup) for tup in cr.fetchall()]
    db.close()
    return render_template('Show Clients.html' , title="Show Clients"  ,  Clients=[TheData] ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_Client' , methods=['GET', 'POST'])
def Add_Client():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Name = request.form.get("Name")
            Address = request.form.get("Address")
            Mobile = request.form.get("Mobile")
            Location = request.form.get("Location")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Clients")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Clients(Date,Name,Id,Address,Mobile,Location,NumberOfWorks) VALUES('{Date}','{Name}',{TheId} ,'{Address}',{Mobile},'{Location}',0)")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Clients")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Client.html' , title="Add Client", ID=f'{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Remove_Client' , methods=['GET', 'POST'])
def Remove_Client():
    if request.method == "POST":
        try:
            CID = request.form.get("CID")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"DELETE FROM Clients WHERE Id = {CID}")
                cur.execute(f"DELETE FROM Works WHERE CId = {CID}")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Remove Client.html' , title="Remove Client" ,TheFullComapnyName =TheFullComapnyName)  

@app.route('/Show_Client_Data' , methods=['GET', 'POST'])
def Show_Client_Data():
    if request.method == "POST":
        CID = request.form.get("Id")
        db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
        cr = db.cursor()
        cr.execute(f"SELECT * FROM Clients WHERE Id = {CID}")
        TheData = [list(tup) for tup in cr.fetchall()]
        cr.execute(f"SELECT * FROM Works WHERE CId = {CID}")
        WData =  [list(tup) for tup in cr.fetchall()]
        db.close()
        return render_template('Show Client Data.html' , title="Show Client Data" , TheData=TheData , WData=[WData] ,TheFullComapnyName = "الاسراء لعمال الوميتال")
    return render_template('Get Client Id.html' , title="Get Client Id" , TheFullComapnyName = TheFullComapnyName )

###################################################################################################################################################
# Works Section #
###################################################################################################################################################

@app.route('/Modify_Work' , methods=['GET', 'POST'])
def Modify_Work():
    if request.method == "POST":
        try:
            Type = request.form.get("Type")
            WID = request.form.get("WID")
            CID = request.form.get("CID")
            TotalMoney = request.form.get("TMoney")
            Address = request.form.get("Address")
            Location = request.form.get("Location")
            Drive = request.form.get("Drive")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                if CID:
                    cur.execute(f"SELECT Name FROM Clients WHERE Id ={CID}")
                    NName = cur.fetchone()[0]
                    cur.execute(f"UPDATE Works SET CName ='{NName}'  WHERE WId = {WID}")
                if CID:
                    cur.execute(f"UPDATE Works SET CId ={CID}  WHERE WId = {WID}")
                if Type:
                    cur.execute(f"UPDATE Works SET Type ='{Type}'  WHERE WId = {WID}")
                if Address:
                    cur.execute(f"UPDATE Works SET Address ='{Address}'  WHERE WId = {WID}")
                if Drive:
                    cur.execute(f"UPDATE Works SET Drive ='{Drive}'  WHERE WId = {WID}")
                if Location:
                    cur.execute(f"UPDATE Works SET Location ='{Location}'  WHERE WId = {WID}")
                if TotalMoney:
                    cur.execute(f"UPDATE Works SET TOTALMoney = {TotalMoney}  WHERE WId = {WID}")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Modify Work.html' , title="Modify work" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Remove_Work'  , methods=['GET', 'POST'])
def Remove_Work():
    if request.method == "POST":
        try:
            WID = request.form.get("WID")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT CId FROM Works WHERE WId = {WID}")
                TheClient = cur.fetchone()[0]
                cur.execute(f"UPDATE Clients SET NumberOfWorks = NumberOfWorks - 1 WHERE Id = {int(TheClient)}")
                cur.execute(f"DELETE FROM Works WHERE WId = {WID}")
                cur.execute(f"DELETE FROM Specifications WHERE WId = {WID}")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Works.db") as con:
                cur = con.cursor()
                con.execute(f"DROP TABLE W{WID}")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Remove Work.html' , title="Remove work" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Show_Works')
def Show_Works():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM Works")
    TheData = [list(tup) for tup in cr.fetchall()]
    db.close()
    return render_template('Show Works.html' , title="Show Works" ,  Works=[TheData] ,TheFullComapnyName =TheFullComapnyName)
     
@app.route('/Add_Work'  , methods=['GET', 'POST'])
def Add_Work(): 
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Address = request.form.get("Address")
            Location = request.form.get("Location")
            Drive = request.form.get("drive")
            Type = request.form.get("Type")
            Input = request.form.get("Input")
            Total = request.form.get("Total")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT WId FROM Works")
                TheId = len(cur.fetchall())
                CID = request.form.get("CID")
                cur.execute(f"SELECT Name FROM Clients WHERE Id = {CID}")
                Name = cur.fetchone()[0]
                cur.execute(f"INSERT INTO Works(Date,CName,CId,WId,Address,Location,Drive,Type,INMoney,OUTMoney,TOTALMoney) VALUES('{Date}','{Name}', {CID},{TheId} ,'{Address}','{Location}' ,'{Drive}','{Type}',{Input},0,{Total})")
                cur.execute(f"UPDATE Clients SET NumberOfWorks = NumberOfWorks + 1 WHERE Id = {CID}")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Works.db") as con:
                cur = con.cursor()
                cur.execute(f"CREATE TABLE IF NOT EXISTS W{TheId}(Date DATE , Money INTEGER , For TEXT , Marchant TEXT , Car INTEGER)")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute(f"SELECT WId FROM Works")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Work.html' , title="Add Work" , ID=f'{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_Money' , methods=['GET', 'POST'])
def Add_Money():
    if request.method == "POST":
        try:
            TheId = request.form.get("WID")
            Input = request.form.get("Input")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"UPDATE Works SET INMoney= INMoney +{int(Input)} WHERE WId = {TheId}")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Add Money.html' , title="Add Money" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_Payments'  , methods=['GET', 'POST'])
def Add_Payments():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT Id FROM Marchants")
    TheMarchants = len(cr.fetchall())
    cr.execute("SELECT Id FROM Cars")
    TheCars = len(cr.fetchall())
    db.commit()
    db.close()
    if request.method == "POST" and TheMarchants != 0 and TheCars != 0:
        try:
            Date = request.form.get("Date")
            WID = request.form.get("WID")
            For = request.form.get("For")
            Marchant = request.form.get("Marchant")
            Car = request.form.get("Using")
            OutMoney = request.form.get("OutMoney")
            InMoney = request.form.get("Amount")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"UPDATE Works SET OUTMoney = OUTMoney +{int(OutMoney)+int(InMoney)}  WHERE WId = {WID}")
                cur.execute(f"SELECT Id FROM Marchants WHERE Name='{Marchant}'")
                TheMarchant = cur.fetchone()[0]
                cur.execute(f"SELECT CName FROM Works WHERE WId = {int(WID)}")
                TheClient = cur.fetchone()[0]
                cur.execute(f"UPDATE Marchants SET TotalMoney = TotalMoney +{int(OutMoney)} WHERE Id ={int(TheMarchant)}")
                cur.execute(f"UPDATE Cars SET Input = Input +{int(InMoney)} WHERE Id = {Car}")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Marchants.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO M{TheMarchant}(Date,Amount,Product,For) VALUES('{Date}', {OutMoney} ,'{For}','{TheClient}')")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Works.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO W{WID}(Date,Money,For,Marchant,Car) VALUES('{Date}', {OutMoney} ,'{For}','{Marchant}','{Car}')")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Cars.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO C{Car}(Date,INM,Client,ClientServ) VALUES('{Date}',{InMoney},'{For}','{TheClient}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT Name FROM Marchants")
    TheMarchants = [list(tup) for tup in  cr.fetchall()]
    db.commit()
    db.close()
    return render_template('Add Payments.html' , title="Add Payments" ,TheFullComapnyName = TheFullComapnyName , TheMarchants=TheMarchants)

@app.route('/Show_Work_Data' , methods=['GET', 'POST'])
def Show_Work_Data():
    if request.method == "POST":
        CID = request.form.get("Id")
        db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
        cr = db.cursor()
        cr.execute(f"SELECT * FROM Works WHERE WId = {CID}")
        TheData = [list(tup) for tup in cr.fetchall()]
        db.close()
        db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Works.db")
        cr = db.cursor()
        cr.execute(f"SELECT * FROM W{CID}")
        WData = [list(tup) for tup in cr.fetchall()]
        db.close()
        return render_template('Show Work Data.html' , title="Show Work Data" , TheData=TheData , WData=WData ,TheFullComapnyName = TheFullComapnyName)
    return render_template('Get Work Id.html' , title="Get Work Id" ,TheFullComapnyName = TheFullComapnyName)

###################################################################################################################################################
# Marchants Section #
###################################################################################################################################################

@app.route('/Add_Marchant' , methods=['GET', 'POST'])
def Add_Marchant():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Address = request.form.get("Address")
            Location = request.form.get("Location")
            Type = request.form.get("Type")
            Name = request.form.get("Name")
            Mobile = request.form.get("Mobile")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Marchants")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Marchants(Date,Name,Id,Location,Mobile,Address,Type,TotalMoney) VALUES('{Date}','{Name}',{TheId} ,'{Location}',{Mobile},'{Address}','{Type}',0)")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Marchants.db") as con:
                cur = con.cursor()
                cur.execute(f"CREATE TABLE IF NOT EXISTS M{TheId}(Date DATE , Amount INTEGER , Product TEXT , For TEXT)")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Marchants")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Marchant.html' , title="Add Marchant", ID=f'{TheId}' ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Remove_Marchant' , methods=['GET', 'POST'])
def Remove_Marchant():
    if request.method == "POST":
        try:
            ID = request.form.get("ID")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"DELETE FROM Marchants WHERE Id = {ID}")
                #cur.execute(f"UPDATE Marchants SET WId = WId-1  WHERE Id > {ID}")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Marchants.db") as con:
                cur = con.cursor()
                con.execute(f"DROP TABLE M{ID}")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Remove Marchant.html' , title="Remove Marchant" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Modify_Marchant' , methods=['GET', 'POST'])
def Modify_Marchant():
    if request.method == "POST":
        try:
            Type = request.form.get("Type")
            ID = request.form.get("ID")
            Address = request.form.get("Address")
            Location = request.form.get("Location")
            Mobile = request.form.get("Mobile")
            Name = request.form.get("Name")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                if Name :
                    cur.execute(f"UPDATE Marchants SET Name ='{Name}'  WHERE Id = {ID}")
                if Type:
                    cur.execute(f"UPDATE Marchants SET Type ='{Type}'  WHERE Id = {ID}")
                if Address:
                    cur.execute(f"UPDATE Marchants SET Address ='{Address}'  WHERE Id = {ID}")
                if Location:
                    cur.execute(f"UPDATE Marchants SET Location ='{Location}'  WHERE Id = {ID}")
                if Mobile:
                    cur.execute(f"UPDATE Marchants SET Mobile ='{Mobile}'  WHERE Id = {ID}")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Modify Marchant.html' , title="Modify Marchant" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Show_Marchants')
def Show_Marchants():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM Marchants")
    TheData = [list(tup) for tup in cr.fetchall()]
    db.close()
    return render_template('Show Marchants.html' , title="Show Marchants" , Marchants=[TheData])

@app.route('/Show_Marchant_Data'  , methods=['GET', 'POST'])
def Show_Marchant_Data():
    if request.method == "POST":
        CID = request.form.get("Id")
        db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
        cr = db.cursor()
        cr.execute(f"SELECT * FROM Marchants WHERE Id = {CID}")
        TheData = [list(tup) for tup in cr.fetchall()]
        db.close()
        db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Marchants.db")
        cr = db.cursor()
        cr.execute(f"SELECT * FROM M{CID}")
        WData = [list(tup) for tup in cr.fetchall()]
        db.close()
        return render_template('Show Marchant Data.html' , title="Show Marchant Data" , TheData=TheData , WData=WData ,TheFullComapnyName =TheFullComapnyName)
    return render_template('Get Marchant Id.html' , title="Get Marchant Id" ,TheFullComapnyName =TheFullComapnyName)

###################################################################################################################################################
# Cars Section #
###################################################################################################################################################

@app.route('/Add_Car' , methods=['GET', 'POST'])
def Add_Car():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Chars = request.form.get("Chars")
            Number = request.form.get("Number")
            Type = request.form.get("Type")
            Shape = request.form.get("Shape")
            Color = request.form.get("Color")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Cars")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Cars(Date,Id,Number,Chars,Color,Type,Shape,Input,Output) VALUES('{Date}',{TheId},{Number},'{Chars}','{Color}','{Type}','{Shape}',0,0)")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Cars.db") as con:
                cur = con.cursor()
                cur.execute(f"CREATE TABLE IF NOT EXISTS C{TheId}(Date DATE , OUT INTEGER , Gas INTEGER , Oil INTEGER , For TEXT , INM INTEGER , Client TEXT , ClientServ TEXT )")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Cars")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Car.html' , title="Add Car", Id=f'{TheId}' ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Remove_Car' , methods=['GET', 'POST'])
def Remove_Car():
    if request.method == "POST":
        try:
            ID = request.form.get("Id")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"DELETE FROM Cars WHERE Id = {ID}")
                #cur.execute(f"UPDATE Marchants SET WId = WId-1  WHERE Id > {ID}")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Cars.db") as con:
                cur = con.cursor()
                con.execute(f"DROP TABLE C{ID}")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Remove Car.html' , title="Remove Car" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Modify_Car' , methods=['GET', 'POST'])
def Modify_Car():
    if request.method == "POST":
        try:
            Type = request.form.get("Type")
            ID = request.form.get("Id")
            Shape = request.form.get("Shape")
            Color = request.form.get("Color")
            Number = request.form.get("Number")
            Chars = request.form.get("Chars")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                if Shape :
                    cur.execute(f"UPDATE Cars SET Shape ='{Shape}'  WHERE Id = {ID}")
                if Type:
                    cur.execute(f"UPDATE Cars SET Type ='{Type}'  WHERE Id = {ID}")
                if Color:
                    cur.execute(f"UPDATE Cars SET Color ='{Color}'  WHERE Id = {ID}")
                if Number:
                    cur.execute(f"UPDATE Cars SET Number ='{Number}'  WHERE Id = {ID}")
                if Chars:
                    cur.execute(f"UPDATE Cars SET Chars ='{Chars}'  WHERE Id = {ID}")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Modify Car.html' , title="Modify Car" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Show_Cars')
def Show_Cars():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM Cars")
    TheData = [list(tup) for tup in cr.fetchall()]
    db.close()
    return render_template('Show Cars.html' , title="Show Cars" , Cars=[TheData] ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Add_Payments_For_Car'  , methods=['GET', 'POST'])
def Add_Payments_For_Car():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            ID = request.form.get("Id")
            For = request.form.get("For")
            Oil = request.form.get("Oil")
            Gas = request.form.get("Gas")
            OutMoney = request.form.get("OutMoney")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"UPDATE Cars SET Output = Output +{int(OutMoney)+int(Oil)+int(Gas)} WHERE Id = {ID}")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Cars.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO C{ID}(Date,OUT,Gas,Oil,For) VALUES('{Date}',{OutMoney},{Gas},{Oil},'{For}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Add Payments For Car.html' , title="Add Payments For Car" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Show_Car_Data'  , methods=['GET', 'POST'])
def Show_Car_Data():
    if request.method == "POST":
        CID = request.form.get("Id")
        db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
        cr = db.cursor()
        cr.execute(f"SELECT * FROM Cars WHERE Id = {CID}")
        TheData = [list(tup) for tup in cr.fetchall()]
        db.close()
        db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Cars.db")
        cr = db.cursor()
        cr.execute(f"SELECT * FROM C{CID}")
        WData = [list(tup) for tup in cr.fetchall()]
        db.close()
        return render_template('Show Car Data.html' , title="Show Car Data" , TheData=TheData , WData=WData ,TheFullComapnyName =TheFullComapnyName)
    return render_template('Get Car Id.html' , title="Get Car Id" , TheFullComapnyName =TheFullComapnyName)

###################################################################################################################################################
# Workers Section #
###################################################################################################################################################

@app.route('/Add_Worker' , methods=['GET', 'POST'])
def Add_Worker():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Name = request.form.get("Name")
            Mobile = request.form.get("Mobile")
            Location = request.form.get("Location")
            Address = request.form.get("Address")
            WType = request.form.get("WType")
            SType = request.form.get("SType")
            PerDay = request.form.get("DailySalary")
            CardNum = request.form.get("CardNum")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"SELECT Id FROM Workers")
                TheId = len(cur.fetchall())
                cur.execute(f"INSERT INTO Workers(Date,Name,Id,Mobile,Location,Address,WType,SType,PerDay,CardNumber,DaysNumber,Get,Discounts) VALUES('{Date}','{Name}',{TheId},{Mobile},'{Location}','{Address}','{WType}','{SType}',{PerDay},'{CardNum}',0,0,0)")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Workers.db") as con:
                cur = con.cursor()
                cur.execute(f"CREATE TABLE IF NOT EXISTS Wo{TheId}(Date DATE , Enroll INTEGER , Bleach INTEGER , Discount INTEGER , Note TEXT)")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally: 
            con.close()
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute(f"SELECT Id FROM Workers")
    TheId = len(cr.fetchall())
    db.close()
    return render_template('Add Worker.html' , title="Add Worker" , Id=f'{TheId}' ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Remove_Worker' , methods=['GET', 'POST'])
def Remove_Worker():
    if request.method == "POST":
        try:
            ID = request.form.get("Id")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"DELETE FROM Workers WHERE Id = {ID}")
                #cur.execute(f"UPDATE Marchants SET WId = WId-1  WHERE Id > {ID}")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Workers.db") as con:
                cur = con.cursor()
                con.execute(f"DROP TABLE Wo{ID}")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Remove Worker.html' , title="Remove Worker" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Modify_Worker' , methods=['GET', 'POST'])
def Modify_Worker():
    if request.method == "POST":
        try:
            ID = request.form.get("Id")
            Name = request.form.get("Name")
            Mobile = request.form.get("Mobile")
            Location = request.form.get("Location")
            Address = request.form.get("Address")
            WType = request.form.get("WType")
            SType = request.form.get("SType")
            CardNum = request.form.get("CardNum")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                if Name :
                    cur.execute(f"UPDATE Workers SET Name ='{Name}'  WHERE Id = {ID}")
                if Mobile:
                    cur.execute(f"UPDATE Workers SET Mobile ='{Mobile}'  WHERE Id = {ID}")
                if Location:
                    cur.execute(f"UPDATE Workers SET Location ='{Location}'  WHERE Id = {ID}")
                if Address:
                    cur.execute(f"UPDATE Workers SET Address ='{Address}'  WHERE Id = {ID}")
                if WType:
                    cur.execute(f"UPDATE Workers SET WType ='{WType}'  WHERE Id = {ID}")
                if SType:
                    cur.execute(f"UPDATE Workers SET SType ='{SType}'  WHERE Id = {ID}")
                if CardNum:
                    cur.execute(f"UPDATE Workers SET CardNum ='{CardNum}'  WHERE Id = {ID}")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Modify Worker.html' , title="Modify Worker" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Show_Workers')
def Show_Workers():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM Workers")
    TheData = [list(tup) for tup in cr.fetchall()]
    db.close()
    return render_template('Show Workers.html' , title="Show Workers" , Workers=[TheData] ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Enroll_Worker' , methods=['GET', 'POST'])
def Enroll_Worker():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            ID = request.form.get("Id")
            Enroll = request.form.get("EnrollNum")
            Note = request.form.get("Note")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"UPDATE Workers SET DaysNumber = DaysNumber +{int(Enroll)} WHERE Id = {ID}")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Workers.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO Wo{ID}(Date,Enroll,Note) VALUES('{Date}',{Enroll},'{Note}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Enroll Worker.html' , title="Enroll Worker" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Bleach_Worker' , methods=['GET', 'POST'])
def Bleach_Worker():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            ID = request.form.get("Id")
            Bleach = request.form.get("SalaryAm")
            Note = request.form.get("Note")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"UPDATE Workers SET Get = Get +{int(Bleach)} WHERE Id = {ID}")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Workers.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO Wo{ID}(Date,Bleach,Note) VALUES('{Date}',{Bleach},'{Note}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Bleach Worker.html' , title="Bleach Worker" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Worker_Discount' , methods=['GET', 'POST'])
def Worker_Discount():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            ID = request.form.get("Id")
            Discount = request.form.get("DiscountAm")
            Note = request.form.get("Note")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"UPDATE Workers SET Discounts = Discounts +{int(Discount)} WHERE Id = {ID}")
                con.commit()
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Workers.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO Wo{ID}(Date,Discount,Note) VALUES('{Date}',{Discount},'{Note}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Worker Discount.html' , title="Worker Discount" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Show_Worker_Data'  , methods=['GET', 'POST'])
def Show_Worker_Data():
    if request.method == "POST":
        CID = request.form.get("Id")
        db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
        cr = db.cursor()
        cr.execute(f"SELECT * FROM Workers WHERE Id = {CID}")
        TheData = [list(tup) for tup in cr.fetchall()]
        db.close()
        db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\Workers.db")
        cr = db.cursor()
        cr.execute(f"SELECT * FROM Wo{CID}")
        WData = [list(tup) for tup in cr.fetchall()]
        db.close()
        return render_template('Show Worker Data.html' , title="Show Worker Data" , TheData=TheData , WData=WData ,TheFullComapnyName =TheFullComapnyName)
    return render_template('Get Worker Id.html' , title="Get Worker Id" , TheFullComapnyName =TheFullComapnyName)

###################################################################################################################################################
# Factory Section #
###################################################################################################################################################
 
@app.route('/Add_Rents' , methods=['GET', 'POST'])
def Add_Rents():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Amount = request.form.get("Amount")
            Month = request.form.get("Month")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO Rents(Date,Amount,Month) VALUES('{Date}',{Amount},{Month})")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Add Rents.html' , title="Add Rents" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Show_Rents')
def Show_Rents():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM Rents")
    TheData = [list(tup) for tup in cr.fetchall()]
    db.close()
    return render_template('Show Rents.html' , title="Show Rents" , Rents=[TheData] ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_GovernPayments' , methods=['GET', 'POST'])
def Add_GovernPayments():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Amount = request.form.get("Amount")
            Type = request.form.get("For")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO GovernPayments(Date,Amount,Type) VALUES('{Date}',{Amount},'{Type}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Add GovernPayments.html' , title="Add GovernPayments" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Show_GovernPayments')
def Show_GovernPayments():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM GovernPayments")
    TheData = [list(tup) for tup in cr.fetchall()]
    db.close()
    return render_template('Show GovernPayments.html' , title="Show GovernPayments" , GovernPayments=[TheData] ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_FPayments' , methods=['GET', 'POST'])
def Add_FPayments():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Amount = request.form.get("Amount")
            For = request.form.get("For")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO Payments(Date,Amount,For) VALUES('{Date}',{Amount},'{For}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Add FPayments.html' , title="Add Factory Payments" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Show_FPayments')
def Show_FPayments():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM Payments")
    TheData = [list(tup) for tup in cr.fetchall()]
    db.close()
    return render_template('Show FPayments.html' , title="Show Factory Payments" , Payments=[TheData] ,TheFullComapnyName =TheFullComapnyName)

###################################################################################################################################################
# Home Section #
###################################################################################################################################################

@app.route('/Add_HRents' , methods=['GET', 'POST'])
def Add_HRents():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Amount = request.form.get("Amount")
            Month = request.form.get("Month")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO HRents(Date,Amount,Month) VALUES('{Date}',{Amount},{Month})")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Add HRents.html' , title="Add HRents" ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Show_HRents')
def Show_HRents():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT  * FROM HRents")
    TheData = [list(tup) for tup in cr.fetchall()]
    db.close()
    return render_template('Show HRents.html' , title="Show HRents" , HRents=[TheData] ,TheFullComapnyName = TheFullComapnyName)

@app.route('/Add_HGovernPayments' , methods=['GET', 'POST'])
def Add_HGovernPayments():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Amount = request.form.get("Amount")
            Type = request.form.get("For")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO HGovernPayments(Date,Amount,Type) VALUES('{Date}',{Amount},'{Type}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Add HGovernPayments.html' , title="Add HGovernPayments" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Show_HGovernPayments')
def Show_HGovernPayments():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM HGovernPayments")
    TheData = [list(tup) for tup in cr.fetchall()]
    db.close()
    return render_template('Show HGovernPayments.html' , title="Show HGovernPayments" , HGovernPayments=[TheData] ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Add_HSchoolPayments' , methods=['GET', 'POST'])
def Add_HSchoolPayments():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Amount = request.form.get("Amount")
            Type = request.form.get("For")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO HSchoolPayments(Date,Amount,Type) VALUES('{Date}',{Amount},'{Type}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Add HSchoolPayments.html' , title="Add HSchoolPayments" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Show_HSchoolPayments')
def Show_HSchoolPayments():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM HSchoolPayments")
    TheData = [list(tup) for tup in cr.fetchall()]
    db.close()
    return render_template('Show HSchoolPayments.html' , title="Show HSchoolPayments" , HSchoolPayments=[TheData] ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Add_HFPayments' , methods=['GET', 'POST'])
def Add_HFPayments():
    if request.method == "POST":
        try:
            Date = request.form.get("Date")
            Amount = request.form.get("Amount")
            For = request.form.get("For")
            with sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO HPayments(Date,Amount,For) VALUES('{Date}',{Amount},'{For}')")
                con.commit()
        except sqlite3.Error as er:
            print(er)
            print("You Has Error")
        finally:
            con.close()
    return render_template('Add HFPayments.html' , title="Add Home Payments" ,TheFullComapnyName =TheFullComapnyName)

@app.route('/Show_HFPayments')
def Show_HFPayments():
    db = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\System.db")
    cr = db.cursor()
    cr.execute("SELECT * FROM HPayments")
    TheData = [list(tup) for tup in cr.fetchall()]
    db.close()
    return render_template('Show HFPayments.html' , title="Show Home Payments" , HPayments=[TheData] ,TheFullComapnyName = TheFullComapnyName)

###################################################################################################################################################
# Running Setion #
###################################################################################################################################################

if __name__  == "__main__":
    #webview.start()
    app.run()