from processing import *
import random
import math

#noise_map = [[0]*25]*25
#test_chunk = [[220,220],[[0,0],[0,0],[0,0],[0,0]]]

screen_width = 500
screen_height = 500
seed = random.randint(0,9999)
random_list = [
    478.7, 240.7, 94.9, 191.6, 310.6, 404.0, 445.6, 434.8, 327.5, 232.7, 420.1, 395.0, 267.0, 320.5, 474.4, 128.8, 62.4, 9.4, 57.8, 10.5, 328.7, 43.8, 378.6, 24.5, 123.7, 131.4, 353.2, 260.2, 1.4, 479.2, 13.3, 48.3, 426.0, 116.3, 301.6, 194.5, 401.9, 46.8, 461.7, 150.8, 220.8, 278.6, 203.9, 403.3, 365.0, 251.7, 231.5, 392.9, 41.1, 396.2, 438.7, 155.7, 82.5, 479.6, 315.8, 415.9, 457.2, 92.0, 68.0, 392.0, 220.1, 36.4, 87.0, 433.1, 422.6, 333.4, 448.8, 321.2, 168.0, 446.5, 115.8, 96.1, 56.0, 65.3, 96.7, 197.6, 171.1, 67.9, 405.4, 5.2, 464.4, 421.7, 460.8, 307.7, 142.8, 39.7, 464.6, 88.6, 211.0, 83.5, 144.0, 145.4, 241.1, 295.5, 98.8, 24.0, 285.2, 161.3, 219.7, 24.8, 301.1, 498.5, 270.6, 404.7, 46.4, 30.1, 483.3, 362.5, 242.8, 289.1, 207.6, 238.7, 242.4, 111.0, 91.6, 188.4, 175.4, 268.0, 136.4, 152.0, 398.4, 292.7, 36.8, 373.8, 114.3, 498.2, 375.8, 140.3, 321.2, 116.5, 344.3, 86.5, 59.3, 496.4, 321.3, 90.1, 184.9, 268.0, 191.2, 220.6, 169.3, 465.8, 169.1, 228.9, 412.1, 49.0, 71.1, 183.7, 382.1, 68.9, 214.0, 372.6, 255.4, 205.5, 44.1, 172.0, 259.0, 15.8, 353.7, 21.1, 115.5, 129.1, 84.6, 236.9, 482.2, 438.6, 24.2, 239.3, 390.0, 183.5, 99.8, 400.6, 414.7, 254.9, 202.8, 314.9, 177.3, 131.6, 190.2, 470.8, 217.7, 110.7, 202.0, 345.2, 482.9, 215.0, 465.2, 149.8, 250.8, 269.7, 488.1, 362.9, 114.9, 219.6, 137.3, 188.3, 433.8, 200.4, 199.6, 247.9, 332.2, 142.0, 352.2, 328.4, 403.9, 421.5, 403.0, 264.0, 387.1, 479.9, 216.2, 474.2, 500.0, 109.7, 166.5, 205.2, 419.4, 115.8, 424.7, 69.3, 55.3, 127.3, 152.5, 129.8, 322.5, 103.2, 339.6, 136.1, 0.2, 333.4, 187.9, 400.0, 195.5, 237.5, 383.5, 332.9, 265.0, 355.5, 282.3, 58.1, 136.0, 14.3, 329.3, 368.6, 364.6, 351.3, 114.8, 63.2, 225.3, 372.3, 117.1, 164.2, 481.9, 136.9, 72.5, 82.8, 364.0, 381.1, 194.5, 132.7, 61.1, 119.8, 253.0, 410.3, 47.8, 262.5, 145.0, 351.8, 1.4, 488.8, 100.2, 410.4, 447.2, 297.0, 19.6, 437.8, 33.2, 445.8, 446.3, 9.0, 77.8, 11.0, 388.7, 443.3, 306.2, 281.9, 421.1, 434.1, 428.9, 474.3, 470.5, 499.8, 395.0, 6.1, 14.3, 219.7, 422.6, 27.6, 124.4, 282.5, 391.3, 319.0, 171.7, 274.8, 422.9, 414.8, 145.8, 294.3, 380.3, 11.6, 493.0, 469.8, 333.1, 345.2, 170.3, 396.4, 11.7, 85.2, 358.2, 118.0, 207.1, 147.0, 228.1, 4.5, 371.7, 164.0, 371.6, 107.1, 226.9, 159.0, 488.0, 5.7, 386.9, 426.0, 333.9, 298.1, 250.2, 143.3, 216.5, 35.2, 336.6, 14.3, 308.6, 64.9, 223.6, 289.1, 286.1, 304.7, 413.5, 401.5, 283.1, 212.7, 83.2, 0.9, 135.4, 343.7, 427.3, 361.7, 212.8, 55.2, 293.1, 109.7, 490.8, 392.4, 455.6, 487.0, 276.8, 164.8, 190.2, 387.7, 433.7, 372.9, 323.7, 251.9, 277.9, 394.9, 248.8, 478.8, 293.7, 375.8, 441.2, 259.5, 347.0, 273.3, 296.7, 280.8, 240.4, 194.7, 498.3, 41.5, 30.5, 221.1, 454.0, 404.1, 325.1, 203.6, 4.6, 343.8, 100.6, 483.9, 127.7, 34.0, 270.2, 447.3, 21.7, 178.3, 359.6, 416.1, 244.3, 389.4, 249.7, 13.0, 359.8, 7.4, 220.8, 72.4, 118.0, 403.6, 284.7, 346.1, 448.2, 445.5, 189.3, 402.7, 430.5, 53.2, 238.6, 299.9, 412.5, 253.6, 479.2, 337.3, 362.3, 355.1, 246.6, 32.9, 35.4, 137.4, 459.2, 147.8, 499.4, 316.6, 127.3, 247.1, 496.1, 176.3, 22.1, 159.7, 51.8, 457.5, 80.5, 13.5, 298.6, 345.1, 489.6, 60.0, 225.4, 58.3, 324.5, 479.0, 314.7, 488.8, 19.6, 116.6, 201.8, 327.3, 28.9, 467.7, 77.5, 417.9, 183.1, 354.6, 435.0, 337.7, 73.1, 71.3, 219.6, 480.6, 95.4, 233.2, 283.8, 345.5, 171.7, 97.9, 5.4, 428.2, 359.3, 312.8, 86.4, 153.9, 362.0, 45.0, 408.0, 49.2, 483.1, 325.4, 127.2, 91.7, 8.0, 3.2]
    
vector_possibilities = ((1,1,0),(-1,1,0),(1,-1,0),(-1,-1,0),(1,0,1),(-1,0,1),(1,0,-1),(-1,0,-1), (0,1,1),(0,-1,1),(0,1,-1),(0,-1,-1))
#picking the vectors randomly or with a seed from this list supposedly makes the noise better, have not tested yet

class Perlin_stuff:
  chunk_vectors = [] #hold the vectors of every created chunk, must figure out how to handle expansion in all directions
  perlin_map = []
  def create_vectors(self,chunk_size,chunk_width,chunk_height):
    for y in range(chunk_height):
      row = []
      for x in range(chunk_width):
        row.append(create_chunk(x*chunk_size, y*chunk_size,seed,chunk_size))
      self.chunk_vectors.append(row)
  
  def draw_vectors(self,chunk_size):
    stroke(0,0,0)
    for y in range(len(self.chunk_vectors)):
      for x in range(len(self.chunk_vectors[y])):
        pass
        #line(x*chunk_size,y*chunk_size,)
        line(x*chunk_size,y*chunk_size,(x*chunk_size)+(self.chunk_vectors[y][x][0]*self.chunk_vectors[y][x][2]),(y*chunk_size)+(self.chunk_vectors[y][x][1]*self.chunk_vectors[y][x][2]))
  
  def create_dist_vector(self,x,y,sc_width,sc_height,chunk_dim):
    x1 = int(x/chunk_dim[0])*chunk_dim[0]
    y1 = int(y/chunk_dim[1])*chunk_dim[1]
    x2 = x1+chunk_dim[0]
    y2 = y1+chunk_dim[1]
    
    dist_vectors = (make_vector(x,y,x1,y1),make_vector(x,y,x2,y1),make_vector(x,y,x1,y2),make_vector(x,y,x2,y2))
    return dist_vectors
  
  
  def fill_perlin(self,sc_width,sc_height):
    chunk_dim = (int(sc_height/len(self.chunk_vectors)),int(sc_width/len(self.chunk_vectors[0])))
    num_chunks = (len(self.chunk_vectors),len(self.chunk_vectors[0]))
    for y in range(sc_height):
      y_index = int(y/50)
      row = []
      unit_y = y/num_chunks[0]
      for x in range(sc_width):
        
        x_index = int(x/50)
        
        dist_vector = self.create_dist_vector(x,y,sc_width,sc_height,(chunk_dim[0],chunk_dim[1]))
        
        g1 = dot_product(dist_vector[0],self.chunk_vectors[y_index][x_index]) # these are the dot products between each chunk corner's vector and the vector starting at the point and ending at the chunk corner, 
        g2 = dot_product(dist_vector[1],self.chunk_vectors[y_index][x_index+1])#the dot product of 2 vectors equals the cosine of the angle between them times the magnitude of each function
        g3 = dot_product(dist_vector[2],self.chunk_vectors[y_index+1][x_index]) #therefore if the chunk vector is facing opposite from the point in question then the output will be -1 times the magnitude of each vector
        g4 = dot_product(dist_vector[3],self.chunk_vectors[y_index+1][x_index+1])
        
        unit_x = (x - x_index*chunk_dim[1])/chunk_dim[1] # unit cordinates are for where the point is in it's chunk 0.5,0.5 would be the exact center of chunk, 1 is the edge of the chunk, etc.
        unit_y = (y - y_index*chunk_dim[0])/chunk_dim[0]
        
        x1 = (g1+g2+unit_x)/3
        x2 = (g3+g4+unit_x)/3
        
        color = (x1+x2+unit_y)/3
        row.append(color)
      self.perlin_map.append(row)
        
  def draw_perlin(self,sc_width,sc_height):
    for y in range(sc_height):
      for x in range(sc_width):
        pixels[y*sc_width+x] = color(self.perlin_map[y][x]*255)


perlin = Perlin_stuff()
  
def dist(x1,y1,x2,y2):
  a = abs(x1-x2)
  b = abs(y1-y2)
  return abs(math.sqrt((a*a)+(b*b)))

def fade(x): #this will use the function  t * t * t * (t * (t * 6 - 15) + 10) to smooth the perlin noise    
  pass

def dot_product(v1,v2):
  x = v1[0]*v2[0]
  y = v1[1]*v2[1]
  return (x+y)

def make_vector(x1,y1,x2,y2):
    a = x1 - x2
    b = y1 - y2
    c = abs(a)+abs(b)
    
    if c == 0:
      c = 1
    vector = [a/c,b/c,dist(x1,y1,x2,y2)]
    vector[0] = int(vector[0]*10000)/10000
    vector[1] = int(vector[1]*10000)/10000
    vector[2] = int(vector[2]*10000)/10000
    return vector



def create_chunk(x,y,seed,chunk_dim):
  pos_neg = (-1,1)
  
  x1 = int(mouse.x/chunk_dim) * chunk_dim #x0 left
  y1 = int(mouse.y/chunk_dim) * chunk_dim #y0 top
  
  vector_cords = (x1,y1,x1 + pos_neg[random.randint(0,1)]*random.randint(0,chunk_dim),y1 + pos_neg[random.randint(0,1)]*random.randint(0,chunk_dim))
  
  vectors = make_vector(vector_cords[0],vector_cords[1],vector_cords[2],vector_cords[3])
  
  
  return vectors
  
def mouse_chunk_lines(chunk_dim,chunk_offset):
  x0 = int(mouse.x/chunk_dim) * chunk_dim
  y0 = int(mouse.y/chunk_dim) * chunk_dim
  x1 = x0 + chunk_dim
  y1 = y0 + chunk_dim
  fill(0,50,400)
  ellipse(mouse.x,mouse.y,10,10)
  stroke(150,150,0)
  line(mouse.x,mouse.y,x0,y0)
  line(mouse.x,mouse.y,x0,y1)
  line(mouse.x,mouse.y,x1,y0)
  line(mouse.x,mouse.y,x1,y1)

def chunk_borders(chunk_dim,chunk_offset,width,height):
  stroke(0,0,255)
  for y in range(int(height/chunk_dim)):
    line(0,y*chunk_dim,width,y*chunk_dim)
    
  for x in range(int(width/chunk_dim)):
    line(x*chunk_dim,0,x*chunk_dim,500)


def setup():
  global screen_width
  global screen_height
  global seed
  size(screen_width,screen_height)
  
  perlin.create_vectors(50,11,11) #create the vectors that the chunks use
  
  perlin.fill_perlin(500,500)#create the map
  loadPixels()
  perlin.draw_perlin(500,500)#draw the map on the screen
  updatePixels()
  chunk_borders(50,0,screen_width,screen_height)
  #perlin.draw_vectors(50)


def draw():
  #global screen_width
  #global screen_height
  pass
  #background(200,200,200)
  #new_vector = create_chunk(mouse.x, mouse.y,5,50)
  #chunk_borders(50,0,screen_width,screen_height)
  #mouse_chunk_lines(50,0)
  #perlin.draw_vectors(50)
  
  
  
  
 
run()
