from SharesDao import shareDao

share1 = {
    'id': 1,
    'price': 117,
    'symbol': 'APPL',
    'name': 'Apple inc'

}
share2 = {
    'id': 2,
    'price': 37,
    'symbol': 'PFE',
    'name': 'Pfizer'

}

#returnValue = shareDao.create(share)
returnValue = shareDao.getAll()
print(returnValue)
returnValue = shareDao.findById(share2['id'])
print("find By Id")
print(returnValue)
returnValue = shareDao.update(share2)
print(returnValue)
returnValue = shareDao.findById(share2['id'])
print(returnValue)
returnValue = shareDao.delete(share2['id'])
print(returnValue)
returnValue = shareDao.getAll()
print(returnValue)