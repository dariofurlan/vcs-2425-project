

## Dataset Description
We utilized the validation set of ImageNet, which comprises 50,000 images spanning 1,000 classes. Each image was annotated using the ground truth labels provided by the ImageNet devkit. Subsequently, we converted each image into a single-channel 16-bit depth estimation using Marigold, a monocular depth estimation model.

## Imagenet 1k-class depth

### Baseline Experiment
We initiated our experiments by evaluating the performance of the models "as-is," without any fine-tuning applied to the depth images.

The models employed in this study (AlexNet, VGG19, InceptionV3, ResNet50) were conveniently pretrained on the same 1,000 classes as our dataset. This alignment was achieved by carefully curating the dataset, thereby obviating the need to fine-tune the final layer of the classifier, as it already produced the correct labels.

To establish a baseline and investigate whether the models exhibited varying performance under different colormaps of the depth images, we experimented with a stacked approach, grayscale, viridis, plasma, magma, and Spectral colormaps.

The results are summarized in the following table:

<table>
    <thead>
        <tr>
            <td rowspan="2">Model</td>
            <td colspan="2">Stacked</td>
            <td colspan="2">Grayscale</td>
            <td colspan="2">Viridis</td>
            <td colspan="2">Plasma</td>
            <td colspan="2">Magma</td>
            <td colspan="2">Spectral</td>
        </tr>
        <tr>
            <td>Top-1</td>
            <td>Top-5</td>
            <td>Top-1</td>
            <td>Top-5</td>
            <td>Top-1</td>
            <td>Top-5</td>
            <td>Top-1</td>
            <td>Top-5</td>
            <td>Top-1</td>
            <td>Top-5</td>
            <td>Top-1</td>
            <td>Top-5</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>AlexNet</td>
            <td><b>04.53%</b></td>
            <td><b>11.63%</b></td>
            <td>04.50%</td>
            <td>11.62%</td>
            <td>01.04%</td>
            <td>03.83%</td>
            <td>01.24%</td>
            <td>03.98%</td>
            <td>02.54%</td>
            <td>07.59%</td>
            <td>01.55%</td>
            <td>04.67%</td>
        </tr>
        <tr>
            <td>VGG19</td>
            <td><b>10.04%</b></td>
            <td><b>22.00%</b></td>
            <td>09.97%</td>
            <td>21.79%</td>
            <td>04.64%</td>
            <td>11.87%</td>
            <td>04.29%</td>
            <td>10.95%</td>
            <td>06.45%</td>
            <td>15.31%</td>
            <td>03.32%</td>
            <td>09.50%</td>
        </tr>
        <tr>
            <td>ResNet50</td>
            <td>13.18%</td>
            <td><b>28.16%</b></td>
            <td><b>13.27%</b></td>
            <td>28.16%</td>
            <td>06.56%</td>
            <td>16.23%</td>
            <td>05.83%</td>
            <td>14.00%</td>
            <td>09.71%</td>
            <td>21.44%</td>
            <td>05.70%</td>
            <td>13.90%</td>
        </tr>
        <tr>
            <td>InceptionV3</td>
            <td><b>16.48%</b></td>
            <td><b>33.05%</b></td>
            <td>16.40%</td>
            <td>32.94%</td>
            <td>13.16%</td>
            <td>26.66%</td>
            <td>12.36%</td>
            <td>25.34%</td>
            <td>15.01%</td>
            <td>30.07%</td>
            <td>10.39%</td>
            <td>22.79%</td>
        </tr>
    </tbody>
</table>

![](./model_acc_by_colormap.png)

This experiment demonstrated that the grayscale approach yielded results most familiar to the models. Furthermore, we established that a straightforward approach, such as duplicating the original single-channel depth image to the three channels required by these models, is as robust as applying a colormap function to the grayscale image.

Superior models naturally exhibit better performance, indicating that models with high accuracy on real RGB images also perform well on depth images.

## Fine-Tuning Experiments

Further experimentation involving fine-tuning these models resulted in a significant increase in accuracy. Given the strong performance of the "stacked" colormap, we focused on this approach for fine-tuning and excluded other colormaps from further analysis.

The fine-tuning procedures were as follows:

- **AlexNet**: Initially, we froze the feature layers and trained the classifier layer. Subsequently, we unfroze all layers and trained the entire model.
- **VGG19**: Similar to AlexNet, we performed both partial and complete fine-tuning.
- **ResNet50**: Partial fine-tuning was conducted by unfreezing the last layer (layer 4) and the final fully connected layer (layer 5) and training them.
- **InceptionV3**: Partial fine-tuning involved unfreezing the last inception block (Mixed_7c), the auxiliary classifier (AuxLogits), and the final fully connected layer (layer 5) and training them.

The results are summarized in the table below:

<table>
    <thead>
        <tr>
            <td rowspan="2">Model</td>
            <td colspan="2">No Fine-Tuning</td>
            <td colspan="2">Partial Fine-Tuning</td>
            <td colspan="2">Complete Fine-Tuning</td>
        </tr>
        <tr>
            <td>Top-1</td>
            <td>Top-5</td>
            <td>Top-1</td>
            <td>Top-5</td>
            <td>Top-1</td>
            <td>Top-5</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>AlexNet</td>
            <td>04.53%</td>
            <td>11.63%</td>
            <td>18.05%</td>
            <td>36.41%</td>
            <td><b>23.62%</b></td>
            <td><b>45.76%</b></td>
        </tr>
        <tr>
            <td>VGG19</td>
            <td>10.04%</td>
            <td>22.00%</td>
            <td>25.40%</td>
            <td>48.18%</td>
            <td><b>34.20%</b></td>
            <td><b>60.96%</b></td>
        </tr>
        <tr>
            <td>ResNet50</td>
            <td>13.18%</td>
            <td>28.16%</td>
            <td>32.36%</td>
            <td>57.87%</td>
            <td><b>44.95%</b></td>
            <td><b>71.90%</b></td>
        </tr>
        <tr>
            <td>InceptionV3</td>
            <td>16.48%</td>
            <td>33.05%</td>
            <td>22.31%</td>
            <td>44.57%</td>
            <td><b><u>48.53%</u></b></td>
            <td><b><u>74.53%</u></b></td>
        </tr>
    </tbody>
</table>

Both partial and complete fine-tuning proved effective in enhancing the models' understanding of depth images. However, our dataset was limited in the number of examples per class, which constrained the overall performance. Despite this limitation, the results remain promising.
