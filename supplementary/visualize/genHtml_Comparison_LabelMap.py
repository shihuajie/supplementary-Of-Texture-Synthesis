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
pathImg = 'results/Comparison_LabelMap/'

# generate webpages
print 'Generating a webpage for show texture synthesis results'
fnHtml = dirOut + 'Comparison_LabelMap.html'
f = open(fnHtml, 'w')
f.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n')
f.write('<html><head></head>\n')
f.write('<link rel="stylesheet" type="text/css" href="../style.css" />\n')
f.write('<body><title>Comparison_LabelMap</title>\n')
f.write('<h2>Compare with the discrete labelmaps of [Rosenberger09] & [Lockerman16]</h2>\n')


f.write('<p style="font-size:18px;"> Note that in [Lockerman16] the discrete labelmaps contain multiple scales, <br> which are indicated as C4, C3, C2 and C1 below. For more information, please refer to their paper. </p>')
f.write('<table style="text-align: center; width: 900px; height: 300px;" border="1" cellpadding="1" cellspacing="1"><tbody>\n')

f.write('<tr>\n')
f.write('<td style="width:128px;"><p style="font-size:12px;">exemplar</td>\n')
f.write('<td style="width:128px;"><p style="font-size:12px;">Our progression map</td>\n')
f.write('<td style="width:128px;"><p style="font-size:12px;">[Rosenberger09]</td>\n')
f.write('<td style="width:128px;"><p style="font-size:12px;">[Lockerman16] - C4</td>\n')
f.write('<td style="width:128px;"><p style="font-size:12px;">[Lockerman16] - C3</td>\n')
f.write('<td style="width:128px;"><p style="font-size:12px;">[Lockerman16] - C2</td>\n')
f.write('<td style="width:128px;"><p style="font-size:12px;">[Lockerman16] - C1</td>\n')
f.write('</tr>\n')

for i in range(1, 4):
  f.write('<tr>\n')
  fnImg = pathImg + ('%d.jpg' % i)
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 160px; display:block; margin:auto" alt="%d" src="%s" sizingMethod="scale"/></a></td>\n' % (fnImg, i, fnImg))
  for j in range(1, 7):
      fnImg = pathImg + '%d-%d.png' % (i, j)
      f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 160px; display:block; margin:auto" alt="%d" src="%s" sizingMethod="scale"/></a></td>\n' % (fnImg, i, fnImg))
  f.write('</tr>\n') 

f.write('</tbody></table><br></body></html>\n')

src_imgPath = root + '/../results/Comparison_LabelMap'
imgNameList = [int(os.path.splitext(x)[0]) for x in os.listdir(src_imgPath) \
               if os.path.isfile(os.path.join(src_imgPath, x)) and os.path.splitext(x)[1] == '.jpg']

imgDirList = ['src_img', 'bump', 'invbump', 'refined_bump', 'refined_invbump']
tableTitleList = ['src_img', 'bump', 'invbump', 'refined_bump', 'refined_invbump']

imgDirList2 = ['src_img', 'bump_discrete', 'invbump_discrete', 'refined_bump_discrete', 'refined_invbump_discrete']
tableTitleList2 = ['src_img', 'bump_discrete', 'invbump_discrete', 'refined_bump_discrete', 'refined_invbump_discrete']


f.write('<p style="font-size:18px;"> Further comparison on controlled synthesis between our continuous progression map and discrete label map of [Lockerman16]. <br> Note that for [Lockerman16], C4 label maps are used for the first two exemplars and C3 for the third one. <br> And when designing the target discrete maps, we force the propotions of different labels be the same as the source label maps as far as possible.</p>')
f.write('<table style="text-align: center; width: 900px; height: 300px;" border="1" cellpadding="1" cellspacing="1"><tbody>\n')
fileIdRange = range(0, len(imgNameList))
for i in fileIdRange:
  
  # continuous - synthesis results
  # tile
  f.write('<tr>\n')
  f.write('<td style="width:128px;"><p style="font-size:12px;">%d.jpg</td>\n' % (imgNameList[i]))
  for j in range(1, len(tableTitleList)):
      f.write('<td style="width:128px;"><p style="font-size:12px;">%s</td>\n' % (tableTitleList[j]))
  f.write('</tr>\n')
  
  # source guidance
  f.write('<tr>\n')
  
  fnImg = pathImg + '%d-1.png' % (imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))

  # target guidance 
  fnImg = pathImg + 'bump.png'
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))

  fnImg = pathImg + 'invbump.png'
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))

  fnImg = pathImg + '%s/%d_trg_gc.png' % (imgDirList[3], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  
  fnImg = pathImg + '%s/%d_trg_gc.png' % (imgDirList[4], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))

  f.write('</tr>\n')
  

  # synthesis result
  f.write('<tr>\n')
  fnImg = pathImg + '%d.jpg' % (imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  for j in range(1, 5):
      fnImg = pathImg + '%s/%d_0.9.png' % (imgDirList[j], imgNameList[i])
      f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
      
  f.write('</tr>\n')
  
  

  # discrete - synthesis results
  # tile
  f.write('<tr>\n')
  f.write('<td style="width:128px;"><p style="font-size:12px;">[Lockerman16]</td>\n')
  for j in range(1, len(tableTitleList2)):
      f.write('<td style="width:128px;"><p style="font-size:12px;">%s</td>\n' % (tableTitleList2[j]))
  f.write('</tr>\n')
  
  # source guidance
  f.write('<tr>\n')
  
  fnImg = pathImg + '%d_src_gc.png' % (imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))

  # target guidance
  for j in range(1, len(tableTitleList2)):
      fnImg = pathImg + '%s/%d_trg.png' % (imgDirList2[j], imgNameList[i])
      f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))

  f.write('</tr>\n')
  

  # synthesis result
  f.write('<tr>\n')
  fnImg = pathImg + '%d.jpg' % (imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  for j in range(1, 5):
      fnImg = pathImg + '%s/%d_0.9.png' % (imgDirList2[j], imgNameList[i])
      f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
      
  f.write('</tr>\n')

f.write('</tbody></table><br></body></html>\n')
f.close()
