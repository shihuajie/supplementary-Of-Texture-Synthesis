import os, sys

#####################
# set directories   #
#####################
root = os.getcwd()

######################
# GCD.html #	
######################

# set up directories
dirOut = root + '/../'
if not os.path.exists(dirOut):
  os.mkdir(dirOut)
pathImg = 'results/Progression_control/'
fontsize = 2

src_imgPath = root + '/../results/Progression_control/src_img'
imgNameList = [int(os.path.splitext(x)[0]) for x in os.listdir(src_imgPath) \
               if os.path.isfile(os.path.join(src_imgPath, x)) and os.path.splitext(x)[1] == '.jpg']
#print(imgNameList)
imgNameList.sort()
print(imgNameList)
#indexRange = list(range(0,len(imgNameList)))

imgDirList = ['src_img', 'Smooth_Bump', 'Refined_Bump', 'Smooth_invBump', 'Refined_invBump']
 
tableTitleList = ['src_img', 'Smooth_Bump', 'Refined_Bump', 'Smooth_invBump', 'Refined_invBump']

# generate webpages
print 'Generating a webpage for show texture synthesis results'
fnHtml = dirOut + 'Progression_control.html'
f = open(fnHtml, 'w')
f.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n')
f.write('<html><head></head>\n')
f.write('<link rel="stylesheet" type="text/css" href="../style.css" />\n')
f.write('<body><title>Progression_control</title>\n')
f.write('<h2>Synthesis with bump-shaped target guidance channels</h2>\n')

f.write('<table style="text-align: center; width: 900px; height: 300px;" border="1" cellpadding="1" cellspacing="1"><tbody>\n')

fileIdRange = range(0, len(imgNameList))
for i in fileIdRange:
  f.write('<tr>\n')
  f.write('<td style="width:128px;"><p style="font-size:12px;">%d.jpg</td>\n' % (imgNameList[i]))
  for j in range(1, len(tableTitleList)):
      f.write('<td style="width:128px;"><p style="font-size:12px;">%s</td>\n' % (tableTitleList[j]))
  f.write('</tr>\n')

  f.write('<tr>\n')
  fnImg = pathImg + '%s/%d_src_gc.png' % (imgDirList[0], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  
  fnImg = pathImg + 'bump.png'
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))

  fnImg = pathImg + '%s/%d_trg.png' % (imgDirList[2], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))

  fnImg = pathImg + 'invbump.png'
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))

  fnImg = pathImg + '%s/%d_trg.png' % (imgDirList[4], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))

  f.write('</tr>\n')
  
  f.write('<tr>\n')
  fnImg = pathImg + 'src_img/%d.jpg' % (imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  for j in range(1, 5):
      fnImg = pathImg + '%s/%d.png' % (imgDirList[j], imgNameList[i])
      f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))

  f.write('</tr>\n')


f.write('</tbody></table><br></body></html>\n')
f.close()
