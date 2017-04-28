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
pathImg = 'results/Comparison_Xue08/'
fontsize = 2

src_imgPath = root + '/../results/Comparison_Xue08/src_img'
imgNameList = [int(os.path.splitext(x)[0]) for x in os.listdir(src_imgPath) \
               if os.path.isfile(os.path.join(src_imgPath, x)) and os.path.splitext(x)[1] == '.jpg']
#print(imgNameList)
imgNameList.sort()
print(imgNameList)
#indexRange = list(range(0,len(imgNameList)))

imgDirList = ['src_img', 'Smooth_Bump', 'Smooth_invBump', \
'Refined_Bump', 'Refined_invBump']
 
tableTitleList = ['Method', 'Src_img', 'ProgressionMap', 'Smooth_Bump', 'Smooth_invBump', \
'Refined_Bump', 'Refined_invBump']

# generate webpages
print 'Generating a webpage for show texture synthesis results'
fnHtml = dirOut + 'Comparison_Xue08.html'
f = open(fnHtml, 'w')
f.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n')
f.write('<html><head></head>\n')
f.write('<link rel="stylesheet" type="text/css" href="../style.css" />\n')
f.write('<body><title>Comparison_Xue08</title>\n')
f.write('<h2>Comparison with [Xue2008]</h2>\n')

f.write('<p style="font-size:18px;"> #1: Our Feature + Isomap <br>#2: Our Feature + GeodisRatio <br>#3: Lab + Isomap <br>#4: Lab + GeodisRatio </p>')
f.write('<p style="font-size:16px;">For a fair comparison, we use the extrema of Isomap for geodesic distance based dimensionality reduction. <br>Specifically, we use the extrema of #1 for #2, and the extremes of #3 for #4, <br>where they are higlighted in yellow and blue circles </p>')

f.write('<table style="text-align: center; width: 900px; height: 300px;" border="1" cellpadding="1" cellspacing="1"><tbody>\n')

fileIdRange = range(0, len(imgNameList))
for i in fileIdRange:
  f.write('<tr>\n')
  f.write('<td style="width:128px;"><p style="font-size:12px;">%d</td>\n' % (imgNameList[i]))
  for j in range(1, len(tableTitleList)):
      f.write('<td style="width:128px;"><p style="font-size:12px;">%s</td>\n' % (tableTitleList[j]))
  f.write('</tr>\n')

  
  f.write('<tr>\n')
  f.write('<td style="width:128px;"><p style="font-size:12px;">#1</td>\n')
  fnImg = pathImg + '%s/%d.jpg' % (imgDirList[0], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Our_feature_IsoMap/%s/%d_src_gc.png' % (imgDirList[1], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))

  fnImg = pathImg + 'Our_feature_IsoMap/%s/%d_trg.png' % (imgDirList[1], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Our_feature_IsoMap/%s/%d_trg.png' % (imgDirList[2], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Our_feature_IsoMap/%s/%d_trg.png' % (imgDirList[3], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Our_feature_IsoMap/%s/%d_trg.png' % (imgDirList[4], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  f.write('</tr>\n')
    
  f.write('<tr>\n')
  f.write('<td style="width:128px;"><p style="font-size:12px;">#2</td>\n')
  fnImg = pathImg + '%s/%d_1.png' % (imgDirList[0], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Our_feature_NeibGraph/%s/%d_src_gc.png' % (imgDirList[1], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))

  fnImg = pathImg + 'Our_feature_NeibGraph/%s/%d_trg.png' % (imgDirList[1], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Our_feature_NeibGraph/%s/%d_trg.png' % (imgDirList[2], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Our_feature_NeibGraph/%s/%d_trg.png' % (imgDirList[3], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Our_feature_NeibGraph/%s/%d_trg.png' % (imgDirList[4], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  f.write('</tr>\n')
  
  f.write('<tr>\n')
  f.write('<td style="width:128px;"><p style="font-size:12px;">#3</td>\n')
  fnImg = pathImg + '%s/%d.jpg' % (imgDirList[0], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Lab_feature_IsoMap/%s/%d_src_gc.png' % (imgDirList[1], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
 
  fnImg = pathImg + 'Lab_feature_IsoMap/%s/%d_trg.png' % (imgDirList[1], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Lab_feature_IsoMap/%s/%d_trg.png' % (imgDirList[2], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Lab_feature_IsoMap/%s/%d_trg.png' % (imgDirList[3], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Lab_feature_IsoMap/%s/%d_trg.png' % (imgDirList[4], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  f.write('</tr>\n')  
  
  f.write('<tr>\n')
  f.write('<td style="width:128px;"><p style="font-size:12px;">#4</td>\n')
  fnImg = pathImg + '%s/%d_2.png' % (imgDirList[0], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Lab_feature_NeibGraph/%s/%d_src_gc.png' % (imgDirList[1], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
 
  fnImg = pathImg + 'Lab_feature_NeibGraph/%s/%d_trg.png' % (imgDirList[1], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Lab_feature_NeibGraph/%s/%d_trg.png' % (imgDirList[2], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Lab_feature_NeibGraph/%s/%d_trg.png' % (imgDirList[3], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  fnImg = pathImg + 'Lab_feature_NeibGraph/%s/%d_trg.png' % (imgDirList[4], imgNameList[i])
  f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  f.write('</tr>\n')

f.write('</tbody></table><br></body></html>\n')
f.close()
