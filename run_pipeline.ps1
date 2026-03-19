# run_pipeline.ps1
# Automates the Hadoop data analytics pipeline

Write-Host "Checking if Hadoop cluster is up..."
$containers = docker ps --filter "status=running" --format "{{.Names}}"
if ($containers -notcontains "namenode") {
    Write-Host "Error: Namenode container is not running. Starting cluster..."
    docker compose up -d
    Start-Sleep -Seconds 30
}

Write-Host "Creating HDFS input directory..."
docker exec namenode hdfs dfs -mkdir -p /input

Write-Host "Uploading dataset to HDFS..."
# Copy locally first to container, then to HDFS
docker cp "Most starred Github Repositories.csv" namenode:/tmp/dataset.csv
docker exec namenode hdfs dfs -put -f /tmp/dataset.csv /input/github_repos.csv

Write-Host "Running Hadoop MapReduce job..."
# Find the streaming jar path (assuming 3.2.1 based on image tag)
$streamingJar = "/opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar"

# Delete output if exists
docker exec namenode hdfs dfs -rm -r -f /output

docker cp mapper.py namenode:/tmp/mapper.py
docker cp reducer.py namenode:/tmp/reducer.py

docker exec namenode hadoop jar $streamingJar `
    -input /input/github_repos.csv `
    -output /output `
    -mapper "python3 /tmp/mapper.py" `
    -reducer "python3 /tmp/reducer.py" `
    -file /tmp/mapper.py `
    -file /tmp/reducer.py

Write-Host "Retrieving results from HDFS..."
docker exec namenode hdfs dfs -getmerge /output /tmp/output.csv
docker cp namenode:/tmp/output.csv ./output.csv

Write-Host "Pipeline completed! Results saved to output.csv"
