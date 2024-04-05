# State of progress 05.04.2024

What's done:
- [x] Preprocessing of the data is done
- [x] Basic NLP prediction models - picked based on popularity of huggingface:
    - [x] RoBERTa
    - [x] BGE reranker
    - [x] BART
    - [x] Basic BERT

- [x] Pretrained image models for image classification
    - [x] ResNet
    - [x] VGG
    - [x] Inception
    - [x] EfficientNet
    - [x] MobileNet
    - [x] ViT

- [x] Multimodal models
    - [x] Concatenation
    - [x] Sum
    - [x] Product
    ***
    - [x] Attention
    - [x] Fusion
    - [x] Late fusion
    - [x] Early fusion
    - [x] Cross-modal attention
    - [x] Cross-modal transformer
    ***

- I tried primarly the late fusion approaches since they are the most popular and the easiest to implement. The results are already good, so I don!t know if it makes sense to even implement early/mid fusion approaches. I will try to implement them in the future, but I will focus on the other parts of the thesis first.

- [x] Evaluation of the models
    - [x] Accuracy
    - [x] F1 score
    - [x] Precision
    - [x] Recall
    - [x] ROC AUC
    - [x] PR AUC
    - [x] Confusion matrix
    - [x] Classification report
    - [x] Loss
    - [x] Learning curve
    - [x] ROC curve
    - [x] Training and inference time
    *** Would be nice:
    - [x] PR curve
    - [x] Calibration curve
    - [x] SHAP values
    - [x] LIME
    - [x] Grad-CAM
    - [x] Saliency maps
    - [x] Integrated gradients
    - [x] SmoothGrad
    - [x] Occlusion sensitivity
    - [x] Feature importance
    - [x] Permutation importance
    - [x] Partial dependence plots
    - [x] Accumulated local effects
    - [x] Individual conditional expectation
    - [x] SHAP interaction values
    - [x] SHAP dependence plots
    - [x] SHAP summary plot
    - [x] SHAP force plot
    - [x] SHAP waterfall
    ***

- [x] Pretrained multimodal models
    - [x] CLIP - Prepared for prime time
    - [x] VisualBERT - Tried, but couldn't get it to work
    *** Would be nice:
    - [x] LXMERT
    - [x] UNITER
    - [x] VL-BERT
    - [x] ViLBERT
    ***

- [x] Plan of implementation part continuation:
    - [x] Train just the basic text models on the data and evaluate them
    - [x] Implement the combination of the image and text models with different fusion methods and print the evaluation
    - [x] Implement the pretrained multimodal models and evaluate them
    - [x] Compare the results of the basic models with the multimodal models
    - [x] Write the results and discussion
    