from graphics import *

def getConfiguration():

    # set defaults
    settings = {
             "player1" : "User",
             "player2" : "CPU",
        "player1color" : "Red",
        "player2color" : "Yellow",
           "algorithm" : "alphabeta",
          "boardStyle" : "Wood"
    }
    
    size = 400
    winStart = GraphWin("Configuration",size,size)
    rect = Rectangle(Point(0,0),Point(size,size))
    rect.setOutline("white")
    rect.setFill("Silver")
    rect.draw(winStart)

    # labels
    line1 = Line(Point(size/2+5,60),Point(size/2+5,size/2-25))
    line1.setWidth(2)
    line1.draw(winStart)

    line2 = Line(Point(1,1),Point(size-1,1))
    line2.setWidth(2)
    line2.draw(winStart)

    line3 = Line(Point(1,size-1),Point(size,size-1))
    line3.setWidth(4)
    line3.draw(winStart)

    line4 = Line(Point(size-1,1),Point(size-1,size-1))
    line4.setWidth(4)
    line4.draw(winStart)

    line5 = Line(Point(1,1),Point(1,size-1))
    line5.setWidth(2)
    line5.draw(winStart)

    textBox_settings = Text(Point(size/2,20),"SETTINGS")
    textBox_settings.setFace("helvetica")
    textBox_settings.setStyle("bold")
    textBox_settings.setSize(24)
    textBox_settings.setTextColor("Black")
    textBox_settings.draw(winStart)

    line6 = Line(Point(1,40),Point(size,40))
    line6.setWidth(2)
    line6.draw(winStart)

    textBox_player1 = Text(Point(size/2-100,80),"Player 1\n______________")
    textBox_player1.setFace("helvetica")
    textBox_player1.setStyle("bold italic")
    textBox_player1.setSize(22)
    textBox_player1.setTextColor("Black")
    textBox_player1.draw(winStart)

    textBox_player2 = Text(Point(size/2+100,80),"Player 2\n______________")
    textBox_player2.setFace("helvetica")
    textBox_player2.setStyle("bold italic")
    textBox_player2.setSize(22)
    textBox_player2.setTextColor("Black")
    textBox_player2.draw(winStart)

    # selections
    textBox_player1USER = Text(Point(size/2-130,125),"User")
    textBox_player1USER.setFace("helvetica")
    textBox_player1USER.setStyle("bold")
    textBox_player1USER.setSize(20)
    textBox_player1USER.setTextColor("Azure")
    textBox_player1USER.draw(winStart)

    textBox_player1CPU = Text(Point(size/2-75,125),"CPU")
    textBox_player1CPU.setFace("helvetica")
    textBox_player1CPU.setSize(20)
    textBox_player1CPU.setTextColor("Black")
    textBox_player1CPU.draw(winStart)

    textBox_player2USER = Text(Point(size/2+75,125),"User")
    textBox_player2USER.setFace("helvetica")
    textBox_player2USER.setSize(20)
    textBox_player2USER.setTextColor("Black")
    textBox_player2USER.draw(winStart)

    textBox_player2CPU = Text(Point(size/2+130,125),"CPU")
    textBox_player2CPU.setFace("helvetica")
    textBox_player2CPU.setStyle("bold")
    textBox_player2CPU.setSize(20)
    textBox_player2CPU.setTextColor("Azure")
    textBox_player2CPU.draw(winStart)

    # colors
    textBox_player1RED = Text(Point(size/2-165,155),"Red")
    textBox_player1RED.setFace("helvetica")
    # textBox_player1RED.setStyle("bold")
    textBox_player1RED.setSize(16)
    textBox_player1RED.setTextColor("Red")
    textBox_player1RED.draw(winStart)

    textBox_player1BLUE = Text(Point(size/2-125,155),"Blue")
    textBox_player1BLUE.setFace("helvetica")
    textBox_player1BLUE.setSize(16)
    textBox_player1BLUE.setTextColor("Black")
    textBox_player1BLUE.draw(winStart)

    textBox_player1YELLOW = Text(Point(size/2-80,155),"Yellow")
    textBox_player1YELLOW.setFace("helvetica")
    textBox_player1YELLOW.setSize(16)
    textBox_player1YELLOW.setTextColor("Black")
    textBox_player1YELLOW.draw(winStart)

    textBox_player1GREEN = Text(Point(size/2-30,155),"Green")
    textBox_player1GREEN.setFace("helvetica")
    textBox_player1GREEN.setSize(16)
    textBox_player1GREEN.setTextColor("Black")
    textBox_player1GREEN.draw(winStart)

    textBox_player2RED = Text(Point(size/2+30,155),"Red")
    textBox_player2RED.setFace("helvetica")
    textBox_player2RED.setSize(16)
    textBox_player2RED.setTextColor("Black")
    textBox_player2RED.draw(winStart)

    textBox_player2BLUE = Text(Point(size/2+70,155),"Blue")
    textBox_player2BLUE.setFace("helvetica")
    textBox_player2BLUE.setSize(16)
    textBox_player2BLUE.setTextColor("Black")
    textBox_player2BLUE.draw(winStart)

    textBox_player2YELLOW = Text(Point(size/2+115,155),"Yellow")
    textBox_player2YELLOW.setFace("helvetica")
    # textBox_player2YELLOW.setStyle("bold")
    textBox_player2YELLOW.setSize(16)
    textBox_player2YELLOW.setTextColor("Yellow")
    textBox_player2YELLOW.draw(winStart)

    textBox_player2GREEN = Text(Point(size/2+165,155),"Green")
    textBox_player2GREEN.setFace("helvetica")
    textBox_player2GREEN.setSize(16)
    textBox_player2GREEN.setTextColor("Black")
    textBox_player2GREEN.draw(winStart)

    line7 = Line(Point(1,180),Point(size,180))
    line7.setWidth(2)
    line7.draw(winStart)

    # algorithm (prune switch)
    textBox_algorithm = Text(Point(size/2,200),"Algorithm")
    textBox_algorithm.setFace("helvetica")
    textBox_algorithm.setStyle("bold italic")
    textBox_algorithm.setSize(22)
    textBox_algorithm.setTextColor("Black")
    textBox_algorithm.draw(winStart)

    textBox_minimax = Text(Point(size/2-50,230),"Minimax")
    textBox_minimax.setFace("helvetica")
    textBox_minimax.setSize(18)
    textBox_minimax.setTextColor("Black")
    textBox_minimax.draw(winStart)

    textBox_alphabetapruning = Text(Point(size/2+50,230),"\u03B1-\u03B2 Pruning")
    textBox_alphabetapruning.setFace("helvetica")
    textBox_alphabetapruning.setSize(18)
    textBox_alphabetapruning.setTextColor("Azure")
    textBox_alphabetapruning.draw(winStart)

    line8 = Line(Point(1,250),Point(size,250))
    line8.setWidth(2)
    line8.draw(winStart)

    # board graphic
    textBox_bkgnd = Text(Point(size/2,270),"Board Style")
    textBox_bkgnd.setFace("helvetica")
    textBox_bkgnd.setStyle("bold italic")
    textBox_bkgnd.setSize(22)
    textBox_bkgnd.setTextColor("Black")
    textBox_bkgnd.draw(winStart)

    textBox_bkgndWOOD = Text(Point(size/2-115,300),"Wood")
    textBox_bkgndWOOD.setFace("helvetica")
    textBox_bkgndWOOD.setStyle("bold")
    textBox_bkgndWOOD.setSize(18)
    textBox_bkgndWOOD.setTextColor("Peru")
    textBox_bkgndWOOD.draw(winStart)

    textBox_bkgndBLUE = Text(Point(size/2-55,300),"Blue")
    textBox_bkgndBLUE.setFace("helvetica")
    textBox_bkgndBLUE.setStyle("bold")
    textBox_bkgndBLUE.setSize(18)
    textBox_bkgndBLUE.setTextColor("Black")
    textBox_bkgndBLUE.draw(winStart)

    textBox_bkgndOLIVE = Text(Point(size/2+5,300),"Olive")
    textBox_bkgndOLIVE.setFace("helvetica")
    textBox_bkgndOLIVE.setStyle("bold")
    textBox_bkgndOLIVE.setSize(18)
    textBox_bkgndOLIVE.setTextColor("Black")
    textBox_bkgndOLIVE.draw(winStart)

    textBox_bkgndGOLD = Text(Point(size/2+70,300),"Gold")
    textBox_bkgndGOLD.setFace("helvetica")
    textBox_bkgndGOLD.setStyle("bold")
    textBox_bkgndGOLD.setSize(18)
    textBox_bkgndGOLD.setTextColor("Black")
    textBox_bkgndGOLD.draw(winStart)

    textBox_bkgndCLAY = Text(Point(size/2+130,300),"Clay")
    textBox_bkgndCLAY.setFace("helvetica")
    textBox_bkgndCLAY.setStyle("bold")
    textBox_bkgndCLAY.setSize(18)
    textBox_bkgndCLAY.setTextColor("Black") # Indian Red
    textBox_bkgndCLAY.draw(winStart)

    line6 = Line(Point(1,319),Point(size,319))
    line6.setWidth(2)
    line6.draw(winStart)

    # start button
    rect_start1 = Rectangle(Point(size/2-90,330),Point(size/2+100,380))
    rect_start1.setFill("Light Gray")
    rect_start1.draw(winStart)

    textBox_start1 = Text(Point(size/2+5,355),"START")
    textBox_start1.setStyle("bold")
    textBox_start1.setTextColor("Dark Green")
    textBox_start1.setSize(34)
    textBox_start1.draw(winStart)

    textBox_start2 = Text(Point(size/2+5,355),"S T A R T")
    # textBox_start2.setStyle("bold")
    textBox_start2.setTextColor("Green")
    textBox_start2.setSize(24)
    textBox_start2.draw(winStart)


    # RUNNING...
    configured = False
    while configured == False:

        click = winStart.getMouse()

        # P1 User - Point(size/2-130,125)
        if click.getX()>size/2-150 and click.getX()<size/2-110 and click.getY()>115 and click.getY()<135:
            settings["player1"] = "User"
            textBox_player1USER.setTextColor("Azure")
            textBox_player1USER.setStyle("bold")
            textBox_player1CPU.setTextColor("Black")
            textBox_player1CPU.setStyle("normal")
        # P1 CPU - Point(size/2-75,125)
        if click.getX()>size/2-95 and click.getX()<size/2-55 and click.getY()>115 and click.getY()<135:
            settings["player1"] = "CPU"
            textBox_player1CPU.setTextColor("Azure")
            textBox_player1CPU.setStyle("bold")
            textBox_player1USER.setTextColor("Black")
            textBox_player1USER.setStyle("normal")

        # P2 User - Point(size/2+75,125)
        if click.getX()>size/2+55 and click.getX()<size/2+95 and click.getY()>115 and click.getY()<135:
            settings["player2"] = "User"
            textBox_player2USER.setTextColor("Azure")
            textBox_player2USER.setStyle("bold")
            textBox_player2CPU.setTextColor("Black")
            textBox_player2CPU.setStyle("normal")
        # P2 CPU - Point(size/2+130,125)
        if click.getX()>size/2+110 and click.getX()<size/2+150 and click.getY()>115 and click.getY()<135:
            settings["player2"] = "CPU"
            textBox_player2CPU.setTextColor("Azure")
            textBox_player2CPU.setStyle("bold")
            textBox_player2USER.setTextColor("Black")
            textBox_player2USER.setStyle("normal")


        # P1 RED - Point(size/2-165,155)
        if click.getX()>size/2-180 and click.getX()<size/2-150 and click.getY()>148 and click.getY()<162:
            settings["player1color"] = "Red"
            textBox_player1RED.setTextColor("Red")
            textBox_player1GREEN.setTextColor("Black")
            textBox_player1YELLOW.setTextColor("Black")
            textBox_player1BLUE.setTextColor("Black")
        # P1 BLUE - Point(size/2-125,155)
        if click.getX()>size/2-140 and click.getX()<size/2-110 and click.getY()>148 and click.getY()<162:
            settings["player1color"] = "Blue"
            textBox_player1RED.setTextColor("Black")
            textBox_player1GREEN.setTextColor("Black")
            textBox_player1YELLOW.setTextColor("Black")
            textBox_player1BLUE.setTextColor("Blue")
        # P1 YELLOW - Point(size/2-80,155)
        if click.getX()>size/2-95 and click.getX()<size/2-65 and click.getY()>148 and click.getY()<162:
            settings["player1color"] = "Yellow"
            textBox_player1RED.setTextColor("Black")
            textBox_player1GREEN.setTextColor("Black")
            textBox_player1YELLOW.setTextColor("Yellow")
            textBox_player1BLUE.setTextColor("Black")
        # P1 GREEN - Point(size/2-30,155)
        if click.getX()>size/2-45 and click.getX()<size/2-15 and click.getY()>148 and click.getY()<162:
            settings["player1color"] = "Green"
            textBox_player1RED.setTextColor("Black")
            textBox_player1GREEN.setTextColor("Green")
            textBox_player1YELLOW.setTextColor("Black")
            textBox_player1BLUE.setTextColor("Black")
        
        # P2 RED - Point(size/2+30,155)
        if click.getX()>size/2+15 and click.getX()<size/2+45 and click.getY()>148 and click.getY()<162:
            settings["player2color"] = "Red"
            textBox_player2RED.setTextColor("Red")
            textBox_player2GREEN.setTextColor("Black")
            textBox_player2YELLOW.setTextColor("Black")
            textBox_player2BLUE.setTextColor("Black")
        # P2 BLUE - Point(size/2+70,155)
        if click.getX()>size/2+55 and click.getX()<size/2+85 and click.getY()>148 and click.getY()<162:
            settings["player2color"] = "Blue"
            textBox_player2RED.setTextColor("Black")
            textBox_player2GREEN.setTextColor("Black")
            textBox_player2YELLOW.setTextColor("Black")
            textBox_player2BLUE.setTextColor("Blue")
        # P2 YELLOW - Point(size/2+115,155)
        if click.getX()>size/2+100 and click.getX()<size/2+130 and click.getY()>148 and click.getY()<162:
            settings["player2color"] = "Yellow"
            textBox_player2RED.setTextColor("Black")
            textBox_player2GREEN.setTextColor("Black")
            textBox_player2YELLOW.setTextColor("Yellow")
            textBox_player2BLUE.setTextColor("Black")
        # P2 GREEN - Point(size/2+165,155)
        if click.getX()>size/2+150 and click.getX()<size/2+170 and click.getY()>148 and click.getY()<162:
            settings["player2color"] = "Green"
            textBox_player2RED.setTextColor("Black")
            textBox_player2GREEN.setTextColor("Green")
            textBox_player2YELLOW.setTextColor("Black")
            textBox_player2BLUE.setTextColor("Black")


        # minimax - Point(size/2-50,230)
        if click.getX()>size/2-86 and click.getX()<size/2-14 and click.getY()>212 and click.getY()<247:
            settings["algorithm"] = "minimax"
            textBox_minimax.setTextColor("Azure")
            textBox_minimax.setStyle("bold")
            textBox_alphabetapruning.setTextColor("Black")
            textBox_alphabetapruning.setStyle("normal")

        # alphabeta - Point(size/2+50,230)
        if click.getX()>size/2+3 and click.getX()<size/2+97 and click.getY()>212 and click.getY()<247:
            settings["algorithm"] = "alphabeta"
            textBox_minimax.setTextColor("Black")
            textBox_minimax.setStyle("normal")
            textBox_alphabetapruning.setTextColor("Azure")
            textBox_alphabetapruning.setStyle("bold")


        # WOOD - Point(size/2-115,300)
        if click.getX()>size/2-140 and click.getX()<size/2-90 and click.getY()>280 and click.getY()<320:
            settings["boardStyle"] = "Wood"
            textBox_bkgndBLUE.setTextColor("Black")
            textBox_bkgndCLAY.setTextColor("Black")
            textBox_bkgndGOLD.setTextColor("Black")
            textBox_bkgndOLIVE.setTextColor("Black")
            textBox_bkgndWOOD.setTextColor("Peru")
        # BLUE - Point(size/2-55,300)
        if click.getX()>size/2-75 and click.getX()<size/2-35 and click.getY()>280 and click.getY()<320:
            settings["boardStyle"] = "Blue"
            textBox_bkgndBLUE.setTextColor("Blue")
            textBox_bkgndCLAY.setTextColor("Black")
            textBox_bkgndGOLD.setTextColor("Black")
            textBox_bkgndOLIVE.setTextColor("Black")
            textBox_bkgndWOOD.setTextColor("Black")
        # OLIVE - Point(size/2+5,300)
        if click.getX()>size/2-20 and click.getX()<size/2+30 and click.getY()>280 and click.getY()<320:
            settings["boardStyle"] = "Olive"
            textBox_bkgndBLUE.setTextColor("Black")
            textBox_bkgndCLAY.setTextColor("Black")
            textBox_bkgndGOLD.setTextColor("Black")
            textBox_bkgndOLIVE.setTextColor("Olive")
            textBox_bkgndWOOD.setTextColor("Black")
        # GOLD - Point(size/2+70,300)
        if click.getX()>size/2+45 and click.getX()<size/2+95 and click.getY()>280 and click.getY()<320:
            settings["boardStyle"] = "Gold"
            textBox_bkgndBLUE.setTextColor("Black")
            textBox_bkgndCLAY.setTextColor("Black")
            textBox_bkgndGOLD.setTextColor("Gold")
            textBox_bkgndOLIVE.setTextColor("Black")
            textBox_bkgndWOOD.setTextColor("Black")
        # CLAY - Point(size/2+130,300)
        if click.getX()>size/2+105 and click.getX()<size/2+155 and click.getY()>280 and click.getY()<320:
            settings["boardStyle"] = "Clay"
            textBox_bkgndBLUE.setTextColor("Black")
            textBox_bkgndCLAY.setTextColor("Indian Red")
            textBox_bkgndGOLD.setTextColor("Black")
            textBox_bkgndOLIVE.setTextColor("Black")
            textBox_bkgndWOOD.setTextColor("Black")


        # "START"
        if click.getX()>size/2-90 and click.getX()<size/2+100 and click.getY()>330 and click.getY()<380:
            if settings["player1color"] == settings["player2color"]:
                errorWin = GraphWin("ERROR",400,50)
                rect = Rectangle(Point(0,0),Point(400,50))
                rect.setOutline("Magenta")
                rect.setFill("Light Steel Blue")
                rect.draw(errorWin)
                errorText = Text(Point(200,25),"( ! ) ERROR:  Players Cannot Be Same Color")
                errorText.setFace("times roman")
                errorText.setStyle("bold")
                errorText.setSize(18)
                errorText.draw(errorWin)
                winStart.getMouse()
                errorWin.close()
            else:
                configured = True
                winStart.close()
                return settings

    winStart.close()
# --------------------------------- END CONFIGURATION FUNCTION