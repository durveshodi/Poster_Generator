from PIL import Image, ImageDraw, ImageFont 

class Poster:
    def __init__(self):
        
        self.BG_height = 624
        self.BG_width = 1195

        self.Base_image =  Image.new("RGBA", (self.BG_width, self.BG_height), color="#00000000")
        self.Upper_Layer = self.Base_image.copy()
        
        self.Draw = ImageDraw.Draw(self.Upper_Layer)
        
        # =============================================================================================
        layer0 = Image.open("image\image_1.png").convert("RGBA")
        layer1 = Image.open("image\image_2.png").convert("RGBA")
        layer2 = Image.open("image\image_3.png").convert("RGBA").resize((layer1.size[0] ,layer1.size[1]+2))
        layer3 = Image.open("image\image_4.png").convert("RGBA")
        layer4 = Image.open("image\image_5.png").convert("RGBA")
        
        anime_img_weight , anime_img_height = layer0.size
        layer0 = layer0.resize((anime_img_weight, anime_img_height))
        
        self.Base_image.paste(layer0, (self.BG_width - anime_img_weight, self.BG_height -  anime_img_height))
        self.Base_image.paste(layer1,(0,0),layer1)
        self.Base_image.paste(layer2,(0,0),layer2)
        self.Base_image.paste(layer3,( 642 ,self.BG_height- layer4.size[0]),layer3)
        self.Base_image.paste(layer4,(0,0),layer4)
        
    def Text(self, text , font):
        self.Draw.text((73,99), 
           text=text,
        #  align="center",
          #anchor="nw",
           fill="#FFFFFFFF", 
           font=font
          ) 
   
    
    def ADD_Genres(self, x, y, genres_list): 

        weights = x
        height = y 
        nweights = 0
        text_width = x
        lines = 1
        
        font = ImageFont.truetype("arial.ttf", 20)
        
        def Genres( x, y, text):

            text_width, text_height = self.Draw.textsize(text, font=font)

            circle = Image.open("image\image_6.png").convert('RGBA')
            circle_width, circle_height = circle.size
            cs = circle.crop((0, 0, circle_width // 2, circle_height))
            ce = circle.crop((circle_width // 2 , 0, circle_width, circle_height))
                
            rectangle = Image.new("RGBA", (text_width, circle_height), color="#3BFE00")
           
            bg = Image.new("RGBA", (circle_width + text_width, circle_height), color="#ffffff00")
            bg.paste(cs, (0,0))
            bg.paste(rectangle, (circle_width // 2 ,0))
            bg.paste(ce, (circle_width // 2 + text_width ,0))
            
            draw = ImageDraw.Draw(bg)
            draw.text((circle_width//2 , (text_height-8)//2), 
                      text=text,
                    # align="center",
                      #anchor="nw",
                      fill="#000000", 
                      font=font
                      )   
            
            self.Upper_Layer.paste(bg, ( x + 18,y),bg)
            return text_width + 18  
    
      
        for genres in genres_list: 
            text_width += self.Draw.textsize(genres, font=font)[0] + 36
            if lines == 1:
                if text_width < 750:
                    nweights = Genres( weights, height,genres)
                weights += nweights + 25
                if weights > 700:
                    lines = 2
                    height += 44
                    weights = 68.0
                    text_width = 0
            elif lines == 2:
                if text_width < 750:
                    nweights = Genres( weights, height, genres)
                weights += nweights + 25
                if weights > 700:
                    height += 44
                    weights = 68.0
                    text_width = 0
                    lines = 3
            elif lines == 3:
                if text_width < 750:
                    nweights = Genres(weights, height, genres)
                weights += nweights + 25
                if weights > 700:
                    text_width = 0
                    break
                
    def addStudio(self, text):

        font = ImageFont.truetype("./text/NotoSerifTelugu-Bold.ttf", 20)
        text_width, text_height = self.Draw.textsize(text, font=font)
        
        rectangle = Image.new("RGBA", (text_width +8, 32), color="#3BFE00")
        self.Upper_Layer.paste(rectangle,(73,236),rectangle)
        
        self.Draw.text((73 +  4 ,236 + (32 - text_height)//2), 
                  text=text,
                #   align="center",
                  #anchor="nw",
                  fill="#000000", 
                  font=font
                  ) 
    
    def addSPrem(self, text):

        font = ImageFont.truetype("./text/NotoSerifTelugu-Bold.ttf", 20)
        text_width, text_height = self.Draw.textsize(text, font=font)
        
        rectangle = Image.new("RGBA", (text_width +8, 32), color="#3BFE00")
        self.Upper_Layer.paste(rectangle,(73,162),rectangle)
        
        self.Draw.text((73 +  4 ,162 + (32 - text_height)//2), 
                  text=text,
                #   align="center",
                  #anchor="nw",
                  fill="#000000", 
                  font=font
                  ) 
        
    def addNameandSeason(self,name,season):

       font = ImageFont.truetype("./text/NotoSerifTelugu-Bold.ttf", 54)
       text_width, text_height = self.Draw.textsize(name, font=font)
       self.Draw.text((73,106), 
                 text=name,
                 fill="#FFFFFFFF", 
                 font=font
                 ) 
       
   
       font = ImageFont.truetype("./text/NotoSerifTelugu-Bold.ttf", 30)
       text = f"Season {season}"
       text_width, text_height = self.Draw.textsize(text, font=font)
       self.Draw.text((73,198), 
                 text=text,
                 fill="#FFFFFFFF", 
                 font=font
                 ) 

        
        
    
    def main(self):
        self.addNameandSeason("Attack on Titan " , 2)
        genres_text = "Action, Adventure, Fantasy, Magic, Supernatural"
        genres_list = genres_text.split(", ")
        self.ADD_Genres(68 , 479 , genres_list)
        
        self.addStudio("WIT Studio")
        self.addSPrem("Spring 2013          Episode 12")
        self.Base_image.paste(self.Upper_Layer,(0,0),self.Upper_Layer)
        self.Base_image.show()


Posters = Poster()
Posters.main()