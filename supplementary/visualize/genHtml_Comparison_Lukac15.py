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
pathImg = 'results/Comparison_Lukac15/'
fontsize = 2

src_imgPath = root + '/../results/Comparison_Lukac15/hog_vis/'
imgNameList = [int(os.path.splitext(x)[0]) for x in os.listdir(src_imgPath) \
               if os.path.isfile(os.path.join(src_imgPath, x)) and os.path.splitext(x)[1] == '.jpg']
#print(imgNameList)
imgNameList.sort()
print(imgNameList)
#indexRange = list(range(0,len(imgNameList)))

imgDirList = ['hog_vis', 'synthesis_hard_constraint_trg_4', 'synthesis_soft_constraint_trg_4', 'synthesis_hard_constraint_trg_5', 'synthesis_soft_constraint_trg_5' ]
 
tableTitleList = ['hog_vis', 'Lukac2015(hard_constraint)', 'Our_method(soft_constraint)', 'Lukac2015(hard_constraint)', 'Our_method(soft_constraint)']

# generate webpages
print 'Generating a webpage for show texture synthesis results'
fnHtml = dirOut + 'Comparison_Lukac15.html'
f = open(fnHtml, 'w')
f.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n')
f.write('<html><head></head>\n')
f.write('<link rel="stylesheet" type="text/css" href="../style.css" />\n')
f.write('<body><title>Comparison_Lukac15</title>\n')
f.write('<h2>Comparison with [Lukac2015]</h2>\n')

f.write('<p style="font-size:18px;"><b>I.</b> Comparison of our soft-constraint with hard constraint on some simple targets. <br> Note that to compare on orientation control, we set beta in eq.3 to zero in our method. </p>')

f.write('<table style="text-align: center; width: 128px; height: 128px;" border="1" cellpadding="1" cellspacing="1"><tbody>\n')
fnImg = pathImg + 'hog_vis/trg_gc_vis_1.png'
f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px; display:block; margin:auto" alt="%d" src="%s" sizingMethod="scale"/></a></td>\n' % (fnImg, 1, fnImg))
fnImg = pathImg + 'hog_vis/trg_gc_vis_2.png'
f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px; display:block; margin:auto" alt="%d" src="%s" sizingMethod="scale"/></a></td>\n' % (fnImg, 2, fnImg))
fnImg = pathImg + 'hog_vis/trg_gc_vis_3.png'
f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px; display:block; margin:auto" alt="%d" src="%s" sizingMethod="scale"/></a></td>\n' % (fnImg, 3, fnImg))
f.write('</tbody></table><br></body></html>\n')

f.write('<td style="width:100px;"><a href="Comparison_Lukac15_simple.html"><p style="font-size:20px;">Click here to view the comparison on simple targets</a></td>')
f.write('<tr>\n')
f.write('<tr>\n')

f.write('<p style="font-size:18px;"><b>II.</b> Comparison of our soft-constraint with hard constraint on <b>very challenging targets</b>. </p>')

f.write('<table style="text-align: center; width: 256px; height: 256px;" border="1" cellpadding="1" cellspacing="1"><tbody>\n')
fnImg = pathImg + 'hog_vis/trg_gc_vis_4.png'
f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 256px; max-width: 256px; display:block; margin:auto" alt="%d" src="%s" sizingMethod="scale"/></a></td>\n' % (fnImg, 1, fnImg))
fnImg = pathImg + 'hog_vis/trg_gc_vis_5.png'
f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 256px; max-width: 256px; display:block; margin:auto" alt="%d" src="%s" sizingMethod="scale"/></a></td>\n' % (fnImg, 2, fnImg))
f.write('</tbody></table><br></body></html>\n')

f.write('<p style="font-size:18px;">It is recommended to zoom in the page or click the image to see the details of each synthesis result. </p>')
f.write('<tr>\n')

f.write('<table style="text-align: center; width: 900px; height: 300px;" border="1" cellpadding="1" cellspacing="1"><tbody>\n')

fileIdRange = range(0, len(imgNameList))
for i in fileIdRange:
  f.write('<tr>\n')
  f.write('<td style="width:256px;"><p style="font-size:12px;">%s.jpg</td>\n' % (imgNameList[i]))
  for j in range(1, len(tableTitleList)):
      f.write('<td style="width:256px;"><p style="font-size:12px;">%s</td>\n' % (tableTitleList[j]))
  f.write('</tr>\n')
  
  f.write('<tr>\n')
  fnImg = pathImg + '%s/%d_hog.png' % (imgDirList[0], imgNameList[i])
  f.write('<td style="width:256px; height:256px"><a href="%s"><img style="border: 0px; max-height: 256px; max-width: 256px; display:block; margin:auto" alt="%d" src="%s" sizingMethod="scale"/></a></td>\n' % (fnImg, i, fnImg))
  for j in range(1, len(imgDirList)):
      fnImg = pathImg + '%s/%d_trg.png' % (imgDirList[j], imgNameList[i])
      f.write('<td style="width:256px; height:128px"><a href="%s"><img style="border: 0px; width: 256px; height: 256px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  f.write('</tr>\n') 

f.write('</tbody></table><br></body></html>\n')
f.close()
