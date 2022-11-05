""" CD warehouse(倉庫)
Customer can buy CDs, 
searching on the title and the artest
Record labels send batches of CDs to the warehouse
Customer can only order titles are in stock

Design TestCase:
Buy a CD:
- In Stock -> quantity bought deducted from stock
- Insufficient Stock -> raise an exception

Search for a CD:
- In catalogue -> return the matching CD
- Not in catalogue -> return null

Receiving batch of CD:
- Copies of 1 CD in catalogue -> add copies to CD
- Copies of 1 CD not in catalogue -> CD add to catalogue with copies
- Multiple CD in batch -> add any missing CDs to catalogue, add copies each CD
"""