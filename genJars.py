import os
import subprocess

sentence = raw_input("enter sentence to translate:")

words = sentence.split();

print words

def makeApplet(word, num):
  """creates an applet"""
  classname = "RandomWord"
  if num > 1:
    classname = classname + str(num)

  code =  """/** takes a word, displays it with random font, color and size
    generated with python
  @author tinaun
  @version 0.1
*/

import java.applet.Applet;
import java.awt.*;
import java.util.Random;

public class """ + classname + """ extends Applet {

    private String word;
    private Color color, bgcolor;

    public void init() {
      Random r = new Random(new Random().nextLong());
      color = new Color(r.nextFloat(), r.nextFloat(), r.nextFloat());
      bgcolor = new Color(255 - color.getRed(), 255 - color.getGreen(), 255 - color.getBlue());
      word = \"""" + word +  """ \" + Integer.toString(r.nextInt(100));
    }

    public void stop() {

    }

    public void paint(Graphics g){
      g.setColor(bgcolor);
      g.fillRect(0,0,200,40);
      g.setColor(color);
      g.drawString(word, 40, 20);
    }
}"""

  print classname
  filename = classname + ".java"
  os.system("rm -f " + filename)

  f = open(filename, 'w')

  f.write(code)
  f.close()

  os.system("javac " + filename)
  appname = classname + ".class"
  os.system("rm -f ../../public_html/testprogs/" + appname)
  os.system("mv " + appname + " ../../public_html/testprogs/" + appname)

def makeHtml(num):
  classname = "RandomWord"
  if num > 1:
    classname += str(num)
  apphtml = "<applet width='200' height='40' code='" + classname + ".class'></applet>\n"
  return apphtml



page = "<!doctype html>\n<html>\n<head>\n <meta charset='utf-8'>\n  <title>bad webpage</title>\n</head>\n <body>\n\n"

num = 1
for word in words:
  makeApplet(word,num)
  page += makeHtml(num);
  num = num + 1

page += "</body>\n</html>\n"

f = open("applet.html", 'w')
f.write(page)
f.close()

os.system("mv applet.html ../../public_html/testprogs/applet.html")

print "done!!"
