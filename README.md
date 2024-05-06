# thesis
Install libraries with requirements.txt

Run youtube_query.py in order to get the csv files for the comments from the YouTube videos. 
The script must be run 3 times, with a different video_id each time, to get 3 csv files. 

Preprocess the data using preprocessing.ipynb. 

I highly recommend running the file LLM.ipynb in Google Colab if you don't have access to GPU on your local machine. 
This notebook makes use of the Qwen 1.5 language model to label the comments with a polarity score. 

After having labeled the comments, run the notebook polarity_calc.ipynb to get the polarization indices and plots. 