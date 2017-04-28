import os, sys

#####################
# set directories   #
#####################
root = os.getcwd()

######################
# GCD.html #	
######################

# set up directories
dirOut = root+'/../'
if not os.path.exists(dirOut):
  os.mkdir(dirOut)
pathImg = 'results/Orientation_control&Comparison_Lukac15/'
fontsize = 2

src_imgPath = root + '/../results/Orientation_control&Comparison_Lukac15/hog_vis/'
imgNameList = [int(os.path.splitext(x)[0]) for x in os.listdir(src_imgPath) \
               if os.path.isfile(os.path.join(src_imgPath, x)) and os.path.splitext(x)[1] == '.jpg']
#print(imgNameList)
imgNameList.sort()
print(imgNameList)
#indexRange = list(range(0,len(imgNameList)))

imgDirList = ['hog_vis', 'Lukac2015(hard_constraint)_trg_0', 'Our_method(soft_constraint)_trg_0', 'Lukac2015(hard_constraint)_trg_1', 'Our_method(soft_constraint)_trg_1', 'Lukac2015(hard_constraint)_trg_2', 'Our_method(soft_constraint)_trg_2', 'Lukac2015(hard_constraint)_trg_3', 'Our_method(soft_constraint)_trg_3' ]
 
tableTitleList = ['hog_vis', 'Lukac2015(hard_constraint)', 'Our_method(soft_constraint)', 'Lukac2015(hard_constraint)', 'Our_method(soft_constraint)', 'Lukac2015(hard_constraint)', 'Our_method(soft_constraint)', 'Lukac2015(hard_constraint)', 'Our_method(soft_constraint)']

# generate webpages
print 'Generating a webpage for show texture synthesis results'
fnHtml = dirOut + 'Comparison_Lukac15_simple.html'
f = open(fnHtml, 'w')
f.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n')
f.write('<html><head></head>\n')
f.write('<link rel="stylesheet" type="text/css" href="../style.css" />\n')
f.write('<body><title>Comp_Lukac15_simple_targets</title>\n')

f.write('<table style="text-align: center; width: 900px; height: 300px;" border="1" cellpadding="1" cellspacing="1"><tbody>\n')
fileIdRange = range(0, len(imgNameList))
for i in fileIdRange:
  f.write('<tr>\n')
  f.write('<td style="width:128px;"><p style="font-size:12px;">%s.jpg</td>\n' % (imgNameList[i]))
  for j in range(1, len(tableTitleList)):
      f.write('<td style="width:128px;"><p style="font-size:12px;">%s</td>\n' % (tableTitleList[j]))
  f.write('</tr>\n')
  
  f.write('<tr>\n')
  fnImg = pathImg + '%s/%d.jpg' % (imgDirList[0], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px; display:block; margin:auto" alt="%d" src="%s" sizingMethod="scale"/></a></td>\n' % (fnImg, i, fnImg))
  for j in range(1, len(imgDirList)):
      fnImg = pathImg + '%s/%d_trg.png' % (imgDirList[j], imgNameList[i])
      f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; width: 128px; height: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  f.write('</tr>\n') 

f.write('</tbody></table><br></body></html>\n')
f.close()
