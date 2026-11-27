import pygame
class background:
    def __init__(self):
        self.back1 = pygame.image.load('backgroundImg/Sprite-0001.png').convert()
        self.back2 = pygame.image.load('backgroundImg/Sprite-0002.png').convert()
        self.back3 = pygame.image.load('backgroundImg/Sprite-0003.png').convert()
        self.back4 = pygame.image.load('backgroundImg/Sprite-0004.png').convert()
        self.back5 = pygame.image.load('backgroundImg/Sprite-0005.png').convert()
        self.back6 = pygame.image.load('backgroundImg/Sprite-0006.png').convert()
        self.back7 = pygame.image.load('backgroundImg/Sprite-0007.png').convert()
        self.castle1 = pygame.image.load('backgroundImg/castle1.png').convert()
        self.castle2 = pygame.image.load('backgroundImg/castle2.png').convert()
        self.castle3 = pygame.image.load('backgroundImg/castle3.png').convert()
        self.castle4 = pygame.image.load('backgroundImg/castle4.png').convert()
        self.castle5 = pygame.image.load('backgroundImg/castle5.png').convert()
        self.castle6 = pygame.image.load('backgroundImg/castle6.png').convert()
        self.mountain1 = pygame.image.load('backgroundImg/Mountain1.png').convert()
        self.mountain2 = pygame.image.load('backgroundImg/Mountain2.png').convert()
        self.mountain3 = pygame.image.load('backgroundImg/Mountain3.png').convert()
        self.mountain4 = pygame.image.load('backgroundImg/Mountain4.png').convert()
        self.mountain5 = pygame.image.load('backgroundImg/Mountain5.png').convert()
        self.mountain6 = pygame.image.load('backgroundImg/Mountain6.png').convert()
        self.mountain7 = pygame.image.load('backgroundImg/Mountain7.png').convert()
        self.mountain8 = pygame.image.load('backgroundImg/Mountain8.png').convert()
        self.mountain9 = pygame.image.load('backgroundImg/Mountain9.png').convert()
        self.mountain10 = pygame.image.load('backgroundImg/Mountain10.png').convert()
        self.bottom1 = pygame.image.load('backgroundImg/bottom1.png').convert()
        self.bottom2 = pygame.image.load('backgroundImg/bottom2.png').convert()
        self.bottom3 = pygame.image.load('backgroundImg/bottom3.png').convert()
        self.bottom4 = pygame.image.load('backgroundImg/bottom4.png').convert()
        self.closed1 = pygame.image.load('backgroundImg/closed1.png').convert()
        self.closed2 = pygame.image.load('backgroundImg/closed2.png').convert()
        self.closed3 = pygame.image.load('backgroundImg/closed3.png').convert()
        self.factoryDestroyed = pygame.image.load('backgroundImg/factoryDestroyed.png').convert()
        self.reactor1 = pygame.image.load('backgroundImg/reactor1.png')

    def draw(self, screen, currentBackgroundReq):
        currentBack = None
        if currentBackgroundReq == 'back1':
            currentBack = self.back1
        if currentBackgroundReq == 'back2':
            currentBack = self.back2
        if currentBackgroundReq == 'back3':
            currentBack = self.back3
        if currentBackgroundReq == 'back4':
            currentBack = self.back4
        if currentBackgroundReq == 'back5':
            currentBack = self.back5
        if currentBackgroundReq == 'back6':
            currentBack = self.back6
        if currentBackgroundReq == 'back7':
            currentBack = self.back7
        if currentBackgroundReq == 'Castle1' or currentBackgroundReq == 'Castle':
            currentBack = self.castle1
        if currentBackgroundReq == 'Castle2':
            currentBack = self.castle2
        if currentBackgroundReq == 'Castle3':
            currentBack = self.castle3
        if currentBackgroundReq == 'Castle4':
            currentBack = self.castle4
        if currentBackgroundReq == 'Castle5' or currentBackgroundReq == 'Castle0':
            currentBack = self.castle5
        if currentBackgroundReq == 'Castle6':
            currentBack = self.castle6     
        if currentBackgroundReq == 'Mountain1':
            currentBack = self.mountain1
        if currentBackgroundReq == 'Mountain2':
            currentBack = self.mountain2 
        if currentBackgroundReq == 'Mountain3':
            currentBack = self.mountain3 
        if currentBackgroundReq == 'Mountain4':
            currentBack = self.mountain4 
        if currentBackgroundReq == 'Mountain5':
            currentBack = self.mountain5 
        if currentBackgroundReq == 'Mountain6':
            currentBack = self.mountain6 
        if currentBackgroundReq == 'Mountain7':
            currentBack = self.mountain7 
        if currentBackgroundReq == 'Mountain8':
            currentBack = self.mountain8 
        if currentBackgroundReq == 'Mountain9':
            currentBack = self.mountain9 
        if currentBackgroundReq == 'Mountain10':
            currentBack = self.mountain10 
        if currentBackgroundReq == 'Bottom1':
            currentBack = self.bottom1
        if currentBackgroundReq == 'Bottom2':
            currentBack = self.bottom2
        if currentBackgroundReq == 'Bottom3':
            currentBack = self.bottom3
        if currentBackgroundReq == 'Bottom4':
            currentBack = self.bottom4
        if currentBackgroundReq == 'FactoryDestroyed':
            currentBack = self.factoryDestroyed
        if currentBackgroundReq == 'Closed1':
            currentBack = self.closed1
        if currentBackgroundReq== 'Closed2':
            currentBack = self.closed2
        if currentBackgroundReq == 'Closed3':
            currentBack = self.closed3
        if currentBackgroundReq == 'Reactor1':
            currentBack = self.reactor1

        # ill chage these to reactor2 and reactor3 once i have made those assets
        if currentBackgroundReq == 'Reactor2':
            currentBack = self.reactor1
        if currentBackgroundReq == 'Reactor3':
            currentBack = self.reactor1  
         
        screen.blit(currentBack, (0, 0))

    def collision(self, currentBackgroundReq, player):
        if currentBackgroundReq == 'Mountain1':
            slope_start_x = 222 
            slope_end_x = 0     
            start_y = 600      
            end_y = 290  

           
            if slope_end_x <= player.x <= slope_start_x:
                
                rise = end_y - start_y
                run = slope_end_x - slope_start_x  
                slope_gradient = rise / run

               
                current_x_offset = player.x - slope_start_x  
                ground_y = start_y + (slope_gradient * current_x_offset)

                if player.y + 80 >= ground_y: 
                    player.y = ground_y - 80
                    player.y_velocity = 0
                    player.is_jumping = False

        if currentBackgroundReq == 'Mountain2':
            slope_start_x = 800
            slope_end_x = 0     
            start_y = 590      
            end_y = 340  

           
            if slope_end_x <= player.x <= slope_start_x:
                
                rise = end_y - start_y
                run = slope_end_x - slope_start_x  
                slope_gradient = rise / run

               
                current_x_offset = player.x - slope_start_x  
                ground_y = start_y + (slope_gradient * current_x_offset)

                if player.y + 80 >= ground_y: 
                    player.y = ground_y - 80
                    player.y_velocity = 0
                    player.is_jumping = False

        if currentBackgroundReq == 'Mountain3':
            slope_start_x = 200
            slope_end_x = 0     
            start_y = 600      
            end_y = 472  

           
            if slope_end_x <= player.x <= slope_start_x:
                
                rise = end_y - start_y
                run = slope_end_x - slope_start_x  
                slope_gradient = rise / run

               
                current_x_offset = player.x - slope_start_x  
                ground_y = start_y + (slope_gradient * current_x_offset)

                if player.y + 80 >= ground_y: 
                    player.y = ground_y - 80
                    player.y_velocity = 0
                    player.is_jumping = False

        if currentBackgroundReq == 'Mountain4':
            slope_start_x = 730 
            slope_end_x = 0     
            start_y = 610      
            end_y = 300  

           
            if slope_end_x <= player.x <= slope_start_x:
                
                rise = end_y - start_y
                run = slope_end_x - slope_start_x  
                slope_gradient = rise / run

               
                current_x_offset = player.x - slope_start_x  
                ground_y = start_y + (slope_gradient * current_x_offset)

                if player.y + 80 >= ground_y: 
                    player.y = ground_y - 80
                    player.y_velocity = 0
                    player.is_jumping = False

        if currentBackgroundReq == 'Mountain5':
            slope_start_x = 672 
            slope_end_x = 0     
            start_y = 610      
            end_y = 350 

           
            if slope_end_x <= player.x <= slope_start_x:
                
                rise = end_y - start_y
                run = slope_end_x - slope_start_x  
                slope_gradient = rise / run

               
                current_x_offset = player.x - slope_start_x  
                ground_y = start_y + (slope_gradient * current_x_offset)

                if player.y + 80 >= ground_y: 
                    player.y = ground_y - 80
                    player.y_velocity = 0
                    player.is_jumping = False

        if currentBackgroundReq == 'Mountain6':
            slope_start_x = 552 
            slope_end_x = 216     
            start_y = 610      
            end_y = 300 

            
            if slope_end_x <= player.x <= slope_start_x:
                
                rise = end_y - start_y
                run = slope_end_x - slope_start_x  
                slope_gradient = rise / run

                
                current_x_offset = player.x - slope_start_x  
                ground_y = start_y + (slope_gradient * current_x_offset)

                if player.y + 80 >= ground_y: 
                    player.y = ground_y - 80
                    player.y_velocity = 0
                    player.is_jumping = False

            slope_start_x = 216 
            slope_end_x = 0     
            start_y = 300      
            end_y = 300 

            
            if slope_end_x <= player.x <= slope_start_x:
                
                rise = end_y - start_y
                run = slope_end_x - slope_start_x  
                slope_gradient = rise / run

                
                current_x_offset = player.x - slope_start_x  
                ground_y = start_y + (slope_gradient * current_x_offset)

                if player.y + 80 >= ground_y: 
                    player.y = ground_y - 80
                    player.y_velocity = 0
                    player.is_jumping = False

        if currentBackgroundReq == 'Mountain7':
            slope_start_x = 800 
            slope_end_x = 300
            start_y = 610      
            end_y = 470 

            
            if slope_end_x <= player.x <= slope_start_x:
                
                rise = end_y - start_y
                run = slope_end_x - slope_start_x  
                slope_gradient = rise / run

                
                current_x_offset = player.x - slope_start_x  
                ground_y = start_y + (slope_gradient * current_x_offset)

                if player.y + 80 >= ground_y: 
                    player.y = ground_y - 80
                    player.y_velocity = 0
                    player.is_jumping = False

            slope_start_x = 300
            slope_end_x = 0 
            start_y = 470    
            end_y = 250

            
            if slope_end_x <= player.x <= slope_start_x:
                
                rise = end_y - start_y
                run = slope_end_x - slope_start_x  
                slope_gradient = rise / run

                
                current_x_offset = player.x - slope_start_x  
                ground_y = start_y + (slope_gradient * current_x_offset)

                if player.y + 80 >= ground_y: 
                    player.y = ground_y - 80
                    player.y_velocity = 0
                    player.is_jumping = False