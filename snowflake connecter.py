import snowflake.connector
#conn = snow.connect() // you need to pass required account info and credentials here


conn = snowflake.connector.connect(
    user='pthakar',
    password='Newlearning@123',
    account='XQ31534.ca-central-1.aws',
    warehouse='COMPUTE_WH'
    )

connection.cursor().execute("put file://my_third_file.txt @util_db.public.my_internal_named_stage")
