import pymongo
import inspect


class Base(dict):
    def __init__(self):
        self.client = pymongo.MongoClient()

    def _tuple_to_dict(self, items):
        return {item[0]: item[1] for item in items}
    def insert(self, dbname):
        collname = self.__class__.__name__
        db = self.client[dbname]
        collection = db[collname]
        pairs = self._tuple_to_dict(
                list(filter(lambda x: not(x[0].startswith('__')) and x[0] != 'client',
                    inspect.getmembers(self, lambda x: not(inspect.isroutine(x)))))
                )
        collection.insert(pairs)


class DB(dict):
    def __init__(self):
        self.client = pymongo.MongoClient()

    def _inner(self):
        collnames = self.collections

    def createCollection(self, name):
        self.collections.append(name)

    def getCollections(self):
        return self.collections


class Collection:
    def __init__(self, items):
        self.items = items
        self.client = pymongo.MongoClient()

    def insert(self, dbname):
        coll = self.client[dbname][self.__class__.__name__]
        coll.insert(self.items)

