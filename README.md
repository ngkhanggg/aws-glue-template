# AWS Glue Template

A collection of reusable AWS Glue scripts/config for building ETL jobs.

## AWS Glue Local Setup

### Prerequisites
1. VSCode
2. Remote Explorer Extension
3. Docker
4. AWS CLI
5. IAM user credentials (Access key + Secret access key)

### VSCode Setup
1. Use the following command to pull Glue 5.0 image to your device
```
docker pull amazon/aws-glue-libs:5
```

2. Use the following command to configure your aws credentials
```
aws configure
```

3. Open your workspace settings (JSON) in VSCode → Paste the following to your `settings.json` file
```
{
    "python.defaultInterpreterPath": "/usr/bin/python3.11",
    "python.analysis.extraPaths": [
        "/usr/lib/spark/python/lib/py4j-0.10.9.7-src.zip:/usr/lib/spark/python/:/usr/lib/spark/python/lib/",
    ]
}
```

4. Build the Docker container
```
docker run -it --rm -v ~/.aws:/home/hadoop/.aws -v $WORKSPACE_LOCATION:/home/hadoop/workspace/ -e AWS_PROFILE=$PROFILE_NAME --name glue5_pyspark amazon/aws-glue-libs:5 pyspark
```

5. Navigate to `Remote Explorer` → Choose `amazon/aws-glue-libs:5` → `Attach in Current Window`

## References
[Develop & Test AWS Glue 5.0 Jobs Locally Using a Docker Container](https://aws.amazon.com/blogs/big-data/develop-and-test-aws-glue-5-0-jobs-locally-using-a-docker-container/)
