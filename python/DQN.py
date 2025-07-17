def action():
    env=[[1,1,1,1],
         [1,0,1,1],
         [1,1,0,1],
         [1,1,1,10]]
    point=0
    game_over=False
    while game_over==False:
        for row in env:
            print(row)
            
        row=int(input("Enter row: "))
        col=int(input("Enter column: "))
        
        value=env[row][col]
        
        if value==1:
            point+=1
            print("You moved forward! +1 point")
        elif value==0:
            point-=1
            print("You hit a wall! -1 point")
        elif value==10:
            point+=10
            print("You reached the goal!")
            game_over=True
    print(f"Your total points: {point}")
    
action()
        