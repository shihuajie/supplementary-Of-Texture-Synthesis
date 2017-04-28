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
pathImg = 'results/Two_controls/'
fontsize = 2

src_imgPath = root + '/../results/Two_controls/src_img'
imgNameList = [int(os.path.splitext(x)[0]) for x in os.listdir(src_imgPath) \
               if os.path.isfile(os.path.join(src_imgPath, x)) and os.path.splitext(x)[1] == '.jpg']
#print(imgNameList)
imgNameList.sort()
print(imgNameList)
#indexRange = list(range(0,len(imgNameList)))

imgDirList = ['src_img', '1x1', '1x2', '2x1', '2x2']
 
tableTitleList = ['src_img', 'ScalarMap1 x VecField1', 'ScalarMap1 x VecField2', 'ScalarMap2 x VecField1', 'ScalarMap2 x VecField2']

# generate webpages
print 'Generating a webpage for show texture synthesis results'
fnHtml = dirOut + 'Two_controls.html'
f = open(fnHtml, 'w')
f.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n')
f.write('<html><head></head>\n')
f.write('<link rel="stylesheet" type="text/css" href="../style.css" />\n')
f.write('<body><title>Two_controls</title>\n')
f.write('<h2>Simultaneous control of progression and orientation</h2>\n')

f.write('<table style="text-align: center; width: 900px; height: 300px;" border="1" cellpadding="1" cellspacing="1"><tbody>\n')

fileIdRange = range(0, len(imgNameList))
for i in fileIdRange:
  f.write('<tr>\n')
  f.write('<td style="width:128px;"><p style="font-size:12px;">%s.jpg</td>\n' % (imgNameList[i]))
  for j in range(1, len(imgDirList)):
      f.write('<td style="width:128px;"><p style="font-size:12px;">%s</td>\n' % (tableTitleList[j]))
  f.write('</tr>\n')
  
  f.write('<tr>\n')
  fnImg = pathImg + '%s/%d.jpg' % (imgDirList[0], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px; display:block; margin:auto" alt="%d" src="%s" sizingMethod="scale"/></a></td>\n' % (fnImg, i, fnImg))
  for j in range(1, len(imgDirList)):
      fnImg = pathImg + '%s/%d.png' % (imgDirList[j], imgNameList[i])
      f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; width: 128px; height: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  f.write('</tr>\n')

  f.write('<tr>\n')
  fnImg = pathImg + '%s/%d_src_gc_vis.png' % (imgDirList[0], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px; display:block; margin:auto" alt="%d" src="%s" sizingMethod="scale"/></a></td>\n' % (fnImg, i, fnImg))
  for j in range(1, len(imgDirList)):
      fnImg = pathImg + '%s/trg_gc_%dx%d_vis.png' % (imgDirList[0], (j+1)/2, (j+1)%2+1)
      f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; width: 128px; height: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  f.write('</tr>\n')
  
  f.write('<tr>\n')
  fnImg = pathImg + '%s/%d_src_gc_vis.png' % (imgDirList[0], imgNameList[i])
  #f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px; display:block; margin:auto" alt="%d" src="%s" sizingMethod="scale"/></a></td>\n' % (fnImg, i, fnImg))
  f.write('<td style="width:128px; height:128px"><p style="font-size:12px;">Re-estimated guidance channels of the synthesized texture</p></td>\n')
  for j in range(1, len(imgDirList)):
      fnImg = pathImg + '%s/%d_trg_gc_vis.png' % (imgDirList[j], imgNameList[i])
      f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; width: 128px; height: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  f.write('</tr>\n')

f.write('</tbody></table><br></body></html>\n')
f.close()
