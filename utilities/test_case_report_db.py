from mysql import connector

class TestCase_Results:

    db_conn = connector.connect(host="localhost", user="root", passwd="Shonya@0803")
    db_cursor = db_conn.cursor()
    db_cursor.execute("use test_reports")


    def test_case_report_from_db(self,report_query):
        self.db_cursor.execute("use test_reports")
        self.db_cursor.execute(report_query)
        self.db_conn.commit()
        self.db_conn.close()
