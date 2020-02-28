################################################
# Week 3.3: Accessing Databases with SQL Magic #
################################################

import sqlalchemy
import ibm_db_sa

# Enter your Db2 credentials in the connection string below
# Recall you created Service Credentials in Part III of the first lab of the course in Week 1
# i.e. from the uri field in the Service Credentials copy everything after db2:// (but remove the double quote at the end)
# for example, if your credentials are as in the screenshot above, you would write:
# %sql ibm_db_sa://my-username:my-password@dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net:50000/BLUDB
# Note the ibm_db_sa:// prefix instead of db2://
# This is because JupyterLab's ipython-sql extension uses sqlalchemy (a python SQL toolkit)
# which in turn uses IBM's sqlalchemy dialect: ibm_db_sa
#%

from sqlalchemy import create_engine

e = create_engine("db2+ibm_db://bzr25790:9nqsnndjss-d342r@dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net:50000/BLUDB")
























# in order to display plot within window
# plt.show()
