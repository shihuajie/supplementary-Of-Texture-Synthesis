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
pathImg = 'results/Time_Varying/'
fontsize = 2

#print(imgNameList)
imgNameList = [23, 139, 605, 608]
#indexRange = list(range(0,len(imgNameList)))
 
tableTitleList = ['t0(clean)', 't1', 't2', 't3(input)', 't4', 't5']
imgPathList = ['t0', 't1', 't2', 't3', 't4', 't5', 'trg_gc_t0', 'trg_gc_t1', 'trg_gc_t2', 'trg_gc_t3', 'trg_gc_t4', 'trg_gc_t5', 'src_gc']

# generate webpages
print 'Generating a webpage for show texture synthesis results'
fnHtml = dirOut + 'Time_Varying.html'
f = open(fnHtml, 'w')
f.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n')
f.write('<html><head></head>\n')
f.write('<link rel="stylesheet" type="text/css" href="../style.css" />\n')
f.write('<body><title>Time_Varying_Weathering</title>\n')
f.write('<h2>Results of time varying weathering texture synthesis</h2>\n')

f.write('<table style="text-align: center; width: 900px; height: 300px;" border="1" cellpadding="1" cellspacing="1"><tbody>\n')

fileIdRange = range(0, len(imgNameList))
for i in fileIdRange:
  f.write('<tr>\n')
  for j in range(len(tableTitleList)):
      f.write('<td style="width:128px;"><p style="font-size:12px;">%s</td>\n' % (tableTitleList[j]))
  f.write('</tr>\n')
  
  f.write('<tr>\n')
  for j in range(len(tableTitleList)):
      fnImg = pathImg + '%d/%d_trg_gc_cmp_t%d.png' % (imgNameList[i], imgNameList[i], j)
      f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  f.write('</tr>\n')
  
  f.write('<tr>\n')
  for j in range(len(tableTitleList)):
      fnImg = pathImg + '%d/%d_t%d.png' % (imgNameList[i], imgNameList[i], j)
      f.write('<td style="width:128px; height:128px"><a href="%s"><img style="border: 0px; max-height: 128px; max-width: 128px;" alt="%d" src="%s"/></a></td>\n' % (fnImg, i, fnImg))
  f.write('</tr>\n')

f.write('</tbody></table><br></body></html>\n')
f.close()
