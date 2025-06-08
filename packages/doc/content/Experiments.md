We adopted the **stacked colormap representation** for both the 200-class ImageNet subset and the Washington RGB-D dataset, since stacked format was observed during preliminary experiments on the full ImageNet validation set as shown in the previous table (table 1)

<br/>

### ImageNet Subset (200 Classes)

We evaluated both **partial** and **complete fine-tuning** across four CNN models. As reported in _Table 1_, full fine-tuning offers **modest yet consistent improvement**s over partial tuning. Despite the lower complexity compared to the full 1,000-class ImageNet task, this 200-class subset still presents a substantial challenge.

<br/>

<table>
    <thead>
        <tr>
            <td rowspan="2">Model</td>
            <td colspan="2">Partial Fine-Tuning</td>
            <td colspan="2">Complete Fine-Tuning</td>
        </tr>
        <tr>
            <td>Top-1</td>
            <td>Top-5</td>
            <td>Top-1</td>
            <td>Top-5</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>AlexNet</td>
            <td>26.25%</td>
            <td> <b> 52.90% <b> </td>
            <td> 26.40% </td>
            <td> <b> 51.25% <b> </td>
        </tr>
        <tr>
            <td>VGG19</td>
            <td>32.50%</td>
            <td> <b> 59.95% <b> </td>
            <td> 36.70% </td>
            <td> <b>  65.25% <b>  </td>
        </tr>
        <tr>
            <td>ResNet50</td>
            <td>44.30% </td>
            <td><b> 71.15% <b> </td>
            <td> 47.75% </td>
            <td> <b> 73.20%  <b> </td>
        </tr>
        <tr>
            <td>InceptionV3</td>
            <td>38.70%</td>
            <td><b> 64.15% <b> </td>
            <td> 47.95% </td>
            <td> <b> 72.80% <b>  </td>
        </tr>
    </tbody>
</table>

_Table 2: Accuracy comparison for 200-class ImageNet subset_

The observed **Top-1** accuracies show that targeted fine-tuning on a reduced label space significantly improves performance compared to tasks with many classes

<br/>

#### Washington RGB-D Dataset

In contrast, the Washington RGB-D dataset comprises only **51 classes**, representing a significantly **lower task complexity**. As shown in _Table 3_, all models achieved **near 90% Top-1 accuracy**, with VGG19 reaching up to **92.23%**.

<br/>

<table>
    <thead>
        <tr>
            <td rowspan="2">Model</td>
            <td colspan="2">Partial Fine-Tuning</td>
        </tr>
        <tr>
            <td>Top-1</td>
            <td>Top-5</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>AlexNet</td>
            <td> <b>87.51%<b> </td>
            <td> <b>98.79%<b> </td>
        </tr>
        <tr>
            <td>VGG19</td>
            <td> <b> 92.23% <b> </td>
            <td> <b> 99.61% <b> </td>
        </tr>
        <tr>
            <td>ResNet50</td>
            <td> <b> 88.48% <b></td>
            <td> <b> 99.31% <b></td>
        </tr>
        <tr>
            <td>InceptionV3</td>
            <td> <b> 89.45% <b> </td>
            <td><b> 99.08% <b></td>
        </tr>
    </tbody>
</table>

_Table 3: Partial fine-tuning accuracy on Washington RGB-D_

These results were obtained using **partial fine-tuning alone**. Given this high baseline, we opted not to undertake full fine-tuning, concluding that the incremental improvements would not justify the higher computational expense.
