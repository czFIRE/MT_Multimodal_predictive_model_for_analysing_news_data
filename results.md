5 epochs of concatenation of the Roberta model and the ViT model:

```
Accuracy: 0.986181516864886
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.95      0.98      0.96      3870
 left_wing_outside_US       0.99      0.99      0.99     17201
     right_wing_in_US       0.97      0.93      0.95      2374
right_wing_outside_US       0.99      0.99      0.99     17587

             accuracy                           0.99     41032
            macro avg       0.98      0.97      0.97     41032
         weighted avg       0.99      0.99      0.99     41032
```

5 epochs concat Bart-Large-CNN + ViT:
```
Accuracy: 0.9902025297945456
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.98      0.98      0.98      3958
 left_wing_outside_US       0.99      0.99      0.99     17133
     right_wing_in_US       0.97      0.96      0.96      2441
right_wing_outside_US       0.99      0.99      0.99     17499

             accuracy                           0.99     41031
            macro avg       0.98      0.98      0.98     41031
         weighted avg       0.99      0.99      0.99     41031
```

5 epochs concat BGE-Reranker + ViT:
```
Accuracy: 0.9739709000511808
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.93      0.95      0.94      3958
 left_wing_outside_US       0.98      0.98      0.98     17133
     right_wing_in_US       0.91      0.89      0.90      2441
right_wing_outside_US       0.98      0.98      0.98     17499

             accuracy                           0.97     41031
            macro avg       0.95      0.95      0.95     41031
         weighted avg       0.97      0.97      0.97     41031
```


5 epochs plus Bart-Large-CNN + ViT
```
Accuracy: 0.9897394652823475
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.98      0.98      0.98      3958
 left_wing_outside_US       0.99      0.99      0.99     17133
     right_wing_in_US       0.96      0.96      0.96      2441
right_wing_outside_US       0.99      0.99      0.99     17499

             accuracy                           0.99     41031
            macro avg       0.98      0.98      0.98     41031
         weighted avg       0.99      0.99      0.99     41031
```


5 epochs mul Bart-Large-CNN + ViT
```
Accuracy: 0.9898125807316419
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.97      0.98      0.98      3958
 left_wing_outside_US       0.99      0.99      0.99     17133
     right_wing_in_US       0.97      0.96      0.96      2441
right_wing_outside_US       0.99      0.99      0.99     17499

             accuracy                           0.99     41031
            macro avg       0.98      0.98      0.98     41031
         weighted avg       0.99      0.99      0.99     41031
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
Accuracy: 0.9728497964953328
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.93      0.94      0.94      3958
 left_wing_outside_US       0.98      0.98      0.98     17133
     right_wing_in_US       0.90      0.88      0.89      2441
right_wing_outside_US       0.98      0.99      0.98     17499

             accuracy                           0.97     41031
            macro avg       0.95      0.95      0.95     41031
         weighted avg       0.97      0.97      0.97     41031
```


5 epochs add Roberta + ViT
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
Accuracy: 0.9834027930101631
Classification Report:
                       precision    recall  f1-score   support

      left_wing_in_US       0.95      0.97      0.96      3958
 left_wing_outside_US       0.99      0.99      0.99     17133
     right_wing_in_US       0.96      0.92      0.94      2441
right_wing_outside_US       0.99      0.99      0.99     17499

             accuracy                           0.98     41031
            macro avg       0.97      0.97      0.97     41031
         weighted avg       0.98      0.98      0.98     41031
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