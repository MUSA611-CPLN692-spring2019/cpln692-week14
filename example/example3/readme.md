# Hosting files on Amazon s3

## Step 1: Create a free account
https://aws.amazon.com/s3/

Although there is a generous free tier, registering does requires a credit card. This is absolutely not necessary for the course.

## Step 2:

Upload your .mbtiles


## Step 3:

Set appropriate permissions:
- Make it a public repo through the console  
  - May need to click around a bit, but it's fairly clear.
- Enable [CORS access](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-cors-configuration.html)  
  - or [more](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html)
- Enable [gzip content-encoding](https://www.rightbrainnetworks.com/2013/03/21/serving-compressed-gzipped-static-files-from-amazon-s3-or-cloudfront/)

## Step 4:

Update the naming following the template as per the example html file herewithin.
