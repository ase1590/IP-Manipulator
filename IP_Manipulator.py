#!/usr/bin/python

# IP Address Manipulator
# By: Joshua Skorich
# Last Revised: 08_29_2013


import re
import sys


"""IP Manipulator
Given an IP Address, return various forms of dotted decimal, decimal, octal, and/or hexidecimal.

Requires that all octal addresses begin with '0' and all hex begin with '0x' or '0X'
"""


def convert(address, base):
  results = []
  
  # Search the address for periods
  dot_search = re.findall(r'\.', address)
  if len(dot_search) == 3:
    search = re.findall(r'(\d+)\.(\d+)\.(\d+)\.(\d+)', address)
    for addr in search:
      (a, b, c, d) = addr
      a = int(a, base)
      b = int(b, base)
      c = int(c, base)
      d = int(d, base) 
      
      # Decimal computation of all variants
      abcd = (a*256**3) + (b*256**2) + (c*256) + d
      bcd = (b*256**2) + (c*256) + d
      cd = (c*256) + d
      
  elif len(dot_search) == 2:
    search = re.findall(r'(\w+)\.(\w+)\.(\w+)', address)
    for addr in search:
      (a, b, cd) = addr
      a = int(a, base)
      b = int(b, base)
      cd = int(cd, base)        
      
      # Decimal computation of all variants
      c = cd / 256
      d =  cd - (c*256)
      abcd = (a*256**3) + (b*256**2) + (c*256) + d
      bcd = (b*256**2) + (c*256) + d
      cd = (c*256) + d        
      
  elif len(dot_search) == 1:
    search = re.findall(r'(\d+)\.(\d+)', address)
    for addr in search:
      (a, bcd) = addr
      a = int(a, base)
      bcd = int(bcd, base)   

      # Decimal computation of all variants
      b = bcd / 256**2
      c = (bcd - (b*256**2)) / 256
      d = bcd - (b*256**2) - (c*256)
      abcd = (a*256**3) + (b*256**2) + (c*256) + d
      bcd = (b*256**2) + (c*256) + d
      cd = (c*256) + d        
        
  elif len(dot_search) == 0:
    abcd = int(address, base)
    a = abcd / 256**3
    b = (abcd - (a*256**3)) / (256**2)
    c = (abcd - (a*256**3) - (b*256**2)) / 256
    d = abcd - (a*256**3) - (b*256**2) - (c*256)
    abcd = (a*256**3) + (b*256**2) + (c*256) + d
    bcd = (b*256**2) + (c*256) + d
    cd = (c*256) + d         
      
  else:
    sys.stderr.write('Please enter IP in valid decimal format')
    sys.exit(1)

    
  # Store decimal variants into results list
  results.append(str(a).rstrip('L') + '.' + str(b).rstrip('L') + '.' + str(c).rstrip('L') + '.' + str(d).rstrip('L'))  
  results.append(str(a).rstrip('L') + '.' + str(b).rstrip('L') + '.' + str(cd).rstrip('L'))
  results.append(str(a).rstrip('L') + '.' + str(bcd).rstrip('L'))
  results.append(str(abcd).rstrip('L'))
    
  # Store hex variants into results list
  results.append(hex(a).rstrip('L') + '.' + hex(b).rstrip('L') + '.' + hex(c).rstrip('L') + '.' + hex(d).rstrip('L'))
  results.append(hex(a).rstrip('L') + '.' + hex(b).rstrip('L') + '.' + hex(cd).rstrip('L'))
  results.append(hex(a).rstrip('L') + '.' + hex(bcd).rstrip('L'))
  results.append(hex(abcd).rstrip('L'))
    
  # Store oct variants into results list
  results.append(oct(a).rstrip('L') + '.' + oct(b).rstrip('L') + '.' + oct(c).rstrip('L') + '.' + oct(d).rstrip('L'))
  results.append(oct(a).rstrip('L') + '.' + oct(b).rstrip('L') + '.' + oct(cd).rstrip('L'))
  results.append(oct(a).rstrip('L') + '.' + oct(bcd).rstrip('L'))
  results.append(oct(abcd).rstrip('L'))

  return results

def format(address):
  search = re.search(r'(^\d)', address)
  first_letter = search.group()
  if first_letter == '0':
    search = re.search(r'0(x)', address, re.IGNORECASE)
    if search:
      base = 16
      return base
    else:
      base = 8
      return base
  else:
    base = 10
    return base


def main():
  from optparse import OptionParser
  parser = OptionParser(usage='usage: %prog [options] ip_addr')
  parser.add_option('-f', '--file', dest='filename', help='write report to FILE', metavar='FILE')
  parser.add_option('--dec', action='store_true', dest='decimal', help='input ip_addr is in decimal form')
  parser.add_option('--hex', action='store_true', dest='hexidecimal', help='input ip_addr is in hexidecimal form')
  parser.add_option('--oct', action='store_true', dest='octal', help='input ip_addr is in octal form')

  
  (options, args) = parser.parse_args()
  
  for arg in args:
    if options.decimal:
      base = 10
    elif options.hexidecimal:
      base = 16
    elif options.octal:
      base = 8
    else:
      base = format(arg)
    
    converted_addresses = convert(arg, base)
    
    if options.filename is not None:
      filename = options.filename
      f = open(filename, 'w')
      for address in converted_addresses:
        address += '\n'
        f.write(address)
    else:
      print '\n'
      print '        IP Address Manipulator       '
      print '-'*37
      for address in converted_addresses:
        line = arg + ' ----> ' + address + '\n'
        print line
      
if __name__ == '__main__':
  main()
