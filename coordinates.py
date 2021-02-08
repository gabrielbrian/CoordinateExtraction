import tkinter as tk
import csv
import os
from exif import Image

root = tk.Tk()

def getLoc():
	text_box.delete(1.0, "end-1c")
	Dir = Picfolder_entry.get()
	text_box.insert('1.0',"      -------coordinates-------")
	def dms_to_dd(gps_coords, gps_coords_ref):
	    d, m, s =  gps_coords
	    dd = d + m / 60 + s / 3600
	    if gps_coords_ref.upper() in ('S', 'W'):
	        return -dd
	    elif gps_coords_ref.upper() in ('N', 'E'):
	        return dd
	    else:
	        raise RuntimeError('Incorrect gps_coords_ref {}'.format(gps_coords_ref))
	        
	for pic in os.listdir(Dir):
	    fullpath = os.path.join(Dir,pic)       
	    with open(fullpath, 'rb') as image_file:
	        my_image = Image(image_file)
	                
	        latitude_final = dms_to_dd(my_image.gps_latitude, my_image.gps_latitude_ref)
	        longitude_final = dms_to_dd(my_image.gps_longitude, my_image.gps_longitude_ref)
	                
	        complete = latitude_final,longitude_final
	        text_box.insert('end','\n')
	        text_box.insert('end',complete)
		

root.title('PhotoCalculator')
root.geometry("400x450") 
root.resizable(0, 0)

background_image = tk.PhotoImage(file='Plane.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

text_box = tk.Text(root, width = 40, height = 16,borderwidth=3)
text_box.place(x=40,y=150)

Picfolder = tk.Label(root,font=("Courier", 8),bg="#C5F0CE",text="Folder path :",bd = 2)
Picfolder.place(x=50,y=50)
Picfolder_entry = tk.Entry(root,bd = 2)
Picfolder_entry.place(x=150,y=50,width=200)

Get_location = tk.Button(root, text = "Get coordinates",font=("Courier", 12,"bold"),bg="#F2DDEC",activebackground = "grey",command = getLoc)
Get_location.place(width="140px",x = 100 , y = 100)


root.mainloop()



