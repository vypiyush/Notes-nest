@echo off

:: Connection String
:: Set MongoDB connection details
set MONGO_HOST=localhost
set MONGO_PORT=27017
set MONGO_DB=myDB

:: Set AWS S3 details
set AWS_S3_BUCKET=mongosafeauto
set AWS_S3_PREFIX=backups/

:: Create a timestamp for the backup folder
set TIMESTAMP=%date:~4,2%-%date:~7,2%-%date:~10,4%_%time:~0,2%-%time:~3,2%

:: Perform MongoDB backup using mongodump
mongodump --uri "mongodb://%MONGO_HOST%:%MONGO_PORT%" --db %MONGO_DB% --out "C:\Users\lenovo\OneDrive\Desktop\Hustle\Intern\0 CLOUD COMPUTING\PROJECT\localbackup\%TIMESTAMP%"

:: Upload the backup to AWS S3 (assuming you have aws-cli configured with IAM role)
aws s3 cp "C:\Users\lenovo\OneDrive\Desktop\Hustle\Intern\0 CLOUD COMPUTING\PROJECT\localbackup\%TIMESTAMP%" s3://%AWS_S3_BUCKET%/%AWS_S3_PREFIX%%TIMESTAMP% --recursive

:: Clean up the local backup folder
rmdir /s /q "C:\Users\lenovo\OneDrive\Desktop\Hustle\Intern\0 CLOUD COMPUTING\PROJECT\localbackup\%TIMESTAMP%"

echo Backup completed!
