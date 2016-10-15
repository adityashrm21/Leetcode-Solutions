class Queue {
public:
    // Push element x to the back of queue.
    stack<int> s1, s2;
    
    void push(int x) {
        
        while(!s1.empty())
        {
            int top=s1.top();
            s2.push(top);
            s1.pop();
        }
        
        s1.push(x);
        
        while(!s2.empty())
        {
            int top=s2.top();
            s1.push(top);
            s2.pop();
        }
    }

    // Removes the element from in front of queue.
    void pop(void) {
        
        if(!s1.empty())
        s1.pop();
    }

    // Get the front element.
    int peek(void) {
       
       return s1.top();
        
    }

    // Return whether the queue is empty.
    bool empty(void) {
        
        if(s1.empty()) return true;
        return false;
    }
};