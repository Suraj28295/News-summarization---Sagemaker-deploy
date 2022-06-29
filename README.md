# News-summarization - Sagemaker-deploy

> Train Model
> * Create S3 bucket give Sagemaker necessary access to perform read and write. upload training data files or older external model in the Bucket. 
> * Run main.ipynb - providing some variable(aws configs custom_names and model related) to initiate the training
> * The output will generate a endpoint which can be be called to get the summary of the data
> ** Input Expected - {"data":{"inputs":YOUR_NEWS_TO_SUMMARY} , "model" : (Pick any one option from – T5, bert2bert, distilbart, pegasus)}
> ** Output - summary string
> ** Example, 
![image](https://user-images.githubusercontent.com/25966450/176410424-7ec57c12-5d76-4316-b48a-3d9a65f8fd3f.png)
> * Access the Model using Endpoint and get the live time summary to your text. Choose different models to check which suits your needs.
> * 



> Links
> * Model github link :- https://github.com/Suraj28295/News-summarization---Sagemaker-deploy
> * Model dashboard links :- you can check the performances of the model and endpoint below,
[Endpoint_Latency-Evaluations](https://cloudwatch.amazonaws.com/dashboard.html?dashboard=Endpoint_Latency-Evaluations&context=eyJSIjoidXMtZWFzdC0xIiwiRCI6ImN3LWRiLTY1ODU2ODQxMTYxNyIsIlUiOiJ1cy1lYXN0LTFfVFdLWU5QY3dhIiwiQyI6InFkajBycWRpM2ZqOGU3cWdxdGFlMXQycjgiLCJJIjoidXMtZWFzdC0xOmUzNTQ5ZDdhLTFlMGMtNDFiOC04ZjJiLWU1ZWExNTNjOGFkNCIsIk0iOiJQdWJsaWMifQ==) ,
[Model Performance metric](https://cloudwatch.amazonaws.com/dashboard.html?dashboard=Model_Performance-Metrics&context=eyJSIjoidXMtZWFzdC0xIiwiRCI6ImN3LWRiLTY1ODU2ODQxMTYxNyIsIlUiOiJ1cy1lYXN0LTFfVFdLWU5QY3dhIiwiQyI6InFkajBycWRpM2ZqOGU3cWdxdGFlMXQycjgiLCJJIjoidXMtZWFzdC0xOjJhMjZmYWNkLTA3OTctNGM3Mi05ZjBlLThhZWQ2OTZkNzg0OSIsIk0iOiJQdWJsaWMifQ==)
