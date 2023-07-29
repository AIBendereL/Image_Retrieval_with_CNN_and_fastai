# Image_Retrieval_with_CNN_and_fastai
My personal practice, doing Image Retrieval with CNN, using fastai, without extra training.

## Image Retrieval with CNN
Image Retrival: retrieve images from a given dataset that are similar to a query image.  
With CNN:  
+ A query image -> CNN -> image features
+ Dataset images -> CNN -> images features
+ Get distance of image features and images features. Sort them from small to big.
+ The images from the dataset with the smallest distance to the query image, are the most relevant.

-> Straight forward and high-precision  

## Why use fastai?  

+ fastai provides convenient datasets downloading.  
+ fastai timm provides convenient models downloading.
+ fastai library helps reducing boilerplate code.
+ fastai library helps simplify code.

## R-precision Metric  

+ For top R images retrieved, number of relevant images -> n relevant image / R.
+ For the experiment, relevant means the images are the same class.

## Table of result  

+ Path: log/dataframes_to_excel_result.xlsx
+ Model:
+ ConvnextLarge has the highest R-precision (R: 1->8) for all datasets, except for Extract1000Fast, with only 0.005 difference in 1-precision from top 1 model.
+ ConvnextLarge has R-precision: 0.4185 -> 0.9962 (R: 1) and 0.3174 -> 0.9956 (R: 8)




