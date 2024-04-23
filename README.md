# MT_Multimodal_predictive_model_for_analysing_news_data
Diploma thesis repository

## Oficial assignment

This thesis aims to create a predictive tool utilizing a multimodal machine-learning model applied to textual and visual news data provided by an industrial partner of FI MU (Newsmatics, Inc.). The main objective is to develop a machine learning model capable of forecasting the political orientation of news articles, based on a corpus of training data categorized by Newsmatics, Inc. The research encompasses a comprehensive examination of existing multimodal machine learning methodologies, followed by the customization of a pre-existing language model tailored for the specific task of political orientation prediction. Moreover, the thesis delves into the integration of multimodal techniques to investigate whether the inclusion of image data alongside textual content enhances the accuracy of political orientation prediction. The study also includes a comparative analysis between the performance of the language model and the multimodal approaches. The results will be written up in the form of a thesis, and the corresponding implementation will be made available for further validation by the industrial partner.

## Steps to run the project

1. Clone the repository
2. Install the requirements (Python 3.10, pip packages you don't have installed)
3. Download the images using the `image_scraper_parallel.py` script
4. Run all the cells in the `exploratory_analysis.ipynb` notebook (this also does some preprocessing steps)
5. Run the relevant cells in the `testing_models.ipynb` notebook