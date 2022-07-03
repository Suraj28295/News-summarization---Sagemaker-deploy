## List of CloudWatch queries for getting Latency and Model evaluation dashboard's data.

- ### For Inference Latency 
    - For Lambda Latency,
        - **Average Latency in 5min**,
            filter @type = "REPORT"
            | stats avg(@duration) by bin(5m) 
        - **Min/Max latency and cost query(Only for Lambda)**,
            filter @type = "REPORT"
            | stats max(@duration) as Max_Latency , min(@duration) as Min_Latency , sum(@billedDuration)*0.0000000021 as Total_Running_Cost_dollars , sum(@billedDuration)/60000 as Total_Billable_Minutes
    - For Endpoint Latency,
        - **SQL query for getting average sagemaker endpoint latency**,
            - **Bert2Bert**:- SELECT AVG(ModelLatency) FROM SCHEMA("AWS/SageMaker", EndpointName,VariantName) WHERE EndpointName ='summarization-endpoint-5bert2bert-cnn-daily-mail-1' AND VariantName = 'AllTraffic'
            - **Distilbart**:- SELECT AVG(ModelLatency) FROM SCHEMA("AWS/SageMaker", EndpointName,VariantName) WHERE EndpointName ='summarization-endpoint-5distilbart-cnn-12-6-1' AND VariantName = 'AllTraffic'
            - **Pegasus**:- SELECT AVG(ModelLatency) FROM SCHEMA("AWS/SageMaker", EndpointName,VariantName) WHERE EndpointName ='summarization-endpoint-5pegasus-xsum-1' AND VariantName = 'AllTraffic'
            - **T5**:- SELECT AVG(ModelLatency) FROM SCHEMA("AWS/SageMaker", EndpointName,VariantName) WHERE EndpointName ='summarization-endpoint-5t5-base-cnn-dm-1' AND VariantName = 'AllTraffic'
            
    - **Invocation count**,
        - SELECT AVG(Invocations) FROM SCHEMA("AWS/SageMaker", EndpointName,VariantName) WHERE EndpointName = 'summarization-endpoint-5distilbart-cnn-12-6-1' AND VariantName = 'AllTraffic' 
        (Replace the endpoint names for other model, follow "**For Endpoint Latency**" section)
- ### For Model Evaluation,
    - **For training Latency**,
    filter @logStream in ['huggingface-pytorch-training-2022-06-26-18-32-18-724/algo-1-1656268442',
'huggingface-pytorch-training-2022-06-26-18-05-26-721/algo-1-1656266839',
'huggingface-pytorch-training-2022-06-26-17-22-37-795/algo-1-1656264257',
'huggingface-pytorch-training-2022-06-26-16-50-36-815/algo-1-1656262332',
'pegasus-xsum-2022-06-29-20-04-56-163/algo-1-1656533202']
| fields @timestamp, @message
| stats (max(@timestamp)-min(@timestamp))/60000 as
Model_Training_Time,avg(eval_samples_per_second) as avg_eval_samples_per_second by @logStream
| sort by Model_Training_Time 
