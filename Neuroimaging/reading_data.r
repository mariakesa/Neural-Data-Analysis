install.packages("devtools")
install.packages("oro.dicom")
library(oro.dicom)
setwd("/media/maria/DATA1/Documents/Neurohacking_data/BRAINIX/DICOM/FLAIR")
slice=readDICOM("/media/maria/DATA1/Documents/Neurohacking_data/BRAINIX/DICOM/FLAIR/IM-0001-0001.dcm")