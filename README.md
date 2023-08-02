# Image_Retrieval_with_CNN_and_fastai
My personal practice, doing Image Retrieval with CNN, using fastai, without extra training.


## Result  

### Hightlight

| Dataset | Model | K=1 | K=4 | K=8 |
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

Highlight table: Image Retrieval, Convnext Large model's Precision at K for datasets.

<br>

For all the datasets, Convnext Large has the highest Precision at K, except for Extract 1000 fast, at K=1, with only 0.005 difference from the highest precision at K.

### Metric

Precision at K: The number of **relevant images** among the **top K retrieved images**.  
P@K = The number of **relevant images** among the **top K retrieved images** / K

### Full
Full result including other models (Convnext Small, Resnet152, Efficientv2RwT, EfficientnetB3, Resnet26d, Vgg16):  
---> Result file path: ***log/dataframes_to_excel_result.xlsx***


## Overview of processing steps

1. **Load datasets**. (divided into data images and target images (query images))
2. **Load models**.  
3. **Extract features**. (data images -> data features, target images -> target features)
4. **Compute distances** between target features and data features.
5. **Sort distances** and **get correspoding data images' indexes**.
6. **Compute Precision at K**.

### Datasets

All the datasets are downloaded from fastai, except for Extract 1000 fast, which I manually built.

I extracted a small portion of ImageNet 1k dataset[^1] to make Extract 1000 fast.  
Extract 1000 fast has 100 classes, 10 images each class, total of 1000 images. Which then divided into 800 data images and 200 target images.  

### Models

All the models are downloaded from fastai timm[^2].  
All the models are pruned the last classifying layer. In other words, the **models' output** is the **output of the penultimate fully connected layer**.  

## Quick reproduction

### Main notebooks

- ***ir_cnn_run.ipynb*** (**main**) (**recommend**) (for loop through **each** dataset and **each** model)
- ***ir_cnn.ipynb*** (other version) (**not** recommend) (run **all** datasets and **all** models **at the same time**) (requires huge memory and gpu)

Run time ***ir_cnn_run.ipynb***: **2 hours and 30 seconds** (for my PC setup) (datasets and models downloading time excluded).

### Quick run with different datasets and different models

In the main notebook ***ir_cnn_run.ipynb***:  
1. Modify variables: *dts_li* and *model_li*.  
- *dts_li* is a list of datasets.  
- *model_li* is a list of models.

Make sure each dataset class will have the **same structure** as dataset classes in ***utils_f/data/datacustom.py***,  
and each model class will have the **same structure** as model classes in ***utils_f/model/model_custom.py***

2. Run the notebook.

<br>

Output:
1. Features ---> Directory: ***Feature***
2. Labels ---> Directory: ***Label***
3. Models ---> Directory: ***Model***
4. Log (Precision at K result) ---> File path: ***log/dataframes_to_excel.xlsx***

The **Log output's order** in will be corresponding to the **order of datasets** in dts_li and the **order of models** in model_li, respectively.

Auto download first time running:
1. Fastai datasets ---> Directory: ***Data***
2. Original fastai timm models ---> Directory: ***User/Admin(or user's name)/.cache*** (in C:\ Disk on Windows)

## Note

1. Here, **relevant images** means **images from the same class**.
2. Because models files are too big, I don't upload them here. However, you can get them easily and fast by running the cell/function *save_models* in the main notebook.  
3. Because features files are too big, I don't upload them here. You can get them all, along with labels files, by run the main notebook. It takes about 2 hours run time for my PC setup, datasets and original models downloading time excluded.
4. After getting features files and labels files, you can load them to use. You can use function *get_feature_paths* and *get_label_paths* (from ***utils_f/path.py***) to get the path in the corresponding order, and then use Pytorch function *torch.load* to load them.

## Prerequisite

fastai  
Convolution Neural Network (CNN)  
jupyter notebook  

## My PC setup 

Windows 10 64-bit  
Processor i7-10700 (16 CPUs)  
RAM 16 GB  
GPU NVIDIA GeForce RTX 2060  

## Library Requirement

Pytorch  
fastai  
timm  
jupyter-lab  
nbdev  
pandas  

[^1]: [ImageNet 1k dataset link](https://www.kaggle.com/datasets/kerrit/imagenet1kmediumtest-10k)
[^2]: [fastai timm link](https://timm.fast.ai/)
