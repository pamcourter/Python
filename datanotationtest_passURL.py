import pandas as pd
import requests
import sys

def DecodeMessage(argURL):
   url = argURL   
    
   response = pd.read_html(url, header=0, encoding='utf-8')   
   grid_gd = response[0]   

   coorMap = {}
   for index, row in grid_gd.iterrows(): 
      coorMap[(int(row['x-coordinate']), int(row['y-coordinate']))] = row['Character']   

   max_xcor = grid_gd['x-coordinate'].max()
   max_ycor = grid_gd['y-coordinate'].max()

   for y in range(0, max_ycor +1): 
      print("\n")         
      for x in range(0,max_xcor+1):       
         if(x,y) in coorMap:            
            print(coorMap[(x,y)], end="" ) 
         else:
           print(" ", end="") 

def main():  
   url = input("Please enter the URL") 
   
   DecodeMessage(url)

if __name__ == "__main__":
    main()