# CS109B - Final project: Predicting movie genres
### Spring 2017, Harvard

#### Team
- Angela Ambroz
- Keun-Hwi Lee
- Johanna Ramos
- Pranav Sidhwani

---- 

## Updates (as of 3 May 2017)

We consolidated all the code into several notebooks, which are located [here, in the `milestone_5` subdirectory](https://github.com/QuinnLee/cs109-project/tree/master/notebooks/milestone_5).  All of the [previous milestone notebooks](https://github.com/QuinnLee/cs109-project/tree/master/notebooks) are in their respective directories.

The main update is in how we pre-processed and cleaned the data.  We faced some limitations, due to our AWS instance's memory constraints (not storage), and setbacks in the multi-label vs multi-class models. 

- [`Fetch-and-sample-data.ipynb`](https://github.com/QuinnLee/cs109-project/blob/master/notebooks/milestone_5/Fetch-and-sample-data.ipynb) - This notebook scraped the data from TMDB.  We used a EC2 instance to scrape the data over several days. 
- [`flatten-data.ipynb`](https://github.com/QuinnLee/cs109-project/blob/master/notebooks/milestone_5/flatten-data.ipynb) - This notebook was used to flatten data.  Features such as cast and crew were lists; we flattened each item in the list into a (one-hot encoded) feature on the data set.
- [`create-test-train-data.ipynb`](https://github.com/QuinnLee/cs109-project/blob/master/notebooks/milestone_5/create-test-train-data.ipynb) - This notebook created the test data set, as well as, downloaded/pre-processed the images for the training and test set. 
- [`aa_ML5_naive_bayes.ipynb`](https://github.com/QuinnLee/cs109-project/blob/master/notebooks/milestone_5/aa_ML5_naive_bayes.ipynb) - Used in Milestone 3, updated to use the latest train and test data.
- [`jr_SVM_mutilabel_v0.ipynb`](https://github.com/QuinnLee/cs109-project/blob/master/notebooks/milestone_5/jr_SVM_mutilabel_v0.ipynb) - Used in Milestone 3, updated to use the latest train and test data.
- [`milestone-5-cnn-and-pretrain-cnn-models.ipynb`](https://github.com/QuinnLee/cs109-project/blob/master/notebooks/milestone_5/milestone-5-cnn-and-pretrain-cnn-models.ipynb) - Used in Milestone 4, some tweaks were added. Updated to use the latest train and test data.

Note: We did not use the Tensorboard in the final write-up, but the code can be found [here](https://github.com/QuinnLee/cs109-project/blob/master/notebooks/milestone_4/ql-tensor-board-ml4.ipynb).

## Data

**[Final dataset (.zip)](https://s3.amazonaws.com/cs109b-data/final_data.zip)**

Pre-processed data for CNN
- [`test_X (.npy)`](https://s3.amazonaws.com/cs109b-data/test_X_array.npy)
- [`test_y (.npy)`](https://s3.amazonaws.com/cs109b-data/test_y_array.npy)
- [`train_y (.npy)`](https://s3.amazonaws.com/cs109b-data/Y_array.npy)
- [`train_X (.npy)`](https://s3.amazonaws.com/cs109b-data/X_array.npy)

JSON format of the data, cleaned
- [`testing_4-29.json`](https://s3.amazonaws.com/cs109b-data/testing_4-29.json)
- [`training_4-29.json`](https://s3.amazonaws.com/cs109b-data/training_4-29.json)

Whole data set, used to create both test and train
- [`themoviedb-4-18-2017.json`](https://s3.amazonaws.com/cs109b-data/themoviedb-4-18-2017.json)

Original, uncleaned train set
- [`themoviedb-sample-4-17-2017.json`](https://s3.amazonaws.com/cs109b-data/themoviedb-sample-4-17-2017.json)


--------

<p><small>This project template was based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
