# Image_Retrieval_with_CNN_and_fastai
My personal practice, doing Image Retrieval with CNN, using fastai, without extra training.


## Result  

| Dataset | Model | R=1 | R=4 | R=8 |
| ------- | ----- | --- | --- | --- |
| mnist | convnext large | 0.9243 | 0.9021 | 0.8869 |
| cifar 100 | convnext large | 0.4185 | 0.3502 | 0.3174 |
| cifar 10 | convnext large | 0.6405 | 0.6032 | 0.5796 |
| imagenette 320px | convnext large | 0.9962 | 0.9958 | 0.9956 |
| imagenette 160px | convnext large | 0.9857 | 0.9855 | 0.9846 |
| imagewoof 320px | convnext large | 0.9646 | 0.962 | 0.9607 |
| imagewoof 160px | convnext large | 0.9384 | 0.9332 | 0.9318 |
| cub 200 2011 | convnext large | 0.767 | 0.7239 | 0.6911 |
| caltech 101 | convnext large | 0.9535 | 0.943 | 0.9289 |
| extract 1000 fast | convnext large | 0.875 | 0.8688 | 0.8069 |  

Full result ---> Log file path: **log/dataframes_to_excel_result.xlsx**
