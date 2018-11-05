#!/bin/python
from sys  import argv
from os   import system
from subprocess import Popen, PIPE

ffm = 'ffmpeg -i' # input file
aud = ' -acodec mp3' #add your quality preferences
dur = ' 2>&1 | grep "Duration" | cut -d " " -f 4'

def cutter(inp,t=0):
  out = inp[:-5] + '_cut' + inp[-5:]
  cut = ' -t %s' % ( duration(inp)-t )
  cmd = ffm + inp + aud + cut + out
  print cmd;  system(cmd)

def fader(inp,t=0):
  out = inp[:-5] + '_fade' + inp[-5:]
  fad = ' -af "afade=t=out:st=%s:d=%s"' % ( duration(inp)-t, t )
  cmd = ffm + inp + fad + out
  print cmd;  system(cmd)

def duration(inp):
  proc = Popen(ffm + inp + dur, shell=True, stdout=PIPE, stderr=PIPE)
  out,err = proc.communicate()
  h,m,s = [float(x)  for x in out[:-2].split(':')]
  return (h*60 + m)*60 + s

if __name__ == '__main__':
  fname=' "'+argv[1]+'"'
  cutter(fname,20)
  #fader (fname, 5)
