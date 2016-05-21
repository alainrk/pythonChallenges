# The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. 

class PaginationHelper:
    
  def chunks(self, l, n):
      for i in range(0, len(l), n):
          yield l[i:i+n]

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.pages = list(self.chunks(collection, items_per_page))
      self.numItems = len(collection)
      self.itemsMax = items_per_page
      
  # returns the number of items within the entire collection
  def item_count(self):
      return reduce(lambda a,b: a+b, (len(i) for i in self.pages))
  
  # returns the number of pages
  def page_count(self):
      return len(self.pages)
  
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      return len(self.pages[page_index]) if 0<=page_index<len(self.pages) else -1
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      return int(item_index/self.itemsMax) if 0<=item_index<self.numItems else -1    
