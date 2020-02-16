# Copyright 2020 Bob Peret
#
import cv2
#
# readImg
# Reads an image file and applies a threshold
# to remove thermal noise and sky glow
#
def readImg(fileName):
      img = cv2.imread(fileName)
      ret, threshImg = cv2.threshold(img, lowerThresh, 255, cv2.THRESH_TOZERO)
      return threshImg

#
# getFileName
# returns a filename in the format:
#   stars_%04d.jpg
#
def getFilename(num):
      filename = 'stars_'
      filename += format(num, '04')
      filename += '.jpg'
      return filename
#
# main
# Reads image files taken in sequence
# and averages them all together to make
# a star trail image.  Also creates a movie
#
if __name__ == "__main__":
      lowerThresh = 128       # lower threshold for noise removal
      lastFile = 170          # Highest file number to process

      starsFirst = readImg(getFilename(19))     # 19 was my first image
      height = starsFirst.shape[0]
      width = starsFirst.shape[1]
      out = cv2.VideoWriter('starTrails.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (width, height))
      out.write(starsFirst)

      for fileNum in range(20, lastFile):
            filename = getFilename(fileNum)
            stars = readImg(filename)
            starsFirst = cv2.add(stars, starsFirst)
            print(filename)
            out.write(starsFirst)         # write a frame to the mpeg file

cv2.imshow('ave', starsFirst)             # Show star trail image
cv2.waitKey(0)
cv2.destroyAllWindows()
