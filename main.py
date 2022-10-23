from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
        p.createCanvas(500, 410)
        p.background(0,255,100)
        p.rectMode(p.CENTER)
        
        for i in range(10):
          p.noStroke()
          p.fill(250-i*25,0,0)
          p.circle(200,200,100-i*10)
    
    p.setup = setup
      
myp5 = window.p5.new(sketch)
