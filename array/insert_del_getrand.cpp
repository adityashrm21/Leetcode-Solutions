class RandomizedSet {
public:
    /** Initialize your data structure here. */
    
    unordered_map<int,int> mp;
    vector<int> nums;
    
    RandomizedSet() {
        
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        
        if(mp.find(val)!=mp.end())
        return false;
        
        
        nums.push_back(val);
        int n=nums.size();
        mp[val]=n-1;
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        
        if(mp.find(val)==mp.end())
        {
            return false;
        }
        
        int last=nums.back();
        nums[mp[val]]=last;
        nums.pop_back();
        mp[last]=mp[val];
        mp.erase(val);
        
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        
        
        return nums[rand()%nums.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */