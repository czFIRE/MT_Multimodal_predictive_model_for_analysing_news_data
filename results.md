5 epochs of concatenation of the Roberta model and the ViT model:

```
Accuracy: 0.9878628354171236
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9632    0.9783    0.9707      3958
 left_wing_outside_US     0.9919    0.9911    0.9915     17133
     right_wing_in_US     0.9661    0.9463    0.9561      2441
right_wing_outside_US     0.9925    0.9926    0.9926     17499

             accuracy                         0.9879     41031
            macro avg     0.9784    0.9771    0.9777     41031
         weighted avg     0.9879    0.9879    0.9879     41031
```

5 epochs mul  Reranker + ViT
```
Accuracy: 0.952645560673637
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.90      0.88      0.89      3958
 left_wing_outside_US       0.97      0.97      0.97     17133
     right_wing_in_US       0.79      0.80      0.80      2441
right_wing_outside_US       0.97      0.97      0.97     17499

             accuracy                           0.95     41031
            macro avg       0.91      0.91      0.91     41031
         weighted avg       0.95      0.95      0.95     41031
```


5 epochs add Reranker + ViT
```
./trained_models/bge-reranker-large_vit-base-patch16-224_add.pt
Accuracy: 0.9721186420023884
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9218    0.9505    0.9359      3958
 left_wing_outside_US     0.9833    0.9805    0.9819     17133
     right_wing_in_US     0.9155    0.8517    0.8824      2441
right_wing_outside_US     0.9803    0.9856    0.9829     17499

             accuracy                         0.9721     41031
            macro avg     0.9502    0.9421    0.9458     41031
         weighted avg     0.9720    0.9721    0.9720     41031
```


REPEAT!!! 5 epochs add Roberta + ViT
```
Accuracy: 0.9869367063927275
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.96      0.98      0.97      3958
 left_wing_outside_US       0.99      0.99      0.99     17133
     right_wing_in_US       0.96      0.94      0.95      2441
right_wing_outside_US       0.99      0.99      0.99     17499

             accuracy                           0.99     41031
            macro avg       0.98      0.97      0.98     41031
         weighted avg       0.99      0.99      0.99     41031
```




5 epochs mul Roberta + ViT
```
./trained_models/roberta-base_vit-base-patch16-224_mul.pt
Accuracy: 0.9807706368355633
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9617    0.9578    0.9597      3958
 left_wing_outside_US     0.9803    0.9896    0.9850     17133
     right_wing_in_US     0.9735    0.8869    0.9282      2441
right_wing_outside_US     0.9864    0.9904    0.9884     17499

             accuracy                         0.9808     41031
            macro avg     0.9755    0.9562    0.9653     41031
         weighted avg     0.9807    0.9808    0.9806     41031
```

5 epochs concat Roberta + Resnet
```
Accuracy: 0.9806731495698374
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.93      0.98      0.96      3958
 left_wing_outside_US       0.99      0.98      0.99     17133
     right_wing_in_US       0.96      0.90      0.93      2441
right_wing_outside_US       0.99      0.99      0.99     17499

             accuracy                           0.98     41031
            macro avg       0.97      0.96      0.96     41031
         weighted avg       0.98      0.98      0.98     41031
```

5 epochs Roberta:
```
Accuracy: 0.9821598303721576
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.94      0.98      0.96      3958
 left_wing_outside_US       0.99      0.99      0.99     17133
     right_wing_in_US       0.96      0.91      0.94      2441
right_wing_outside_US       0.99      0.99      0.99     17499

             accuracy                           0.98     41031
            macro avg       0.97      0.97      0.97     41031
         weighted avg       0.98      0.98      0.98     41031
```

Roberta + ConvNext add texts
```
./trained_models/roberta-base_convnext-base-224-22k_add.pt
Accuracy: 0.9876678608856718
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9558    0.9823    0.9689      3958
 left_wing_outside_US     0.9931    0.9896    0.9913     17133
     right_wing_in_US     0.9724    0.9521    0.9621      2441
right_wing_outside_US     0.9919    0.9919    0.9919     17499

             accuracy                         0.9877     41031
            macro avg     0.9783    0.9790    0.9786     41031
         weighted avg     0.9877    0.9877    0.9877     41031
```

Roberta + ConvNext mul
```
./trained_models/roberta-base_convnext-base-224-22k_mul.pt
Accuracy: 0.9892276571372864
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9626    0.9818    0.9721      3958
 left_wing_outside_US     0.9937    0.9898    0.9917     17133
     right_wing_in_US     0.9775    0.9594    0.9684      2441
right_wing_outside_US     0.9926    0.9945    0.9936     17499

             accuracy                         0.9892     41031
            macro avg     0.9816    0.9814    0.9814     41031
         weighted avg     0.9893    0.9892    0.9892     41031
```


BeIT + Roberta add texts
```
./trained_models/roberta-base_beit-base-patch16-224-pt22k-ft22k_add.pt
Accuracy: 0.9879359508664181
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9656    0.9783    0.9719      3958
 left_wing_outside_US     0.9918    0.9912    0.9915     17133
     right_wing_in_US     0.9683    0.9496    0.9588      2441
right_wing_outside_US     0.9919    0.9922    0.9921     17499

             accuracy                         0.9879     41031
            macro avg     0.9794    0.9778    0.9786     41031
         weighted avg     0.9879    0.9879    0.9879     41031
```

BeIT + bart large cnn add texts

```
./trained_models/bart-large-cnn_beit-base-patch16-224-pt22k-ft22k_add.pt
Accuracy: 0.9908118252053325
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9783    0.9798    0.9790      3958
 left_wing_outside_US     0.9936    0.9931    0.9933     17133
     right_wing_in_US     0.9732    0.9660    0.9696      2441
right_wing_outside_US     0.9933    0.9946    0.9939     17499

             accuracy                         0.9908     41031
            macro avg     0.9846    0.9834    0.9840     41031
         weighted avg     0.9908    0.9908    0.9908     41031
```

BeIT + Bart large CNN mul texts
```
./trained_models/bart-large-cnn_beit-base-patch16-224-pt22k-ft22k_mul.pt
Accuracy: 0.9903975043259974
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9776    0.9808    0.9792      3958
 left_wing_outside_US     0.9929    0.9922    0.9925     17133
     right_wing_in_US     0.9729    0.9697    0.9713      2441
right_wing_outside_US     0.9933    0.9937    0.9935     17499

             accuracy                         0.9904     41031
            macro avg     0.9842    0.9841    0.9841     41031
         weighted avg     0.9904    0.9904    0.9904     41031
```


BeIT + Bart large CNN mul titles:

```
Accuracy: 0.9577148984913846
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.92      0.92      0.92      3958
 left_wing_outside_US       0.97      0.97      0.97     17133
     right_wing_in_US       0.89      0.88      0.89      2441
right_wing_outside_US       0.96      0.97      0.97     17499

             accuracy                           0.96     41031
            macro avg       0.94      0.93      0.93     41031
         weighted avg       0.96      0.96      0.96     41031

```

ViT + Bart-Large-CNN concat titles only:
```
Accuracy: 0.9498671736004485
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.90      0.91      0.91      3958
 left_wing_outside_US       0.96      0.96      0.96     17133
     right_wing_in_US       0.88      0.84      0.86      2441
right_wing_outside_US       0.96      0.96      0.96     17499

             accuracy                           0.95     41031
            macro avg       0.93      0.92      0.92     41031
         weighted avg       0.95      0.95      0.95     41031
```


ViT + Bart-Large-CNN mul titles only:
```
Accuracy: 0.9500134044990373
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.90      0.92      0.91      3958
 left_wing_outside_US       0.96      0.96      0.96     17133
     right_wing_in_US       0.88      0.83      0.86      2441
right_wing_outside_US       0.96      0.96      0.96     17499

             accuracy                           0.95     41031
            macro avg       0.93      0.92      0.92     41031
         weighted avg       0.95      0.95      0.95     41031
```

Roberta convnext concat 
```
./trained_models/roberta-base_convnext-base-224-22k_concat.pt
Accuracy: 0.9891301698715605
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9684    0.9826    0.9754      3958
 left_wing_outside_US     0.9918    0.9917    0.9917     17133
     right_wing_in_US     0.9770    0.9590    0.9680      2441
right_wing_outside_US     0.9930    0.9923    0.9927     17499

             accuracy                         0.9891     41031
            macro avg     0.9825    0.9814    0.9819     41031
         weighted avg     0.9891    0.9891    0.9891     41031
```

Bart + Convnext mul
```
./trained_models/bart-large-cnn_convnext-base-224-22k_mul.pt
Accuracy: 0.9913967487996881
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9783    0.9798    0.9790      3958
 left_wing_outside_US     0.9944    0.9943    0.9943     17133
     right_wing_in_US     0.9695    0.9623    0.9659      2441
right_wing_outside_US     0.9945    0.9953    0.9949     17499

             accuracy                         0.9914     41031
            macro avg     0.9842    0.9829    0.9835     41031
         weighted avg     0.9914    0.9914    0.9914     41031
```

Roberta + ConvNext + add
```
Accuracy: 0.9876678608856718
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9558    0.9823    0.9689      3958
 left_wing_outside_US     0.9931    0.9896    0.9913     17133
     right_wing_in_US     0.9724    0.9521    0.9621      2441
right_wing_outside_US     0.9919    0.9919    0.9919     17499

             accuracy                         0.9877     41031
            macro avg     0.9783    0.9790    0.9786     41031
         weighted avg     0.9877    0.9877    0.9877     41031
```

roberta + beit + mul
```
Accuracy: 0.9877166045185347
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9603    0.9831    0.9715      3958
 left_wing_outside_US     0.9916    0.9903    0.9909     17133
     right_wing_in_US     0.9764    0.9484    0.9622      2441
right_wing_outside_US     0.9918    0.9918    0.9918     17499

             accuracy                         0.9877     41031
            macro avg     0.9800    0.9784    0.9791     41031
         weighted avg     0.9878    0.9877    0.9877     41031
```

bge + convnext + mul:
```
Accuracy: 0.9634666471692135
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.8885    0.9406    0.9138      3958
 left_wing_outside_US     0.9838    0.9695    0.9766     17133
     right_wing_in_US     0.8844    0.8214    0.8517      2441
right_wing_outside_US     0.9720    0.9825    0.9772     17499

             accuracy                         0.9635     41031
            macro avg     0.9322    0.9285    0.9298     41031
         weighted avg     0.9636    0.9635    0.9634     41031
```

bge + convnext + concat
```
Accuracy: 0.9789914942360655
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9413    0.9603    0.9507      3958
 left_wing_outside_US     0.9847    0.9864    0.9856     17133
     right_wing_in_US     0.9250    0.9295    0.9273      2441
right_wing_outside_US     0.9897    0.9829    0.9863     17499

             accuracy                         0.9790     41031
            macro avg     0.9602    0.9648    0.9625     41031
         weighted avg     0.9791    0.9790    0.9790     41031
```

bge + convnext + add
```
Accuracy: 0.9787721478881821
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9512    0.9512    0.9512      3958
 left_wing_outside_US     0.9867    0.9846    0.9856     17133
     right_wing_in_US     0.9299    0.9238    0.9268      2441
right_wing_outside_US     0.9840    0.9870    0.9855     17499

             accuracy                         0.9788     41031
            macro avg     0.9630    0.9617    0.9623     41031
         weighted avg     0.9788    0.9788    0.9788     41031
```

bge + beit + concat
```
Accuracy: 0.9793326996661061
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9400    0.9616    0.9507      3958
 left_wing_outside_US     0.9854    0.9856    0.9855     17133
     right_wing_in_US     0.9449    0.9136    0.9290      2441
right_wing_outside_US     0.9872    0.9864    0.9868     17499

             accuracy                         0.9793     41031
            macro avg     0.9644    0.9618    0.9630     41031
         weighted avg     0.9794    0.9793    0.9793     41031
```

bge + beit + mul
```
Accuracy: 0.9680241768419
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9015    0.9338    0.9173      3958
 left_wing_outside_US     0.9851    0.9751    0.9801     17133
     right_wing_in_US     0.8770    0.8615    0.8692      2441
right_wing_outside_US     0.9795    0.9837    0.9816     17499

             accuracy                         0.9680     41031
            macro avg     0.9358    0.9385    0.9371     41031
         weighted avg     0.9682    0.9680    0.9681     41031
```

bge + beit + add
```
Accuracy: 0.9782115961102581
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9416    0.9618    0.9516      3958
 left_wing_outside_US     0.9866    0.9831    0.9849     17133
     right_wing_in_US     0.9228    0.9205    0.9217      2441
right_wing_outside_US     0.9862    0.9851    0.9856     17499

             accuracy                         0.9782     41031
            macro avg     0.9593    0.9627    0.9610     41031
         weighted avg     0.9783    0.9782    0.9782     41031
```

bart + resnet + add
```
Accuracy: 0.9895932343837586
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9770    0.9752    0.9761      3958
 left_wing_outside_US     0.9929    0.9922    0.9926     17133
     right_wing_in_US     0.9589    0.9644    0.9616      2441
right_wing_outside_US     0.9935    0.9938    0.9937     17499

             accuracy                         0.9896     41031
            macro avg     0.9806    0.9814    0.9810     41031
         weighted avg     0.9896    0.9896    0.9896     41031
```

bart + resnet + mul
```
Accuracy: 0.9887645926250883
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9714    0.9783    0.9748      3958
 left_wing_outside_US     0.9915    0.9926    0.9920     17133
     right_wing_in_US     0.9651    0.9525    0.9588      2441
right_wing_outside_US     0.9933    0.9925    0.9929     17499

             accuracy                         0.9888     41031
            macro avg     0.9803    0.9789    0.9796     41031
         weighted avg     0.9888    0.9888    0.9888     41031
```

bart + resnet + concat
```
Accuracy: 0.9902025297945456
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9739    0.9816    0.9777      3958
 left_wing_outside_US     0.9932    0.9929    0.9931     17133
     right_wing_in_US     0.9661    0.9586    0.9624      2441
right_wing_outside_US     0.9943    0.9939    0.9941     17499

             accuracy                         0.9902     41031
            macro avg     0.9819    0.9818    0.9818     41031
         weighted avg     0.9902    0.9902    0.9902     41031
```

roberta + resnet + mul
```
Accuracy: 0.984523896566011
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9514    0.9752    0.9632      3958
 left_wing_outside_US     0.9902    0.9876    0.9889     17133
     right_wing_in_US     0.9560    0.9340    0.9449      2441
right_wing_outside_US     0.9906    0.9906    0.9906     17499

             accuracy                         0.9845     41031
            macro avg     0.9720    0.9719    0.9719     41031
         weighted avg     0.9846    0.9845    0.9845     41031
```

roberta + resnet + add
```
Accuracy: 0.9821598303721576
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9482    0.9720    0.9600      3958
 left_wing_outside_US     0.9897    0.9848    0.9873     17133
     right_wing_in_US     0.9479    0.9172    0.9323      2441
right_wing_outside_US     0.9872    0.9909    0.9891     17499

             accuracy                         0.9822     41031
            macro avg     0.9683    0.9662    0.9672     41031
         weighted avg     0.9822    0.9822    0.9821     41031
```

bge + resnet + add
```
Accuracy: 0.9726304501474495
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9341    0.9495    0.9417      3958
 left_wing_outside_US     0.9807    0.9825    0.9816     17133
     right_wing_in_US     0.8919    0.8857    0.8888      2441
right_wing_outside_US     0.9848    0.9803    0.9826     17499

             accuracy                         0.9726     41031
            macro avg     0.9479    0.9495    0.9487     41031
         weighted avg     0.9727    0.9726    0.9726     41031
```

bge + resnet + mul
```
Accuracy: 0.9721186420023884
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9260    0.9487    0.9372      3958
 left_wing_outside_US     0.9799    0.9819    0.9809     17133
     right_wing_in_US     0.8990    0.8894    0.8942      2441
right_wing_outside_US     0.9853    0.9794    0.9823     17499

             accuracy                         0.9721     41031
            macro avg     0.9476    0.9498    0.9487     41031
         weighted avg     0.9722    0.9721    0.9721     41031
```

bge + resnet + concat
```
Accuracy: 0.9641734298457264
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9113    0.9298    0.9205      3958
 left_wing_outside_US     0.9829    0.9691    0.9760     17133
     right_wing_in_US     0.8589    0.8677    0.8633      2441
right_wing_outside_US     0.9730    0.9806    0.9768     17499

             accuracy                         0.9642     41031
            macro avg     0.9315    0.9368    0.9341     41031
         weighted avg     0.9644    0.9642    0.9643     41031
```

bart + convnext + add
```
Accuracy: 0.9916892105968658
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9820    0.9793    0.9806      3958
 left_wing_outside_US     0.9935    0.9942    0.9938     17133
     right_wing_in_US     0.9765    0.9721    0.9743      2441
right_wing_outside_US     0.9942    0.9948    0.9945     17499

             accuracy                         0.9917     41031
            macro avg     0.9866    0.9851    0.9858     41031
         weighted avg     0.9917    0.9917    0.9917     41031
```

bart + convnext + concat
```
./trained_models/bart-large-cnn_convnext-base-224-22k_concat.pt
Accuracy: 0.9913723769832565
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9781    0.9818    0.9800      3958
 left_wing_outside_US     0.9938    0.9940    0.9939     17133
     right_wing_in_US     0.9765    0.9685    0.9724      2441
right_wing_outside_US     0.9941    0.9942    0.9941     17499

             accuracy                         0.9914     41031
            macro avg     0.9856    0.9846    0.9851     41031
         weighted avg     0.9914    0.9914    0.9914     41031
```

reranker + beit + concat
```
./trained_models/bart-large-cnn_beit-base-patch16-224-pt22k-ft22k_concat.pt
Accuracy: 0.9912017742682362
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9784    0.9828    0.9806      3958
 left_wing_outside_US     0.9932    0.9943    0.9938     17133
     right_wing_in_US     0.9731    0.9635    0.9683      2441
right_wing_outside_US     0.9946    0.9939    0.9943     17499

             accuracy                         0.9912     41031
            macro avg     0.9848    0.9836    0.9842     41031
         weighted avg     0.9912    0.9912    0.9912     41031
```

reranker + vit + mul
```
./trained_models/bge-reranker-large_vit-base-patch16-224_mul.pt
Accuracy: 0.9731422582925106
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9247    0.9500    0.9372      3958
 left_wing_outside_US     0.9809    0.9825    0.9817     17133
     right_wing_in_US     0.9231    0.8804    0.9012      2441
right_wing_outside_US     0.9835    0.9822    0.9828     17499

             accuracy                         0.9731     41031
            macro avg     0.9531    0.9488    0.9507     41031
         weighted avg     0.9731    0.9731    0.9731     41031
```

reranker + vit + concat
```
./trained_models/bge-reranker-large_vit-base-patch16-224_concat.pt
Accuracy: 0.9723867319831347
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9196    0.9480    0.9336      3958
 left_wing_outside_US     0.9823    0.9818    0.9821     17133
     right_wing_in_US     0.9131    0.8652    0.8885      2441
right_wing_outside_US     0.9828    0.9836    0.9832     17499

             accuracy                         0.9724     41031
            macro avg     0.9495    0.9447    0.9468     41031
         weighted avg     0.9724    0.9724    0.9723     41031
```

roberta + vit + mul
```
./trained_models/roberta-base_vit-base-patch16-224_mul.pt
Accuracy: 0.9865955009626868
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9563    0.9785    0.9673      3958
 left_wing_outside_US     0.9920    0.9894    0.9907     17133
     right_wing_in_US     0.9700    0.9394    0.9544      2441
right_wing_outside_US     0.9906    0.9923    0.9914     17499

             accuracy                         0.9866     41031
            macro avg     0.9772    0.9749    0.9760     41031
         weighted avg     0.9866    0.9866    0.9866     41031
```

bart + vit + concat
```
./trained_models/bart-large-cnn_vit-base-patch16-224_concat.pt
Accuracy: 0.9909580561039214
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9769    0.9831    0.9800      3958
 left_wing_outside_US     0.9928    0.9940    0.9934     17133
     right_wing_in_US     0.9719    0.9631    0.9675      2441
right_wing_outside_US     0.9950    0.9937    0.9943     17499

             accuracy                         0.9910     41031
            macro avg     0.9841    0.9835    0.9838     41031
         weighted avg     0.9910    0.9910    0.9910     41031
```

reranker + vit + add
```
./trained_models/bge-reranker-large_vit-base-patch16-224_add.pt
Accuracy: 0.9691209085813166
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9002    0.9439    0.9216      3958
 left_wing_outside_US     0.9828    0.9788    0.9808     17133
     right_wing_in_US     0.9118    0.8472    0.8783      2441
right_wing_outside_US     0.9795    0.9824    0.9810     17499

             accuracy                         0.9691     41031
            macro avg     0.9436    0.9381    0.9404     41031
         weighted avg     0.9692    0.9691    0.9690     41031
```

roberta beit concat
```
Accuracy: 0.9884477590114791
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9674    0.9813    0.9743      3958
 left_wing_outside_US     0.9921    0.9910    0.9915     17133
     right_wing_in_US     0.9700    0.9541    0.9620      2441
right_wing_outside_US     0.9923    0.9923    0.9923     17499

             accuracy                         0.9884     41031
            macro avg     0.9804    0.9797    0.9800     41031
         weighted avg     0.9885    0.9884    0.9884     41031
```

roberta vit concat
```
Accuracy: 0.9878628354171236
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US     0.9632    0.9783    0.9707      3958
 left_wing_outside_US     0.9919    0.9911    0.9915     17133
     right_wing_in_US     0.9661    0.9463    0.9561      2441
right_wing_outside_US     0.9925    0.9926    0.9926     17499

             accuracy                         0.9879     41031
            macro avg     0.9784    0.9771    0.9777     41031
         weighted avg     0.9879    0.9879    0.9879     41031
```