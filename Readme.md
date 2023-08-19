# Missing Map Area Prediction on Italy Map

This project aims to predict missing map areas on an Italy map using the K-Nearest Neighbors (KNN) algorithm. The input consists of 5 images labeled from 1 to 5, with missing maps ranging from 10% to 50%. The KNN algorithm is implemented in Python, with varying values of K (1, 3, 5, 7, and 9) used for prediction.

## Project Overview

- **Objective**: Predict missing map areas on an Italy map using KNN.
- **Input**: 5 images labeled 1 to 5 with varying percentages of missing maps (10% to 50%).
- **Algorithm**: K-Nearest Neighbors (KNN) with K values of 1, 3, 5, 7, and 9.
- **Language**: Python

## Project Structure

- `images/`: Contains the input images labeled 1 to 5.
- `src/`: Source code for the KNN algorithm and prediction.
  - `knn.py`: KNN implementation and prediction logic.
  - `main.py`: Main script to execute the prediction.
- `results/`: Directory to store the prediction results.
- `README.md`: Project documentation (this file).

## Usage

1. Place the input images (labeled 1 to 5) in the `images/` directory.
2. Run the `main.py` script to execute the prediction.

```bash
python src/main.py
```

3. The prediction results will be stored in the `results/` directory.

## Requirements

- Python 3.x
- Libraries: scikit-learn, numpy

## Future Improvements

- Explore different distance metrics for KNN.
- Experiment with different image preprocessing techniques.
- Implement more advanced machine learning algorithms for comparison.


## Note

This project does not include actual map data and is for educational and illustrative purposes only.

Feel free to modify and expand upon this project to suit your needs!

**Happy coding!**
