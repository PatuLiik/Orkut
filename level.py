import wall
import character

def level_create(level, lay1, lay2, lay3, player1):
    if level == 0: #---LEVEL 0---#
        walls = []
        walls.append(wall.WallObject(50, 200, 200, 70))#0
        walls.append(wall.WallObject(150, 150, 50, 220))#1
        walls.append(wall.WallObject(300, 180, 100, 90))#2
        walls.append(wall.WallObject(340, 50, 70, 30))#3

        for walls in walls: #võtab kõik objectid walls listist
            walls.draw(lay1)#joonistab layer ühele ehk screenile
            player1.collide(walls.rectangle)#collison
        
        
        
    
