# Solar Photovoltaic-Thermoelectric (PV-TE) Performance Prediction

## Overview

This project is dedicated to enhancing the performance prediction of solar PV-TE modules across different geographic locations. Utilizing advanced machine learning techniques, we aim to provide accurate predictions of power output and efficiency, contributing to the optimization of solar energy systems worldwide.

## Methodology

We've employed a variety of regressive surrogate machine learning models including Artificial Neural Networks (ANN), Support Vector Regressors (SVR), Gradient Boosting (XGB, LGBM), CatBoost, and Bagging techniques. The models are trained on a rich dataset generated through finite element analysis, incorporating variables such as wind speed, solar irradiance, and ambient temperature.

## Results

The models were evaluated across multiple metrics including MSE (Mean Squared Error), RMSE (Root Mean Squared Error), MAE (Mean Absolute Error), RRMSE (%), and R² Score. The evaluation spanned several countries, providing a global perspective on the efficiency and power output prediction capabilities of each model.

### Best Models for Prediction of Power and Efficiency

Below is a summary of the performance of various models across different countries:

![Best Models Summary](/path/to/your/image.png)

*Figure: Comparative analysis of machine learning models in predicting solar PV-TE module performance across multiple countries.*

### Interpretation of the Results

- **MSE, RMSE, MAE**: Lower values indicate more accurate predictions with less error.
- **RRMSE (%)**: Represents the relative root mean square error in percentage, where lower values signify better model performance.
- **R² Score**: A value close to 1 indicates excellent model performance, showing that the predicted values closely match the actual values.

The visualization shows that models such as ANN, LGBM, and CatBoost tend to offer the best predictions for power output, while Bagging excels in efficiency prediction. The disparity across different geographic locations underscores the importance of localized model tuning.

## How to Use

Interested parties can utilize our findings to select appropriate machine learning models for predicting the performance of solar PV-TE systems in specific regions. The methodology and results sections provide insights into model selection and performance expectations.

## Contributions

We welcome contributions from the community. If you have suggestions or want to improve the models, please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

We extend our gratitude to the researchers and developers whose tools and libraries have made this analysis
