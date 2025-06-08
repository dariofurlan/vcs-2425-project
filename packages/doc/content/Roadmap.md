## Objectives

### 1 - Evalutaion "as-is"

Evaluate the accuracy of the main state of the art models for image classification on **depth images**

Steps:

1. come up with a list of state of the art models for image classification (zero shot ? one shot ? BLIP ? ResNet ?)
2. find a labeled dataset of depth images (or use Depth Map estimation algorithm to generate depth images from RGB images of an existing large dataset)
3. find an evaluation metric for image classification (or more than one ?)
4. evaluate the models on the dataset using the metric(s)
5. compare the results
6. write a report

#### Algorithms

| Model       | Type                             |
| ----------- | -------------------------------- |
| AlexNet     | Convolutional                    |
| VGG         | Convolutional                    |
| ResNet      | Convolutional + Skip Connections |
| BLIP / CLIP | Convolutional + Attention        |

#### Datasets

| Dataset  | Description                                                                  | Depth ?   |
| -------- | ---------------------------------------------------------------------------- | --------- |
| ImageNet | 1.2 million images, 1000 classes of RGB Image (it needs conversion to Depth) | Synthetic |
| CIFAR100 | 60,000 32x32 color images in 100 classes (it needs conversion to Depth)      | Synthetic |
| NYUv2    | 1449 RGB-D images, 894 training and 654 test images                          | Natural   |
| SUN3D    | 415 RGB-D images, 254 training and 161 test images                           | Natural   |

What are depth images ?

- Normal
- Red is closer blue is far

TOPLine: state of the art alg. tested on RGB images. This is the "upper bound".
Baseline: alg. tested on depth images with no fine-tuning. This is the "lower bound".
Everything in between is good.

Feature Extraction from Depth Maps for Object Recognition 
https://stacks.stanford.edu/file/druid:np318ty6250/Jordan_Preprocessing_and_Feature_Extraction_from_Depth_Maps.pdf

### 2 - Custom Algorithm

Fine-tune / train an image classification algorithm to the specific task of classifying **depth images.**

Steps:

1. based on the algorithms that we selected earlier, choose one that we will fine-tune (or more than one ?)
2. find a labeled dataset of depth images (or use Depth Map estimation algorithm to generate depth images from RGB images of an existing large dataset)
3. fine-tune the model on the dataset
4. evaluate the model on the dataset using the metric(s) that we selected earlier

### 3 - Application

Develop a simple application that uses the trained model to detect anomalies using depth images.
In particulare the goal is to help the healthcare operator to detect anomalies in the depth image video stream of elderly people while they are in their room of the retirement house. This is to obtain the advantages of computer vision withouth sacrificing the privacy.
