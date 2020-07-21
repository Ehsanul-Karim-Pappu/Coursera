import sqlite3

conn = sqlite3.connect("orgdb.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

for line in open(input()):
    if not line.startswith('From: '):
        continue
    org = line.split()[1].split('@')[1]
    # print(org)
    cur.execute("SELECT count FROM Counts WHERE org = '%s'" % org)
    cnt = cur.fetchone()
    # print(cnt)
    if cnt == None:
        cur.execute("INSERT INTO Counts (org, count) VALUES ('%s', 1)" % org)
    else:
        cur.execute(
            "UPDATE Counts SET count = count + 1 WHERE org = '%s'" % org)

conn.commit()

# sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 20"

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

cur.close()
