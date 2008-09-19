import os
import re
import xml

IMAGE_PATH_PREFIX = '../../images/logo/'

find_png = re.compile('.*<property name="icon">(.*)\.png</property>')

def open_files_as_xml():
  
  for f in os.listdir('.'):
    if (f.endswith('.glade')):
      curr_file = open(f,'r')
      file_lines = curr_file.readlines()
      updated_lines = list()
      for line in file_lines :
        #print line
        match = re.findall(find_png, line)
        if (match):
          str_match = match.pop()  
          if (str_match.find(IMAGE_PATH_PREFIX) == -1) :# if we don't already have the right prefix...
            new_line = line.replace(str_match , IMAGE_PATH_PREFIX + str_match)     
            updated_lines.append(new_line)
          else:
            updated_lines.append(line) 
        else:
          updated_lines.append(line) 
      curr_file.close()
      curr_file = open(f, 'w')
      curr_file.writelines(updated_lines)
      curr_file.close()

if __name__ == "__main__":
  open_files_as_xml()
