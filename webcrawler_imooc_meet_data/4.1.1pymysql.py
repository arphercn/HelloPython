import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='test_python',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `urls` (`name`, `url`) VALUES (%s, %s)"
        cursor.execute(sql, ('baidu', 'www.baidu.com'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `name`, `url` FROM `urls` WHERE `name`=%s"
        cursor.execute(sql, ('baidu',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()