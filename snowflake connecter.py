import snowflake.connector
import os
#conn = snow.connect() // you need to pass required account info and credentials here


conn = snowflake.connector.connect(
    user='pthakar',
    password='Newlearning@123',
    account='XQ31534.ca-central-1.aws',
    warehouse='COMPUTE_WH'
    )

conn.cursor().execute("put file://my_third_file.txt @demo_db.public.my_internal_named_stage")
