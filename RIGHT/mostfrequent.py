class solution:
  def topKFrequent(self,nums: List[int], k:int)-> List[int]:
    count={}
    frequ=[[] for i in range(len(nums)+1)]
